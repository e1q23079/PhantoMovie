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

    def setup(self):
        """
        ウィンドウの初期設定を行うメソッド
        """
        self.title("PhantoMovie")
        self.geometry("500x365")
        self.resizable(False, False)
        self.create_widgets()

        self.player_btn_state("disabled")

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

    def all_btn_state(self, state):
        """
        すべてのボタンの状態を変更するメソッド
        """
        self.upload_frame.convert_btn.config(state=state)
        self.upload_frame.analyze_btn.config(state=state)
        self.player_frame.play_stop_btn.config(state=state)
        self.player_frame.forward_btn.config(state=state)
        self.player_frame.back_btn.config(state=state)
        self.upload_frame.upload_public_movie_btn.config(state=state)
        self.upload_frame.upload_private_movie_btn.config(state=state)

    def convert_btn_state(self, state):
        """
        変換ボタンの状態を変更するメソッド
        """
        self.upload_frame.convert_btn.config(state=state)

    def analyze_btn_state(self, state):
        """
        分析ボタンの状態を変更するメソッド
        """
        self.upload_frame.analyze_btn.config(state=state)

    def player_btn_state(self, state):
        """
        プレイヤーボタンの状態を変更するメソッド
        """
        self.player_frame.play_stop_btn.config(state=state)
        self.player_frame.forward_btn.config(state=state)
        self.player_frame.back_btn.config(state=state)

    def run(self):
        """
        アプリケーションを実行するメソッド
        """
        self.mainloop()
