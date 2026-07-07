from logging import getLogger

from .model.file import File
from .service.analyze import Analyze
from .service.convert import Convert
from .service.writer import Writer


def app():
    """
    アプリケーション
    """
    logger = getLogger(__name__)
    logger.info("Application is running.")

    # ファイルのセット
    file = File()

    # public_movie_path = input(
    #     "「公開動画」のファイル名を入力してください（例: sample.mp4）: "
    # )
    # if public_movie_path == "":
    #     logger.error("Public movie path is not set.")
    #     return

    # secret_movie_path = input(
    #     "「秘密動画」のファイル名を入力してください（例: sample2.mp4）: "
    # )
    # if secret_movie_path == "":
    #     logger.error("Secret movie path is not set.")
    #     return

    # file.set_public_movie_path(f"./assets/movie/{public_movie_path}")  # 公開動画
    # file.set_private_movie_path(f"./assets/movie/{secret_movie_path}")  # 秘密動画

    file.set_public_movie_path("./assets/movie/public_movie.mp4")  # 公開動画
    file.set_private_movie_path("./assets/movie/secret_movie.mp4")  # 秘密動画

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

    logger.info("Starting video conversion...")

    convert_data, width, height, fps = converter.convert()

    # output_filename = input(
    #     "変換後の動画のファイル名を入力してください（例: output.avi）: "
    # )

    # if output_filename == "":
    #     logger.error("Output filename is not set.")
    #     return

    # save = Writer(
    #     filename=f"./assets/movie/{output_filename}",
    #     fps=fps,
    #     width=width,
    #     height=height,
    # )
    # save.save(convert_data)

    writer = Writer(
        filename="./assets/movie/output.avi",
        fps=fps,
        width=width,
        height=height,
    )
    writer.save(convert_data)

    logger.info("Video conversion completed.")

    file2 = File()
    file2.set_public_movie_path("./assets/movie/output.avi")  # 公開動画

    # 公開動画の取得
    public_movie2 = file2.get_public_movie()

    if public_movie2 is None:
        logger.error("Failed to get public movie.")
        return

    analyzer = Analyze(public_movie=public_movie2)

    logger.info("Starting video analysis...")

    analysis_data = analyzer.analyze()

    # result_filename = input(
    #     "出力動画のファイル名を入力してください（例: output_diff）: "
    # )

    # if result_filename == "":
    #     logger.error("Result filename is not set.")
    #     return

    # save2 = Writer(
    #     filename=f"./assets/movie/{result_filename}.avi",
    #     fps=fps,
    #     width=width,
    #     height=height,
    # )
    # save2.save(analysis_data.get_frames())

    writer = Writer(
        filename="./assets/movie/result.avi",
        fps=fps,
        width=width,
        height=height,
    )

    writer.save(analysis_data.get_frames())

    logger.info("Analysis completed.")

    # リソースの解放
    public_movie.release()
    secret_movie.release()


if __name__ == "__main__":
    """
    エントリーポイント
    """
    app()
