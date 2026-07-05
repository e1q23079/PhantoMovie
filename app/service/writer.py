import cv2


class Writer:
    """
    動画を保存するためのクラス
    """

    def __init__(self, filename: str, fps: int, width: int, height: int):
        """
        動画を保存するためのクラスの初期化
        :param filename: 保存する動画のファイル名
        :param fps: 保存する動画のフレームレート
        :param width: 保存する動画の幅
        :param height: 保存する動画の高さ
        """
        self.codec = cv2.VideoWriter.fourcc(*"FFV1")  # コーデックの指定
        self.video = cv2.VideoWriter(filename, self.codec, fps, (width, height))

    def save(self, frames):
        """
        動画を保存する
        :param frames: 保存する動画のフレームを格納するリスト
        """
        for frame in frames:
            self.write(frame)
        self.release()

    def write(self, frame):
        """
        動画にフレームを書き込む
        :param frame: 書き込むフレーム
        """
        self.video.write(frame)

    def release(self):
        """
        動画の保存を終了する
        """
        self.video.release()
