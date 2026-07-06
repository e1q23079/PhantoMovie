import threading
from logging import getLogger
from tkinter import messagebox as MessageBox
from typing import TYPE_CHECKING

from ..service.analyze import Analyze
from ..service.data import Data
from ..service.player import Player

if TYPE_CHECKING:
    from ..controller.upload_controller import UploadController
    from ..ui.main_window import MainWindow

logger = getLogger(__name__)


class AnalyzeController:
    def __init__(
        self,
        main_window: "MainWindow",
        player: "Player",
        upload_controller: "UploadController",
    ):
        self.main_window = main_window
        self.data = Data()
        self.player = player
        self.upload_controller = upload_controller

    def analyze_thread(self):
        """
        解析処理を別スレッドで実行する
        """
        analyze_data = self.analyzer.analyze()
        self.player.set_frames(analyze_data.get_frames())
        MessageBox.showinfo("解析完了", "動画の解析が完了しました。")
        if self.public_movie is not None:
            self.public_movie.release()

    def analyze_btn_click(self):
        """ "
        解析ボタンがクリックされたときの処理
        """
        logger.debug("Analyzing video...")

        # 公開動画の取得
        self.public_movie = self.upload_controller.file.get_public_movie()

        # 公開動画ファイル読み込みの確認
        if self.public_movie is None:
            logger.error("Public movie path is not set.")
            return

        # アナライザー
        self.analyzer = Analyze(public_movie=self.public_movie)

        status = self.analyzer._is_check()

        if not status:
            logger.error("Failed to open the public video.")
            return

        thread = threading.Thread(target=self.analyze_thread)
        thread.start()

        self.main_window.progress_frame.start(self.analyzer.get_progress)
