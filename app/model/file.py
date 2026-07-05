import cv2


class File:
    """
    ファイルを管理するクラス
    """

    def __init__(self):
        """
        Fileクラスの初期化
        """
        self.public_movie_path = None
        self.private_movie_path = None

    def set_public_movie_path(self, path: str) -> None:
        """
        公開動画のパスを設定するメソッド
        :param path: 公開動画のパス
        """
        self.public_movie_path = path

    def set_private_movie_path(self, path: str) -> None:
        """
        秘密動画のパスを設定するメソッド
        :param path: 秘密動画のパス
        """
        self.private_movie_path = path

    def get_public_movie(self) -> cv2.VideoCapture | None:
        """
        公開動画を取得するメソッド
        :return: cv2.VideoCaptureオブジェクトまたはNone
        """
        if self.public_movie_path is None:
            return None
        return cv2.VideoCapture(self.public_movie_path)

    def get_private_movie(self) -> cv2.VideoCapture | None:
        """
        秘密動画を取得するメソッド
        :return: cv2.VideoCaptureオブジェクトまたはNone
        """
        if self.private_movie_path is None:
            return None
        return cv2.VideoCapture(self.private_movie_path)
