import unittest

import numpy as np

from app.lib.analyze.b4.re_formula import ReFormula
from app.lib.img import IMG


class TestReFormulaB4(unittest.TestCase):
    """
    ReFormulaB4クラスのテストクラス
    """

    def setUp(self):
        """
        テストのセットアップ
        """
        img = IMG(np.zeros((1, 1, 3), dtype=np.uint8))
        self.formula = ReFormula(img)

    def test_formula_b4_0(self):
        """
        ピクセル値が0の場合のテスト
        """
        result = self.formula._diff_pixel(0)
        self.assertEqual(result, 8)

    def test_formula_b4_1(self):
        """
        ピクセル値が16の場合のテスト
        """
        result = self.formula._diff_pixel(15)
        self.assertEqual(result, 248)
