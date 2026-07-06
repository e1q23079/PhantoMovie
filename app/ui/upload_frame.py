import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..ui.main_window import MainWindow


class UploadFrame:
    """
    UploadFrameクラスは、動画のアップロードを行うフレームを表すクラス
    """

    def __init__(
        self,
        main_window: "MainWindow",
    ):
        """
        UploadFrameクラスの初期化
        :param main_window: 親ウィンドウ
        """
        self.main_window = main_window
        self.create_widgets()

    def create_widgets(self):
        """
        ウィジェットの作成と配置を行うメソッド
        :param frame: 親フレーム
        """
        # 公開動画アップロードフレーム
        public_upload_frame = tk.Frame(self.main_window)
        public_upload_frame.grid(row=2, column=0, padx=10, pady=1)

        self.upload_public_movie_btn = tk.Button(
            public_upload_frame, text="「公開動画」を選択"
        )
        self.upload_public_movie_btn.grid(row=0, column=0, columnspan=2, pady=1)

        self.analyze_btn = tk.Button(public_upload_frame, text="解析")
        self.analyze_btn.grid(row=0, column=2, padx=10, pady=1)

        # 秘密動画アップロードフレーム
        private_upload_frame = tk.Frame(self.main_window)
        private_upload_frame.grid(row=3, column=0, padx=10, pady=1)

        self.upload_private_movie_btn = tk.Button(
            private_upload_frame, text="「秘密動画」を選択"
        )
        self.upload_private_movie_btn.grid(row=0, column=0, columnspan=2, pady=1)

        self.convert_btn = tk.Button(private_upload_frame, text="変換")
        self.convert_btn.grid(row=0, column=2, padx=10, pady=1)
