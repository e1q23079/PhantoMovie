import numpy as np

from ..lib import lsb
from ..lib.img import IMG


class Diff:
    def __init__(self, img: np.ndarray):
        """
        画像の差分を計算するクラス
        :param img: 画像データ
        """
        self.img = IMG(img)

    def _diff_pixel(self, x: int, y: int) -> list[int]:
        """
        指定された座標のピクセル値の差分を計算する
        :param x: x座標
        :param y: y座標
        :return: 計算されたピクセル値の差分
        """
        img1_pixel_r = self.img.bgr.get_r(x, y)
        img1_pixel_g = self.img.bgr.get_g(x, y)
        img1_pixel_b = self.img.bgr.get_b(x, y)
        if lsb.get_lsb(img1_pixel_r) == 1:
            result_pixel_r = 255
        else:
            result_pixel_r = 0
        if lsb.get_lsb(img1_pixel_g) == 1:
            result_pixel_g = 255
        else:
            result_pixel_g = 0
        if lsb.get_lsb(img1_pixel_b) == 1:
            result_pixel_b = 255
        else:
            result_pixel_b = 0
        return [result_pixel_b, result_pixel_g, result_pixel_r]

    def get_diff(self):
        """
        画像の差分を計算する
        :return: 差分画像
        """
        height = self.img.height
        width = self.img.width
        result = np.full((height, width, 3), 255, dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                pixel = self._diff_pixel(x, y)
                result[y, x] = pixel
        return result
