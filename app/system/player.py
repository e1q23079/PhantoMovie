import numpy


class Player:
    """
    動画を再生するためのクラス
    """

    def __init__(self, frames: list):
        """
        動画を再生するためのクラスの初期化

        :param frames: 動画のフレームを格納するリスト"""
        self.is_playing = False
        self.current_frame_index = 0
        self.frames = frames  # This will hold the frames of the movie

    def reset_current_frame_index(self):
        """
        現在のフレームインデックスをリセットする
        """
        self.current_frame_index = 0

    def get_frame(self) -> tuple[bool, numpy.ndarray | None]:
        """
        現在のフレームを取得する
        :param frames: 動画のフレームを格納するリスト
        """
        if self.current_frame_index < len(self.frames):
            frame = self.frames[self.current_frame_index]
            self.current_frame_index += 1
            return True, frame
        else:
            return False, None

    def get_is_playing(self) -> bool:
        """
        動画が再生中かどうかを返す
        """
        return self.is_playing

    def play_movie(self):
        """
        動画を再生する
        """
        # Logic to play the movie
        self.is_playing = True
        print("Playing movie...")

    def stop_movie(self):
        """
        動画を停止する
        """
        self.is_playing = False
        # Logic to stop the movie
        print("Stopping movie...")

    def backward_movie(self):
        """
        動画を巻き戻す
        """
        # Logic to backward the movie
        print("Rewinding movie...")
        self.current_frame_index = max(0, self.current_frame_index - 1)

    def forward_movie(self):
        """
        動画を早送りする
        """
        # Logic to forward the movie
        print("Forwarding movie...")
        self.current_frame_index = min(
            len(self.frames) - 1, self.current_frame_index + 1
        )
