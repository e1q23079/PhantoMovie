import numpy as np

from ..lib.img import IMG
from ..lib.re_formula2 import ReFormula


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
        self.re_formula = ReFormula(self.img)

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
                pixel = self.re_formula(x, y)
                result[y, x] = pixel
        return result
