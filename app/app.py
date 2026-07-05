import cv2

from .lib.composition import Composition
from .lib.diff import Diff


def app():
    """
    アプリケーション
    """
    print("Application is running.")

    # 公開画像
    public_img = cv2.imread("./assets/img/sample.jpg")
    if public_img is None:
        print("Failed to load image.")
        return

    # 秘密画像
    secret_key = cv2.imread("./assets/img/sample2.jpg")
    if secret_key is None:
        print("Failed to load image.")
        return

    # 画像の合成
    composition = Composition(public_img, secret_key)
    compose_result = composition.get_compose()

    # 画像の差分
    diff = Diff(compose_result)
    diff_result = diff.get_diff()

    # リサイズ
    compose_result = cv2.resize(compose_result, (640, 480))
    diff_result = cv2.resize(diff_result, (640, 480))

    # 画像の表示
    cv2.imshow("Composed Image", compose_result)
    cv2.imshow("Diff Image", diff_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    """
    エントリーポイント
    """
    app()
