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


def get_lsb(value: int) -> int:
    """
    10進数の値から最下位ビットを取得する

    Args:
        value (int): LSBを抽出する値

    Returns:
        int: 最下位ビット
    """
    lsb = int(_to_binary_str(value)[-1])
    return lsb


def clear_lsb(value: int) -> int:
    """
    10進数の値の最下位ビットをクリアする

    Args:
        value (int): LSBをクリアする値

    Returns:
        int: 最下位ビットがクリアされた新しい値
    """
    binary = _to_binary_str(value)
    result = int(binary[:-1] + "0", 2)
    return result


def set_lsb(value: int, lsb: int) -> int:
    """
    10進数の値の最下位ビットを指定された値に設定する

    Args:
        value (int): LSBを設定する値
        lsb (int): 設定する最下位ビットの値（0または1）

    Returns:
        int: 最下位ビットが設定された新しい値
    """
    binary = _to_binary_str(value)
    result = int(binary[:-1] + str(lsb), 2)
    return result
