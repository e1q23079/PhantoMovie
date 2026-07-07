import unittest

import numpy as np

from app.lib.analyze.lsb.re_formula import ReFormula
from app.lib.img import IMG


class TestReFormulaLSB(unittest.TestCase):
    """
    ReFormulaLSBクラスのテストクラス
    """

    def setUp(self):
        """
        テストのセットアップ
        """
        img = IMG(np.zeros((1, 1, 3), dtype=np.uint8))
        self.formula = ReFormula(img)

    def test_formula_lsb_1(self):
        """
        LSBが1の場合のテスト
        """
        result = self.formula._diff_pixel(1)
        self.assertEqual(result, 255)

    def test_formula_lsb_0(self):
        """
        LSBが0の場合のテスト
        """
        result = self.formula._diff_pixel(0)
        self.assertEqual(result, 0)
