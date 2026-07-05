import numpy as np

from ..lib.bgr import BGR


class IMG:
    """
    画像処理に関するクラス
    """

    def __init__(self, img: np.ndarray):
        """
        画像を初期化する
        :param img: 画像データ
        """
        self.img = img
        self.height = self._get_height()
        self.width = self._get_width()
        self.bgr = BGR(self.img)

    def get_img(self) -> np.ndarray:
        """
        画像データを取得する
        :return: 画像データ
        """
        return self.img

    def get_pixel(self, x: int, y: int) -> np.ndarray:
        """
        指定された座標のピクセル値を取得する
        :param x: x座標
        :param y: y座標
        :return: ピクセル値
        """
        return self.img[y, x]

    def _get_height(self) -> int:
        """
        画像の高さを取得する
        :return: 画像の高さ
        """
        return self.img.shape[0]

    def _get_width(self) -> int:
        """
        画像の幅を取得する
        :return: 画像の幅
        """
        return self.img.shape[1]
