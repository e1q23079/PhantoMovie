import threading
import tkinter as tk
import tkinter.ttk as ttk
from logging import getLogger
from tkinter import filedialog
from tkinter import messagebox as MessageBox

import cv2
from PIL import Image, ImageTk

from .model.file import File
from .service.analyze import Analyze
from .service.convert import Convert
from .service.player import Player
from .service.writer import Writer


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PhantoMovie")
        self.geometry("500x365")
        self.resizable(False, False)
        self.create_widgets()
        self.file = File()
        self.player = None
        self.logger = getLogger(__name__)
        # ウィンドウ終了時のイベントバインド
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

    def create_widgets(self):
        """
        ウィジェットの作成と配置
        """
        # 中央ぞろえのために、グリッドの列と行の重みを設定
        self.grid_columnconfigure(0, weight=1)

        # 動画フレーム
        movie_frame = tk.Frame(self)
        movie_frame.grid(row=0, column=0, padx=10, pady=1)

        self.canvas = tk.Canvas(
            movie_frame, width=427, height=240, bg="black", bd=0, highlightthickness=0
        )
        self.canvas.create_image(0, 0, anchor=tk.NW)
        self.canvas.grid(row=0, column=0, columnspan=3, pady=1)

        # コントロールフレーム
        control_frame = tk.Frame(self)
        control_frame.grid(row=1, column=0, padx=10, pady=1)

        self.back = tk.Button(
            control_frame, text="戻る", command=self.play_backward_movie
        )
        self.back.grid(row=0, column=0, pady=1)

        self.play_stop = tk.Button(
            control_frame, text="再生/停止", command=self.play_stop_btn
        )
        self.play_stop.grid(row=0, column=1, pady=1)

        self.forward = tk.Button(
            control_frame, text="進む", command=self.play_forward_movie
        )
        self.forward.grid(row=0, column=2, pady=1)

        # 公開動画アップロードフレーム
        public_upload_frame = tk.Frame(self)
        public_upload_frame.grid(row=2, column=0, padx=10, pady=1)

        self.upload_public_movie = tk.Button(
            public_upload_frame,
            text="「公開動画」を選択",
            command=self.select_public_movie,
        )
        self.upload_public_movie.grid(row=0, column=0, columnspan=2, pady=1)

        self.analyze = tk.Button(
            public_upload_frame, text="解析", command=self.analyze_btn_click
        )
        self.analyze.grid(row=0, column=2, padx=10, pady=1)

        # 秘密動画アップロードフレーム
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

        # 進捗バーフレーム
        status_frame = tk.Frame(self)
        status_frame.grid(row=4, column=0, padx=10, pady=1, sticky=tk.W + tk.E)

        self.progress = ttk.Progressbar(status_frame, mode="determinate", maximum=1)
        self.progress.pack(fill=tk.X, padx=10, pady=1)

    def update_progress_convert(self):
        """
        進捗バーの更新（変換処理用）
        """
        progress = self.converter.get_progress()
        self.progress["value"] = progress
        self.update_idletasks()
        if progress < 1.0:
            self.after(100, self.update_progress_convert)

    def update_progress_analyze(self):
        """
        進捗バーの更新（解析処理用）
        """
        progress = self.analyzer.get_progress()
        self.progress["value"] = progress
        self.update_idletasks()
        if progress < 1.0:
            self.after(100, self.update_progress_analyze)

    def select_public_movie(self):
        """
        アップロードする公開動画を選択するためのファイルダイアログを開く
        """
        print("Selecting public movie...")
        filename = filedialog.askopenfilename(
            title="公開",
            filetypes=(("Video files", "*.mp4 *.avi"), ("All files", "*.*")),
        )
        self.file.set_public_movie_path(filename)

    def select_private_movie(self):
        """
        アップロードする秘密動画を選択するためのファイルダイアログを開く
        """
        print("Selecting private movie...")
        filename = filedialog.askopenfilename(
            title="秘密",
            filetypes=(("Video files", "*.mp4 *.avi"), ("All files", "*.*")),
        )
        self.file.set_private_movie_path(filename)

    def on_button_click(self):
        """
        ボタンがクリックされたときの処理
        """
        print("Button clicked!")

    def convert_thread(self):
        """
        変換処理を別スレッドで実行する
        """
        convert_data, width, height = self.converter.convert()

        writer = Writer(
            filename=self.output_filename, fps=30, width=width, height=height
        )
        writer.save(convert_data)
        MessageBox.showinfo("変換完了", "動画の変換が完了しました。")
        if self.public_movie is not None:
            self.public_movie.release()
        if self.secret_movie is not None:
            self.secret_movie.release()

    def analyze_thread(self):
        """
        解析処理を別スレッドで実行する
        """
        analyze_data = self.analyzer.analyze()
        self.player = Player(frames=analyze_data.get_frames())
        MessageBox.showinfo("解析完了", "動画の解析が完了しました。")
        if self.public_movie is not None:
            self.public_movie.release()

    def analyze_btn_click(self):
        """ "
        解析ボタンがクリックされたときの処理
        """
        print("Analyzing video...")

        # 公開動画の取得
        self.public_movie = self.file.get_public_movie()

        # 公開動画ファイル読み込みの確認
        if self.public_movie is None:
            self.logger.error("Public movie path is not set.")
            return

        # アナライザー
        self.analyzer = Analyze(public_movie=self.public_movie)

        status = self.analyzer._is_check()

        if not status:
            self.logger.error("Failed to open the public video.")
            return

        thread = threading.Thread(target=self.analyze_thread)
        thread.start()

        self.after(100, self.update_progress_analyze)

    def convert_btn_click(self):
        """ "
        変換ボタンがクリックされたときの処理
        """
        print("Converting video...")
        self.output_filename = filedialog.asksaveasfilename(
            title="変換後の動画を保存",
            defaultextension=".avi",
            filetypes=(("AVI files", "*.avi"), ("All files", "*.*")),
        )

        if not self.output_filename:
            self.logger.error("No output filename specified.")
            return

        # 動画の取得
        self.public_movie = self.file.get_public_movie()
        self.secret_movie = self.file.get_private_movie()

        # 公開動画ファイル読み込みの確認
        if self.public_movie is None:
            self.logger.error("Public movie path is not set.")
            return

        # 秘密動画ファイル読み込みの確認
        if self.secret_movie is None:
            self.logger.error("Secret movie path is not set.")
            return

        # コンバーター
        self.converter = Convert(
            public_movie=self.public_movie,
            private_movie=self.secret_movie,
        )

        status = self.converter._is_check()

        if not status:
            self.logger.error("Failed to open one or both videos.")
            return

        thread = threading.Thread(target=self.convert_thread)
        thread.start()

        self.after(100, self.update_progress_convert)

    def next_frame(self):
        """
        次のフレームを表示する
        """
        print("Next frame...")
        if self.player is None:
            print("Movie is not loaded.")
            return
        if self.player.get_is_playing() is False:
            print("Movie is not playing.")
            return
        ret, img_bgr = self.player.get_frame()
        if not ret:
            self.player.reset_current_frame_index()
            self.player.stop_movie()
            print("Error reading frame")
            return
        if img_bgr is None:
            print("No more frames to display.")
            return
        img_bgr = cv2.resize(img_bgr, (427, 240))
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

        img_pil = Image.fromarray(img_rgb)
        self.img_tk = ImageTk.PhotoImage(img_pil)

        if img_pil is not None:
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)
        self.canvas.grid(row=0, column=0, columnspan=3, pady=1)

        self.after(33, self.next_frame)

    def play_stop_btn(self):
        """
        再生/停止ボタンがクリックされたときの処理
        """
        print("Play/Stop button clicked...")
        if self.player is None:
            print("Movie is not loaded.")
            return
        if self.player.get_is_playing():
            self.stop_movie()
        else:
            self.play_movie()

    def stop_movie(self):
        """
        動画を停止する
        """
        print("Stopping movie...")
        if self.player is None:
            print("Movie is not loaded.")
            return
        self.player.stop_movie()

    def play_movie(self):
        """
        動画を再生する
        """
        print("Playing movie...")
        if self.player is None:
            print("Movie is not loaded.")
            return
        self.player.play_movie()
        self.after(33, self.next_frame)

    def play_forward_movie(self):
        """
        動画を早送りする
        """
        print("Forwarding movie...")
        if self.player is None:
            print("Movie is not loaded.")
            return
        self.player.forward_movie()
        self.next_frame()

    def play_backward_movie(self):
        """
        動画を巻き戻す
        """
        print("Rewinding movie...")
        if self.player is None:
            print("Movie is not loaded.")
            return
        self.player.backward_movie()
        self.next_frame()

    # ウィンドウ終了時の処理
    def on_exit(self):
        """
        ウィンドウ終了時の処理
        """
        ret = MessageBox.askokcancel("確認", "本当に終了しますか？")
        if ret:
            self.destroy()

    def run(self):
        """
        アプリケーションを実行する
        """
        self.mainloop()


if __name__ == "__main__":
    app = Application()
    app.run()
