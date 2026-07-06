import threading
from logging import getLogger
from tkinter import filedialog
from tkinter import messagebox as MessageBox
from typing import TYPE_CHECKING

from ..service.convert import Convert
from ..service.writer import Writer

logger = getLogger(__name__)

if TYPE_CHECKING:
    from ..controller.upload_controller import UploadController
    from ..ui.main_window import MainWindow


class ConvertController:
    """
    ConvertControllerクラスは、動画変換の制御を行うクラス
    """

    def __init__(
        self, main_window: "MainWindow", upload_controller: "UploadController"
    ):
        """
        ConvertControllerクラスの初期化
        """
        self.main_window = main_window
        self.upload_controller = upload_controller
        self.converter = None

    def convert_thread(self):
        """
        変換処理を別スレッドで実行する
        """
        self.main_window.all_btn_state("disabled")
        if self.converter is None:
            logger.error("Converter is not initialized.")
            return
        convert_data, width, height = self.converter.convert()

        writer = Writer(
            filename=self.output_filename, fps=30, width=width, height=height
        )
        writer.save(convert_data)
        MessageBox.showinfo("変換完了", "動画の変換が完了しました。")
        self.main_window.all_btn_state("normal")
        if self.public_movie is not None:
            self.public_movie.release()
        if self.secret_movie is not None:
            self.secret_movie.release()

    def convert_btn_click(self):
        """ "
        変換ボタンがクリックされたときの処理
        """
        logger.debug("Converting video...")
        self.output_filename = filedialog.asksaveasfilename(
            title="変換後の動画を保存",
            defaultextension=".avi",
            filetypes=(("AVI files", "*.avi"), ("All files", "*.*")),
        )

        if not self.output_filename:
            logger.error("No output filename specified.")
            return

        # 動画の取得
        self.public_movie = self.upload_controller.file.get_public_movie()
        self.secret_movie = self.upload_controller.file.get_private_movie()

        # 公開動画ファイル読み込みの確認
        if self.public_movie is None:
            logger.error("Public movie path is not set.")
            MessageBox.showerror("エラー", "「公開動画」が選択されていません。")
            return

        # 秘密動画ファイル読み込みの確認
        if self.secret_movie is None:
            logger.error("Secret movie path is not set.")
            MessageBox.showerror("エラー", "「秘密動画」が選択されていません。")
            return

        # コンバーター
        self.converter = Convert(
            public_movie=self.public_movie,
            private_movie=self.secret_movie,
        )

        status = self.converter._is_check()

        if not status:
            logger.error("Failed to open one or both videos.")
            MessageBox.showerror("エラー", "動画の読み込みに失敗しました。")
            return

        thread = threading.Thread(target=self.convert_thread)
        thread.start()

        self.main_window.progress_frame.start(self.converter.get_progress)

    def is_processing(self):
        """
        変換処理中かどうかを返す
        """
        if self.converter is None:
            return False
        return self.converter.is_processing()
