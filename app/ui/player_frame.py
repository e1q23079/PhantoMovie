import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..ui.main_window import MainWindow


class PlayerFrame:
    def __init__(self, main_window: "MainWindow"):
        """
        PlayerFrameクラスの初期化
        :param main_window: 親ウィンドウ
        :param player_controller: プレイヤーコントローラー
        """
        self.main_window = main_window
        self.create_widgets()

    def create_widgets(self):
        """
        ウィジェットの作成と配置を行うメソッド
        :param frame: 親フレーム
        """
        # コントロールフレーム
        control_frame = tk.Frame(self.main_window)
        control_frame.grid(row=1, column=0, padx=10, pady=1)

        self.back_btn = tk.Button(control_frame, text="戻る")
        self.back_btn.grid(row=0, column=0, pady=1)

        self.play_stop_btn = tk.Button(
            control_frame,
            text="再生/停止",
        )
        self.play_stop_btn.grid(row=0, column=1, pady=1)

        self.forward_btn = tk.Button(
            control_frame,
            text="進む",
        )
        self.forward_btn.grid(row=0, column=2, pady=1)
