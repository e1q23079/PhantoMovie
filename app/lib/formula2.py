from ..lib import binary
from ..lib.img import IMG


class Formula:
    """
    画像処理の式を表すクラス
    """

    def __init__(self, img1: IMG, img2: IMG):
        """
        画像処理の式を初期化する
        :param img1: 1枚目の画像データ
        :param img2: 2枚目の画像データ
        """
        self.img1 = img1
        self.img2 = img2

    def _convert(self, value1: int, value2: int) -> int:
        """
        入力された2つの値を変換する
        """
        clear_lsb_value1 = binary.clear_4b(value1)
        classified_value2 = binary.classify(value2)
        return binary.set_4b(clear_lsb_value1, classified_value2)

    def __call__(self, x: int, y: int) -> list[int]:
        """
        指定された座標のピクセル値を計算する
        :param x: x座標
        :param y: y座標
        :return: 計算されたピクセル値
        """
        img1_pixel_r = self.img1.bgr.get_r(x, y)
        img1_pixel_g = self.img1.bgr.get_g(x, y)
        img1_pixel_b = self.img1.bgr.get_b(x, y)

        img2_pixel_r = self.img2.bgr.get_r(x, y)
        img2_pixel_g = self.img2.bgr.get_g(x, y)
        img2_pixel_b = self.img2.bgr.get_b(x, y)

        result_pixel_r = self._convert(img1_pixel_r, img2_pixel_r)
        result_pixel_g = self._convert(img1_pixel_g, img2_pixel_g)
        result_pixel_b = self._convert(img1_pixel_b, img2_pixel_b)
        return [result_pixel_b, result_pixel_g, result_pixel_r]
