import unittest

from app.lib import lsb


class TestLSB(unittest.TestCase):
    """
    lsbモジュールのテストクラス
    """

    def setUp(self):
        """
        テストのセットアップを行う
        """
        pass

    def test_to_binary_str(self):
        """
        _to_binary_strメソッドのテスト
        """
        self.assertEqual(lsb._to_binary_str(0), "00000000")
        self.assertEqual(lsb._to_binary_str(1), "00000001")
        self.assertEqual(lsb._to_binary_str(5), "00000101")
        self.assertEqual(lsb._to_binary_str(255), "11111111")

    def test_get_lsb(self):
        """
        get_lsbメソッドのテスト
        """
        self.assertEqual(lsb.get_lsb(0), 0)
        self.assertEqual(lsb.get_lsb(1), 1)
        self.assertEqual(lsb.get_lsb(5), 1)
        self.assertEqual(lsb.get_lsb(4), 0)
        self.assertEqual(lsb.get_lsb(255), 1)

    def test_clear_lsb(self):
        """
        clear_lsbメソッドのテスト
        """
        self.assertEqual(lsb.clear_lsb(0), 0)
        self.assertEqual(lsb.clear_lsb(1), 0)
        self.assertEqual(lsb.clear_lsb(5), 4)
        self.assertEqual(lsb.clear_lsb(4), 4)
        self.assertEqual(lsb.clear_lsb(255), 254)

    def test_set_lsb(self):
        """
        set_lsbメソッドのテスト
        """
        self.assertEqual(lsb.set_lsb(0, 0), 0)
        self.assertEqual(lsb.set_lsb(0, 1), 1)
        self.assertEqual(lsb.set_lsb(5, 0), 4)
        self.assertEqual(lsb.set_lsb(4, 1), 5)
        self.assertEqual(lsb.set_lsb(255, 0), 254)
