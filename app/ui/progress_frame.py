import tkinter as tk
import tkinter.ttk as ttk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..ui.main_window import MainWindow


class ProgressFrame:
    def __init__(self, main_window: "MainWindow"):
        self.main_window = main_window
        self.create_widgets()

    def create_widgets(self):
        """
        ウィジェットの作成と配置を行うメソッド
        :param frame: 親フレーム
        """
        # 進捗バーフレーム
        status_frame = tk.Frame(self.main_window)
        status_frame.grid(row=4, column=0, padx=10, pady=1, sticky=tk.W + tk.E)

        self.progress = ttk.Progressbar(status_frame, mode="determinate", maximum=1)
        self.progress.pack(fill=tk.X, padx=10, pady=1)

    def start(self, er):
        """
        進捗状況を更新を開始するメソッド
        """
        self.er = er
        self.update_progress()

    def update_progress(self):
        """
        進捗状況を更新するメソッド
        """
        progress = self.er()
        self.progress["value"] = progress
        self.main_window.update_idletasks()
        if progress < 1.0:
            self.main_window.after(100, self.update_progress)
