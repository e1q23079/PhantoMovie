from logging import getLogger

import cv2

from .lib.diff import Diff
from .system.analyze import Analyze
from .system.convert import Convert
from .system.file import File
from .system.writer import Writer


def app():
    """
    アプリケーション
    """
    logger = getLogger(__name__)
    logger.info("Application is running.")

    # ファイルのセット
    file = File()
    file.set_public_movie_path("./assets/movie/sample.mp4")  # 公開動画
    file.set_private_movie_path("./assets/movie/sample2.mp4")  # 秘密動画

    # 動画の取得
    public_movie = file.get_public_movie()
    secret_movie = file.get_private_movie()

    # 公開動画ファイル読み込みの確認
    if public_movie is None:
        logger.error("Public movie path is not set.")
        return

    # 秘密動画ファイル読み込みの確認
    if secret_movie is None:
        logger.error("Secret movie path is not set.")
        return

    # コンバーター
    converter = Convert(
        public_movie=public_movie,
        private_movie=secret_movie,
    )

    status = converter._is_check()

    if not status:
        logger.error("Failed to open one or both videos.")
        return

    convert_data, width, height = converter.convert()

    save = Writer(filename="output.avi", fps=30, width=width, height=height)
    save.save(convert_data)

    file2 = File()
    file2.set_public_movie_path("output.avi")

    # 公開動画の取得
    public_movie2 = file2.get_public_movie()

    if public_movie2 is None:
        logger.error("Failed to get public movie.")
        return

    analyzer = Analyze(public_movie=public_movie2)
    analysis_data = analyzer.analyze()

    save2 = Writer(filename="output_diff.avi", fps=30, width=width, height=height)
    save2.save(analysis_data.get_frames())

    # テスト
    for frame in convert_data:
        # 画像の表示
        diff = Diff(frame)
        diff_result = diff.get_diff()
        cv2.imshow("Composed Image", frame)
        cv2.imshow("Diff Image", diff_result)

        fps = public_movie.get(cv2.CAP_PROP_FPS)
        key = cv2.waitKey(int(1000 / fps))
        if key == 27:  # ESC key
            break

    # while True:
    #     # 公開動画のフレームを取得
    #     ret1, public_frame = converter.public_movie.read()
    #     if not ret1:
    #         print("Failed to read frame from public video.")
    #         break

    #     # 秘密動画のフレームを取得
    #     ret2, secret_frame = secret_movie.read()
    #     if not ret2:
    #         print("Failed to read frame from secret video.")
    #         break

    #     # リサイズ
    #     public_frame = cv2.resize(public_frame, (320, 240))
    #     secret_frame = cv2.resize(secret_frame, (320, 240))

    #     # 画像の合成
    #     composition = Composition(public_frame, secret_frame)
    #     compose_result = composition.get_compose()

    #     # 画像の差分
    #     diff = Diff(compose_result)
    #     diff_result = diff.get_diff()

    # # リサイズ
    # compose_result = cv2.resize(compose_result, (320, 240))
    # diff_result = cv2.resize(diff_result, (320, 240))

    # save_composed.write(compose_result)
    # save_diff.write(diff_result)

    # print(".", end="", flush=True)

    # # 画像の表示
    # cv2.imshow("Composed Image", compose_result)
    # cv2.imshow("Diff Image", diff_result)

    # fps = public_movie.get(cv2.CAP_PROP_FPS)
    # key = cv2.waitKey(int(1000 / fps))
    # if key == 27:  # ESC key
    #     break

    # リソースの解放
    public_movie.release()
    secret_movie.release()
    # save_composed.release()
    # save_diff.release()


if __name__ == "__main__":
    """
    エントリーポイント
    """
    app()
