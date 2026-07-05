import tkinter as tk
from logging import getLogger
from tkinter import filedialog

import cv2
from PIL import Image, ImageTk

from .system.convert import Convert
from .system.file import File
from .system.save import Save


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PhantoMovie")
        self.geometry("500x340")
        self.resizable(False, False)
        self.create_widgets()
        self.file = File()
        self.logger = getLogger(__name__)

    def create_widgets(self):

        self.movie = cv2.VideoCapture("output_diff.avi")
        ret = self.movie.isOpened()
        if not ret:
            img_pil = None
        img_pil = None

        # 中央ぞろえのために、グリッドの列と行の重みを設定
        self.grid_columnconfigure(0, weight=1)

        movie_frame = tk.Frame(self)
        movie_frame.grid(row=0, column=0, padx=10, pady=1)

        control_frame = tk.Frame(self)
        control_frame.grid(row=1, column=0, padx=10, pady=1)

        self.canvas = tk.Canvas(
            movie_frame, width=427, height=240, bg="black", bd=0, highlightthickness=0
        )
        if img_pil is not None:
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)
        self.canvas.grid(row=0, column=0, columnspan=3, pady=1)

        self.back = tk.Button(control_frame, text="戻る", command=self.on_button_click)
        self.back.grid(row=0, column=0, pady=1)

        self.play_stop = tk.Button(
            control_frame, text="再生/停止", command=self.play_movie
        )
        self.play_stop.grid(row=0, column=1, pady=1)

        self.forward = tk.Button(
            control_frame, text="進む", command=self.on_button_click
        )
        self.forward.grid(row=0, column=2, pady=1)

        public_upload_frame = tk.Frame(self)
        public_upload_frame.grid(row=2, column=0, padx=10, pady=1)

        self.upload_public_movie = tk.Button(
            public_upload_frame,
            text="「公開動画」を選択",
            command=self.select_public_movie,
        )
        self.upload_public_movie.grid(row=0, column=0, columnspan=2, pady=1)

        self.analyze = tk.Button(
            public_upload_frame, text="解析", command=self.on_button_click
        )
        self.analyze.grid(row=0, column=2, padx=10, pady=1)

        private_upload_frame = tk.Frame(self)
        private_upload_frame.grid(row=3, column=0, padx=10, pady=1)

        self.upload_private_movie = tk.Button(
            private_upload_frame,
            text="「秘密動画」を選択",
            command=self.select_private_movie,
        )
        self.upload_private_movie.grid(row=0, column=0, columnspan=2, pady=1)

        self.convert = tk.Button(
            private_upload_frame, text="変換", command=self.convert_btn_click
        )
        self.convert.grid(row=0, column=2, padx=10, pady=1)

    def select_public_movie(self):
        # Logic to select the public movie
        print("Selecting public movie...")
        filename = filedialog.askopenfilename(
            title="公開",
            filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*")),
        )
        self.file.set_public_movie_path(filename)

    def select_private_movie(self):
        # Logic to select the private movie
        print("Selecting private movie...")
        filename = filedialog.askopenfilename(
            title="秘密",
            filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*")),
        )
        self.file.set_private_movie_path(filename)

    def on_button_click(self):
        print("Button clicked!")

    def convert_btn_click(self):
        # Logic to convert the video
        print("Converting video...")
        filename = filedialog.asksaveasfilename(
            title="変換後の動画を保存",
            defaultextension=".avi",
            filetypes=(("AVI files", "*.avi"), ("All files", "*.*")),
        )

        # 動画の取得
        public_movie = self.file.get_public_movie()
        secret_movie = self.file.get_private_movie()

        # 公開動画ファイル読み込みの確認
        if public_movie is None:
            self.logger.error("Public movie path is not set.")
            return

        # 秘密動画ファイル読み込みの確認
        if secret_movie is None:
            self.logger.error("Secret movie path is not set.")
            return

        # コンバーター
        converter = Convert(
            public_movie=public_movie,
            private_movie=secret_movie,
        )

        status = converter._is_check()

        if not status:
            self.logger.error("Failed to open one or both videos.")
            return

        convert_data, width, height = converter.convert()

        save = Save(filename=filename, fps=30, width=width, height=height)
        save.save(convert_data)

    def next_frame(self):
        # Logic to go to the next frame
        print("Next frame...")
        ret, img_bgr = self.movie.read()
        if not ret:
            print("Error reading frame")
            return
        img_bgr = cv2.resize(img_bgr, (427, 240))
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

        img_pil = Image.fromarray(img_rgb)
        self.img_tk = ImageTk.PhotoImage(img_pil)

        if img_pil is not None:
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)
        self.canvas.grid(row=0, column=0, columnspan=3, pady=1)

        self.after(33, self.next_frame)

    def play_movie(self):
        # Logic to play the movie
        print("Playing movie...")
        self.after(33, self.next_frame)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = Application()
    app.run()
