import cv2

from .lib.composition import Composition
from .lib.diff import Diff
from .lib.save import Save


def app():
    """
    アプリケーション
    """
    print("Application is running.")

    # 公開動画
    public_movie = cv2.VideoCapture("./assets/movie/sample.mp4")
    if public_movie.isOpened() is None:
        print("Failed to load video.")
        return

    # 秘密動画
    secret_movie = cv2.VideoCapture("./assets/movie/sample2.mp4")
    if secret_movie.isOpened() is None:
        print("Failed to load video.")
        return

    save_composed = Save(
        "output_composed.mp4",
        fps=30,
        width=320,
        height=240,
    )

    save_diff = Save(
        "output_diff.mp4",
        fps=30,
        width=320,
        height=240,
    )

    while True:
        # 公開動画のフレームを取得
        ret1, public_frame = public_movie.read()
        if not ret1:
            print("Failed to read frame from public video.")
            break

        # 秘密動画のフレームを取得
        ret2, secret_frame = secret_movie.read()
        if not ret2:
            print("Failed to read frame from secret video.")
            break

        # リサイズ
        public_frame = cv2.resize(public_frame, (320, 240))
        secret_frame = cv2.resize(secret_frame, (320, 240))

        # 画像の合成
        composition = Composition(public_frame, secret_frame)
        compose_result = composition.get_compose()

        # 画像の差分
        diff = Diff(compose_result)
        diff_result = diff.get_diff()

        # # リサイズ
        # compose_result = cv2.resize(compose_result, (320, 240))
        # diff_result = cv2.resize(diff_result, (320, 240))

        save_composed.write(compose_result)
        save_diff.write(diff_result)

        print(".", end="", flush=True)

        # 画像の表示
        cv2.imshow("Composed Image", compose_result)
        cv2.imshow("Diff Image", diff_result)

        fps = public_movie.get(cv2.CAP_PROP_FPS)
        key = cv2.waitKey(int(1000 / fps))
        if key == 27:  # ESC key
            break

    # リソースの解放
    public_movie.release()
    secret_movie.release()
    save_composed.release()
    save_diff.release()


if __name__ == "__main__":
    """
    エントリーポイント
    """
    app()
