from logging import getLogger

import cv2

from ..lib.diff import Diff
from ..system.data import Data


class Analyze:
    def __init__(self, public_movie: cv2.VideoCapture):
        self.public_movie = public_movie
        self.current_frame = 0
        self.total_frames = self.get_total_frames()
        self.logger = getLogger(__name__)
        self.data = Data()

    def _is_check(self):
        """
        動画が正しく読み込まれているかを確認するメソッド

        Returns:
            bool: 動画が正しく読み込まれている場合はTrue、そうでない場合はFalse
        """
        if not self.public_movie.isOpened():
            self.logger.error("Failed to open public movie.")
            return False
        return True

    def get_total_frames(self):
        """
        動画の総フレーム数を取得するメソッド

        Returns:
            int: 総フレーム数
        """
        public_total_frames = int(self.public_movie.get(cv2.CAP_PROP_FRAME_COUNT))
        return public_total_frames

    def get_progress(self):
        """
        解析の進捗状況を取得するメソッド

        Returns:
            float: 進捗状況（0.0から1.0の範囲）
        """
        if self.total_frames == 0:
            return 0.0
        return self.current_frame / self.total_frames

    def analyze(self):
        while True:
            # 公開動画のフレームを取得
            ret1, public_frame = self.public_movie.read()
            if not ret1:
                self.logger.error("Failed to read frame from public video.")
                break

            # 画像の差分
            diff = Diff(public_frame)
            diff_result = diff.get_diff()
            # データにフレームを追加
            self.data.add_frame(diff_result)
            self.current_frame += 1
            self.logger.debug(
                f"Processed frame {self.current_frame}/{self.total_frames}"
            )
            print(".", end="", flush=True)

        return self.data
