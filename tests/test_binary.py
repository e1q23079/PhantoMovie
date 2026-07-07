import unittest

from app.lib import binary


class TestBinary(unittest.TestCase):
    """
    binaryモジュールのテストクラス
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
        self.assertEqual(binary._to_binary_str(0), "00000000")
        self.assertEqual(binary._to_binary_str(1), "00000001")
        self.assertEqual(binary._to_binary_str(5), "00000101")
        self.assertEqual(binary._to_binary_str(255), "11111111")

    def test_get_4b(self):
        """
        get_4bメソッドのテスト
        """
        self.assertEqual(binary.get_4b(0), 0)
        self.assertEqual(binary.get_4b(1), 1)
        self.assertEqual(binary.get_4b(5), 5)
        self.assertEqual(binary.get_4b(255), 15)

    def test_clear_4b(self):
        """
        clear_4bメソッドのテスト
        """
        self.assertEqual(binary.clear_4b(0), 0)
        self.assertEqual(binary.clear_4b(1), 0)
        self.assertEqual(binary.clear_4b(5), 0)
        self.assertEqual(binary.clear_4b(255), 240)

    def test_set_4b(self):
        """
        set_4bメソッドのテスト
        """
        self.assertEqual(binary.set_4b(0, 0), 0)
        self.assertEqual(binary.set_4b(0, 1), 1)
        self.assertEqual(binary.set_4b(5, 0), 0)
        self.assertEqual(binary.set_4b(240, 15), 255)

    def test_classify(self):
        """
        classifyメソッドのテスト
        """
        self.assertEqual(binary.classify(0), 0)
        self.assertEqual(binary.classify(15), 0)
        self.assertEqual(binary.classify(16), 1)
        self.assertEqual(binary.classify(31), 1)
        self.assertEqual(binary.classify(32), 2)
        self.assertEqual(binary.classify(47), 2)
        self.assertEqual(binary.classify(48), 3)
        self.assertEqual(binary.classify(63), 3)
        self.assertEqual(binary.classify(64), 4)
        self.assertEqual(binary.classify(79), 4)
        self.assertEqual(binary.classify(80), 5)
        self.assertEqual(binary.classify(95), 5)
        self.assertEqual(binary.classify(96), 6)
        self.assertEqual(binary.classify(111), 6)
        self.assertEqual(binary.classify(112), 7)
        self.assertEqual(binary.classify(127), 7)
        self.assertEqual(binary.classify(128), 8)
        self.assertEqual(binary.classify(143), 8)
        self.assertEqual(binary.classify(144), 9)
        self.assertEqual(binary.classify(159), 9)
        self.assertEqual(binary.classify(160), 10)
        self.assertEqual(binary.classify(175), 10)
        self.assertEqual(binary.classify(176), 11)
        self.assertEqual(binary.classify(191), 11)
        self.assertEqual(binary.classify(192), 12)
        self.assertEqual(binary.classify(207), 12)
        self.assertEqual(binary.classify(208), 13)
        self.assertEqual(binary.classify(223), 13)
        self.assertEqual(binary.classify(224), 14)
        self.assertEqual(binary.classify(239), 14)
        self.assertEqual(binary.classify(240), 15)
        self.assertEqual(binary.classify(255), 15)

    def test_revert_classify(self):
        """
        classifyメソッドの逆変換のテスト
        """
        self.assertEqual(binary.revert_classify(0), 8)
        self.assertEqual(binary.revert_classify(1), 24)
        self.assertEqual(binary.revert_classify(2), 40)
        self.assertEqual(binary.revert_classify(3), 56)
        self.assertEqual(binary.revert_classify(4), 72)
        self.assertEqual(binary.revert_classify(5), 88)
        self.assertEqual(binary.revert_classify(6), 104)
        self.assertEqual(binary.revert_classify(7), 120)
        self.assertEqual(binary.revert_classify(8), 136)
        self.assertEqual(binary.revert_classify(9), 152)
        self.assertEqual(binary.revert_classify(10), 168)
        self.assertEqual(binary.revert_classify(11), 184)
        self.assertEqual(binary.revert_classify(12), 200)
        self.assertEqual(binary.revert_classify(13), 216)
        self.assertEqual(binary.revert_classify(14), 232)
        self.assertEqual(binary.revert_classify(15), 248)
