from ...func import lsb
from ...img import IMG


class ReFormula:
    def __init__(self, img: IMG):
        """
        画像処理の式を初期化する
        :param img: 画像データ
        """
        self.img = img

    def _diff_pixel(self, value) -> int:
        """
        指定された座標のピクセル値の差分を計算する
        :param value: ピクセル値
        :return: 計算されたピクセル値の差分
        """
        if lsb.get_lsb(value) == 1:
            result = 255
        else:
            result = 0

        return result

    def __call__(self, x: int, y: int) -> list[int]:
        """
        指定された座標のピクセル値を計算する
        :param x: x座標
        :param y: y座標
        :return: 計算されたピクセル値
        """
        img1_pixel_r = self.img.bgr.get_r(x, y)
        img1_pixel_g = self.img.bgr.get_g(x, y)
        img1_pixel_b = self.img.bgr.get_b(x, y)

        result_pixel_r = self._diff_pixel(img1_pixel_r)
        result_pixel_g = self._diff_pixel(img1_pixel_g)
        result_pixel_b = self._diff_pixel(img1_pixel_b)

        return [result_pixel_b, result_pixel_g, result_pixel_r]
