import tkinter as tk

import cv2
from PIL import Image, ImageTk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PhantoMovie")
        self.geometry("500x340")
        self.resizable(False, False)
        self.create_widgets()

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
            public_upload_frame, text="「公開動画」を選択", command=self.on_button_click
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
            command=self.on_button_click,
        )
        self.upload_private_movie.grid(row=0, column=0, columnspan=2, pady=1)

        self.convert = tk.Button(
            private_upload_frame, text="変換", command=self.on_button_click
        )
        self.convert.grid(row=0, column=2, padx=10, pady=1)

    def on_button_click(self):
        print("Button clicked!")

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
