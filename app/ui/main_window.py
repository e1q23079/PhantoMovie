import tkinter as tk

from ..controller.app_controller import AppController
from ..ui.player_frame import PlayerFrame
from ..ui.progress_frame import ProgressFrame
from ..ui.upload_frame import UploadFrame
from ..ui.video_frame import VideoFrame


class MainWindow(tk.Tk):
    """
    MainWindowクラスは、PhantoMovieアプリケーションのメインウィンドウを表すクラス
    """

    def __init__(self):
        """
        MainWindowクラスの初期化
        """
        super().__init__()
        self.setup()
        self.controller = AppController(self)
        self.create_widgets()

    def setup(self):
        """
        ウィンドウの初期設定を行うメソッド
        """
        self.title("PhantoMovie")
        self.geometry("500x365")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        """
        ウィジェットの作成と配置を行うメソッド
        """
        # 中央ぞろえのために、グリッドの列と行の重みを設定
        self.grid_columnconfigure(0, weight=1)

        self.video_frame = VideoFrame(self)
        self.player_frame = PlayerFrame(self)
        self.upload_frame = UploadFrame(self)
        self.progress_frame = ProgressFrame(self)

    def run(self):
        """
        アプリケーションを実行するメソッド
        """
        self.mainloop()
