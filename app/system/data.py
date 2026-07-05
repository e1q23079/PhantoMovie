class Data:
    """
    データクラスは、動画のフレームを格納するためのクラス
    """

    def __init__(self):
        """
        データクラスの初期化
        """
        self.frames = []

    def add_frame(self, frame):
        """
        フレームを追加するメソッド

        Args:
            frame (numpy.ndarray): 追加するフレーム
        """
        self.frames.append(frame)

    def get_frame(self, index):
        """
        指定されたインデックスのフレームを取得するメソッド

        Args:
            index (int): 取得するフレームのインデックス

        Returns:
            numpy.ndarray: 指定されたインデックスのフレーム
        """
        if 0 <= index < len(self.frames):
            return self.frames[index]
        else:
            return None  # インデックスが範囲外の場合はNoneを返す

    def clear_frames(self):
        """
        追加されたフレームをクリアするメソッド
        """
        self.frames.clear()

    def get_frames(self):
        """
        追加されたフレームを取得するメソッド

        Returns:
            list: 追加されたフレームのリスト
        """
        return self.frames
