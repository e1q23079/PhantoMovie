import numpy as np

from ..lib import binary
from ..lib.img import IMG


class Diff:
    """
    画像の差分を計算するクラス
    """

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

        result_pixel_r = binary.revert_classify(binary.get_4b(img1_pixel_r))
        result_pixel_g = binary.revert_classify(binary.get_4b(img1_pixel_g))
        result_pixel_b = binary.revert_classify(binary.get_4b(img1_pixel_b))
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
