def _to_binary_str(value: int) -> str:
    """
    10進数値を2進数の文字列に変換する

    Args:
        value (int): 10進数の値

    Returns:
        str: 2進数の文字列
    """
    binary = f"{value:08b}"
    return binary


def get_4b(value: int) -> int:
    """
    10進数の値から最下位4ビットを取得する

    Args:
        value (int): LSBを抽出する値

    Returns:
        int: 最下位4ビット
    """
    lsb = int(_to_binary_str(value)[-4:], 2)
    return lsb


def clear_4b(value: int) -> int:
    """
    10進数の値の最下位4ビットをクリアする

    Args:
        value (int): LSBをクリアする値

    Returns:
        int: 最下位4ビットがクリアされた新しい値
    """
    binary = _to_binary_str(value)
    result = int(binary[:-4] + "0000", 2)
    return result


def set_4b(value: int, b4: int) -> int:
    """
    10進数の値の最下位4ビットを指定された値に設定する

    Args:
        value (int): LSBを設定する値
        b4 (int): 設定する最下位4ビットの値（0または1）

    Returns:
        int: 最下位4ビットが設定された新しい値
    """
    binary = _to_binary_str(value)
    result = int(binary[:-4] + f"{b4:04b}", 2)
    return result


def classify(value: int) -> int:
    """
    入力された値を分類する
    """
    wide = int(255 / 8)
    if value < wide:
        return 0
    elif value < wide * 2:
        return 1
    elif value < wide * 3:
        return 2
    elif value < wide * 4:
        return 3
    elif value < wide * 5:
        return 4
    elif value < wide * 6:
        return 5
    elif value < wide * 7:
        return 6
    elif value < wide * 8:
        return 7
    return 8


def revert_classify(value: int) -> int:
    """
    入力された値を分類する
    """
    wide = int(255 / 8)
    if value == 0:
        return 0
    elif value == 1:
        return wide * 1
    elif value == 2:
        return wide * 2
    elif value == 3:
        return wide * 3
    elif value == 4:
        return wide * 4
    elif value == 5:
        return wide * 5
    elif value == 6:
        return wide * 6
    elif value == 7:
        return wide * 7
    elif value == 8:
        return 255
    return 255
