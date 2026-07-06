from logging import getLogger
from tkinter import messagebox as MessageBox
from typing import TYPE_CHECKING

from ..controller.analyze_controller import AnalyzeController
from ..controller.convert_controller import ConvertController
from ..controller.player_controller import PlayerController
from ..controller.upload_controller import UploadController
from ..model.file import File
from ..service.player import Player

if TYPE_CHECKING:
    from ..ui.main_window import MainWindow

logger = getLogger(__name__)


class AppController:
    """
    AppControllerクラスは、アプリケーション全体の制御を行うクラス
    """

    def __init__(self, main_window: "MainWindow"):
        """
        AppControllerクラスの初期化
        """
        self.main_window = main_window
        self.file = File()
        self.player = None
        # ウィンドウ終了時のイベントバインド
        self.main_window.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.run()

    def run(self):
        """
        アプリケーションを実行するメソッド
        """
        self.player = Player()

        self.player_controller = PlayerController(self.main_window, self.player)
        self.upload_controller = UploadController(self.file)

        self.convert_controller = ConvertController(
            self.main_window, self.upload_controller
        )
        self.analyze_controller = AnalyzeController(
            self.main_window, self.player, self.upload_controller
        )

        self.main_window.player_frame.play_stop_btn.config(
            command=self.player_controller.play_stop_btn
        )
        self.main_window.player_frame.back_btn.config(
            command=self.player_controller.play_backward_movie
        )
        self.main_window.player_frame.forward_btn.config(
            command=self.player_controller.play_forward_movie
        )

        self.main_window.upload_frame.upload_public_movie_btn.config(
            command=self.upload_controller.select_public_movie
        )

        self.main_window.upload_frame.upload_private_movie_btn.config(
            command=self.upload_controller.select_private_movie
        )

        self.main_window.upload_frame.convert_btn.config(
            command=self.convert_controller.convert_btn_click
        )

        self.main_window.upload_frame.analyze_btn.config(
            command=self.analyze_controller.analyze_btn_click
        )

    def on_exit(self):
        """
        アプリケーション終了時の処理を行うメソッド
        """
        ret = MessageBox.askokcancel("確認", "本当に終了しますか？")
        if ret:
            if (
                self.convert_controller.is_processing()
                or self.analyze_controller.is_processing()
            ):
                MessageBox.showwarning(
                    "警告", "変換または解析処理中のため、終了できません。"
                )
                return
            self.main_window.destroy()
