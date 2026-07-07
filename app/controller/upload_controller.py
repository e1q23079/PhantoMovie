from tkinter import filedialog
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..model.file import File


class UploadController:
    """
    UploadControllerクラスは、動画アップロードの制御を行うクラス
    """

    def __init__(self, file: "File"):
        """
        UploadControllerクラスの初期化
        """
        self.file = file

    def select_public_movie(self):
        """
        公開動画を選択するメソッド
        """
        filename = filedialog.askopenfilename(
            title="「公開動画」を開く",
            filetypes=(("Video files", "*.mp4 *.avi"), ("All files", "*.*")),
        )
        self.file.set_public_movie_path(filename)

    def select_private_movie(self):
        """
        秘密動画を選択するメソッド
        """
        filename = filedialog.askopenfilename(
            title="「秘密動画」を開く",
            filetypes=(("Video files", "*.mp4 *.avi"), ("All files", "*.*")),
        )
        self.file.set_private_movie_path(filename)
