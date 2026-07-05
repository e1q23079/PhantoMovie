import numpy as np


class BGR:
    """
    BGR形式の画像を扱うクラス
    """

    def __init__(self, img: np.ndarray):
        """
        BGR形式の画像を初期化する
        :param img: BGR形式の画像データ
        """
        self.img = img

    def get_b(self, x: int, y: int) -> int:
        """
        指定された座標のBGR形式の画像のB成分を取得する
        :param x: x座標
        :param y: y座標
        :return: B成分の値
        """
        return self.img[y, x][0]

    def get_g(self, x: int, y: int) -> int:
        """
        指定された座標のBGR形式の画像のG成分を取得する
        :param x: x座標
        :param y: y座標
        :return: G成分の値
        """
        return self.img[y, x][1]

    def get_r(self, x: int, y: int) -> int:
        """
        指定された座標のBGR形式の画像のR成分を取得する
        :param x: x座標
        :param y: y座標
        :return: R成分の値
        """
        return self.img[y, x][2]
