from logging import getLogger
from tkinter import messagebox as MessageBox

import cv2

from ..lib.composition2 import Composition
from ..service.data import Data

logger = getLogger(__name__)


class Convert:
    """
    Convertクラスは、公開動画と秘密動画を受け取り、動画の合成や差分の計算を行うためのクラス
    """

    def __init__(self, public_movie: cv2.VideoCapture, private_movie: cv2.VideoCapture):
        """
        Convertクラスの初期化
        """
        self.public_movie = public_movie
        self.private_movie = private_movie
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
        if not self.private_movie.isOpened():
            logger.error("Failed to open private movie.")
            MessageBox.showerror("エラー", "「秘密動画」の読み込みに失敗しました。")
            return False
        return True

    def get_total_frames(self) -> int:
        """
        動画の総フレーム数を取得するメソッド

        Returns:
            int: 総フレーム数
        """
        public_total_frames = int(self.public_movie.get(cv2.CAP_PROP_FRAME_COUNT))
        private_total_frames = int(self.private_movie.get(cv2.CAP_PROP_FRAME_COUNT))
        return min(public_total_frames, private_total_frames)

    def get_progress(self) -> float:
        """
        変換の進捗状況を取得するメソッド

        Returns:
            float: 進捗状況（0.0から1.0の範囲）
        """
        if self.total_frames == 0:
            return 0.0
        return self.current_frame / self.total_frames

    def convert(self) -> tuple[list, int, int, float]:
        """
        動画の変換処理を行うメソッド
        """
        while True:
            # 公開動画のフレームを取得
            ret1, public_frame = self.public_movie.read()
            if not ret1:
                logger.error("Failed to read frame from public video.")
                break

            fps = self.public_movie.get(cv2.CAP_PROP_FPS)

            # 秘密動画のフレームを取得
            ret2, secret_frame = self.private_movie.read()
            if not ret2:
                logger.error("Failed to read frame from secret video.")
                break

            # リサイズ
            public_frame = cv2.resize(public_frame, (427, 240))
            secret_frame = cv2.resize(secret_frame, (427, 240))

            # 画像の合成
            composition = Composition(public_frame, secret_frame)
            compose_result = composition.get_compose()

            # データの書き込み
            self.data.add_frame(compose_result)
            self.current_frame += 1
            logger.debug(f"Processed frame {self.current_frame}/{self.total_frames}")

        return (
            self.data.get_frames(),
            composition.get_width(),
            composition.get_height(),
            fps,
        )

    def is_processing(self) -> bool:
        """
        変換処理中かどうかを返すメソッド

        Returns:
            bool: 変換処理中の場合はTrue、そうでない場合はFalse
        """
        return self.current_frame < self.total_frames
