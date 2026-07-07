import unittest

import numpy as np

from app.lib.convert.b4.formula import Formula
from app.lib.img import IMG


class TestFormulaB4(unittest.TestCase):
    """
    FormulaB4クラスのテストクラス
    """

    def setUp(self):
        """
        テストのセットアップ
        """
        img = IMG(np.zeros((1, 1, 3), dtype=np.uint8))
        self.formula = Formula(img, img)

    def test_formula_b4_clear(self):
        """
        Formulaクラスのテスト（4ビット目をクリアすることを確認する）
        """
        result = self.formula._convert(0b00000000, 0)
        self.assertEqual(result, 0b00000000)

        result = self.formula._convert(0b00000001, 0)
        self.assertEqual(result, 0b00000000)

    def test_formula_b4_set(self):
        """
        Formulaクラスのテスト（4ビット目を設定することを確認する）
        """
        result = self.formula._convert(0b00000000, 0)
        self.assertEqual(result, 0)

        result = self.formula._convert(0b00000000, 16)
        self.assertEqual(result, 1)
