import threading
from logging import getLogger
from tkinter import messagebox as MessageBox
from typing import TYPE_CHECKING

import cv2

from ..service.analyze import Analyze
from ..service.data import Data
from ..service.player import Player

if TYPE_CHECKING:
    from ..controller.upload_controller import UploadController
    from ..ui.main_window import MainWindow

logger = getLogger(__name__)


class AnalyzeController:
    """
    AnalyzeControllerクラスは、動画解析の制御を行うクラス
    """

    def __init__(
        self,
        main_window: "MainWindow",
        player: "Player",
        upload_controller: "UploadController",
    ):
        """
        AnalyzeControllerクラスの初期化
        """
        self.main_window = main_window
        self.data = Data()
        self.player = player
        self.upload_controller = upload_controller
        self.analyzer = None

    def analyze_thread(self):
        """
        解析処理を別スレッドで実行する
        """
        self.main_window.all_btn_state("disabled")
        if self.analyzer is None:
            logger.error("Analyzer is not initialized.")
            return
        analyze_data = self.analyzer.analyze()
        self.player.set_frames(analyze_data.get_frames())
        MessageBox.showinfo("解析完了", "動画の解析が完了しました。")
        self.main_window.all_btn_state("normal")
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
            MessageBox.showerror("エラー", "「公開動画」が選択されていません。")
            return

        self.player.set_fps(self.public_movie.get(cv2.CAP_PROP_FPS))

        # アナライザー
        self.analyzer = Analyze(public_movie=self.public_movie)

        status = self.analyzer._is_check()

        if not status:
            logger.error("Failed to open the public video.")
            MessageBox.showerror("エラー", "「公開動画」の読み込みに失敗しました。")
            return

        thread = threading.Thread(target=self.analyze_thread)
        thread.start()

        self.main_window.progress_frame.start(self.analyzer.get_progress)

    def is_processing(self):
        """
        解析処理中かどうかを返す
        """
        if self.analyzer is None:
            return False
        return self.analyzer.is_processing()
