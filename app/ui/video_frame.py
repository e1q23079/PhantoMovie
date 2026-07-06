import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..ui.main_window import MainWindow


class VideoFrame:
    """
    VideoFrameクラスは、動画を表示するためのフレームを表すクラス
    """

    def __init__(self, main_window: "MainWindow"):
        """
            VideoFrameクラスの初期化
        :param main_window: 親ウィンドウ
        """
        # 動画フレーム
        movie_frame = tk.Frame(main_window)
        movie_frame.grid(row=0, column=0, padx=10, pady=1)

        self.canvas = tk.Canvas(
            movie_frame, width=427, height=240, bg="black", bd=0, highlightthickness=0
        )
        self.canvas.create_image(0, 0, anchor=tk.NW)
        self.canvas.grid(row=0, column=0, columnspan=3, pady=1)
