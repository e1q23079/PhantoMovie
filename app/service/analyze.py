from logging import getLogger
from tkinter import messagebox as MessageBox

import cv2

from ..lib.diff import Diff
from ..service.data import Data

logger = getLogger(__name__)


class Analyze:
    """
    Analyzeクラスは、公開動画を受け取り、動画の解析や差分の計算を行うためのクラス
    """

    def __init__(self, public_movie: cv2.VideoCapture):
        """
        Analyzeクラスの初期化

        Args:
            public_movie (cv2.VideoCapture): 公開動画のVideoCaptureオブジェクト
        """
        self.public_movie = public_movie
        self.current_frame = 0
        self.total_frames = self.get_total_frames()
        self.data = Data()

    def _is_check(self) -> bool:
        """
        動画が正しく読み込まれているかを確認するメソッド

        Returns:
            bool: 動画が正しく読み込まれている場合はTrue、そうでない場合はFalse
        """
        if not self.public_movie.isOpened():
            logger.error("Failed to open public movie.")
            MessageBox.showerror("エラー", "「公開動画」の読み込みに失敗しました。")
            return False
        return True

    def get_total_frames(self) -> int:
        """
        動画の総フレーム数を取得するメソッド

        Returns:
            int: 総フレーム数
        """
        public_total_frames = int(self.public_movie.get(cv2.CAP_PROP_FRAME_COUNT))
        return public_total_frames

    def get_progress(self) -> float:
        """
        解析の進捗状況を取得するメソッド

        Returns:
            float: 進捗状況（0.0から1.0の範囲）
        """
        if self.total_frames == 0:
            return 0.0
        return self.current_frame / self.total_frames

    def analyze(self) -> Data:
        """
        動画の解析処理を行うメソッド
        """
        while True:
            # 公開動画のフレームを取得
            ret1, public_frame = self.public_movie.read()
            if not ret1:
                logger.error("Failed to read frame from public video.")
                break

            # 画像の差分
            diff = Diff(public_frame)
            diff_result = diff.get_diff()
            # データにフレームを追加
            self.data.add_frame(diff_result)
            self.current_frame += 1
            logger.debug(f"Processed frame {self.current_frame}/{self.total_frames}")

        return self.data

    def is_processing(self) -> bool:
        """
        解析処理中かどうかを返すメソッド

        Returns:
            bool: 解析処理中の場合はTrue、そうでない場合はFalse
        """
        return self.current_frame < self.total_frames
