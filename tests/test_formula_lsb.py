import unittest

import numpy as np

from app.lib.convert.lsb.formula import Formula
from app.lib.img import IMG


class TestFormulaLSB(unittest.TestCase):
    """
    FormulaLSBクラスのテストクラス
    """

    def setUp(self):
        """
        テストのセットアップ
        """
        img = IMG(np.zeros((1, 1, 3), dtype=np.uint8))
        self.formula = Formula(img, img)

    def test_formula_lsb_zero(self):
        """
        Formulaクラスのテスト（127以下の値を入力した場合、LSBは0に設定されることを確認する）
        """
        result = self.formula._convert(0, 0)
        self.assertEqual(result, 0)

        result = self.formula._convert(1, 0)
        self.assertEqual(result, 0)

        result = self.formula._convert(0, 1)
        self.assertEqual(result, 0)

        result = self.formula._convert(10, 0)
        self.assertEqual(result, 10)

        result = self.formula._convert(10, 1)
        self.assertEqual(result, 10)

    def test_formula_lsb_one(self):
        """
        Formulaクラスのテスト（128以上の値を入力した場合、LSBは1に設定されることを確認する）
        """
        result = self.formula._convert(0, 128)
        self.assertEqual(result, 1)

        result = self.formula._convert(1, 128)
        self.assertEqual(result, 1)

        result = self.formula._convert(0, 255)
        self.assertEqual(result, 1)

        result = self.formula._convert(10, 128)
        self.assertEqual(result, 11)

        result = self.formula._convert(10, 255)
        self.assertEqual(result, 11)
