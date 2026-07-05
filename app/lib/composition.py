import cv2
import numpy as np

from ..lib.formula import Formula
from ..lib.img import IMG


class Composition:
    def __init__(self, img1: np.ndarray, img2: np.ndarray):
        """
        画像を合成するクラス
        :param img1: 1枚目の画像データ
        :param img2: 2枚目の画像データ
        :param formula: 画像処理の式
        """
        self.img1 = IMG(img1)
        self.height = self.img1.height
        self.width = self.img1.width
        self.current_frame = 0
        self.total_frames = 0
        temp_img2 = cv2.resize(img2, (self.img1.width, self.img1.height))
        self.img2 = IMG(temp_img2)
        self.formula = Formula(self.img1, self.img2)

    def get_pixels_num(self):
        """
        画像のピクセル数を取得する
        :return: 画像のピクセル数
        """
        return self.width * self.height

    def progress(self, current_frame, total_frames):
        """
        進捗状況を計算する
        :param current_frame: 現在のフレーム数
        :param total_frames: 総フレーム数
        :return: 進捗状況（0〜100）
        """
        if total_frames == 0:
            return 0
        return (current_frame / total_frames) * 100

    def get_compose(self):
        """
        画像を合成する
        :return: 合成された画像
        """
        height = self.img1.height
        width = self.img1.width
        result = np.full((height, width, 3), 255, dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                pixel = self.formula(x, y)
                result[y, x] = pixel
        return result

    def get_width(self):
        """
        画像の幅を取得する
        :return: 画像の幅
        """
        return self.width

    def get_height(self):
        """
        画像の高さを取得する
        :return: 画像の高さ
        """
        return self.height
