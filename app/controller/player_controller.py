import tkinter as tk
from logging import getLogger
from typing import TYPE_CHECKING

import cv2
from PIL import Image, ImageTk

if TYPE_CHECKING:
    from ..service.player import Player
    from ..ui.main_window import MainWindow

logger = getLogger(__name__)


class PlayerController:
    """
    PlayerControllerクラスは、動画再生の制御を行うクラス
    """

    def __init__(self, main_window: "MainWindow", player: "Player"):
        """
        PlayerControllerクラスの初期化
        """
        self.main_window = main_window
        self.player = player

    def render_frame(self, img_bgr):
        """
        フレームを描画する
        :param img_bgr: BGR形式の画像
        """
        img_bgr = cv2.resize(img_bgr, (427, 240))
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        self.img_tk = ImageTk.PhotoImage(img_pil)

        if img_pil is not None:
            self.main_window.video_frame.canvas.create_image(
                0, 0, anchor=tk.NW, image=self.img_tk
            )
        self.main_window.video_frame.canvas.grid(row=0, column=0, columnspan=3, pady=1)

    def next_frame(self):
        """
        次のフレームを表示する
        """
        logger.debug("Displaying next frame...")
        if self.player is None:
            logger.error("Movie is not loaded.")
            return
        if self.player.get_is_playing() is False:
            logger.debug("Movie is not playing.")
            return
        ret, img_bgr = self.player.get_frame()
        if not ret:
            self.player.reset_current_frame_index()
            self.player.stop_movie()
            logger.error("Error reading frame")
            return
        if img_bgr is None:
            logger.debug("No more frames to display.")
            return

        self.render_frame(img_bgr)

        self.main_window.after(33, self.next_frame)

    def play_stop_btn(self):
        """
        再生/停止ボタンがクリックされたときの処理
        """
        logger.debug("Play/Stop button clicked...")
        if self.player is None:
            logger.error("Movie is not loaded.")
            return
        if self.player.get_is_playing():
            self.stop_movie()
        else:
            self.play_movie()

    def stop_movie(self):
        """
        動画を停止する
        """
        logger.debug("Stopping movie...")
        if self.player is None:
            logger.error("Movie is not loaded.")
            return
        self.player.stop_movie()

    def play_movie(self):
        """
        動画を再生する
        """
        logger.debug("Playing movie...")
        if self.player is None:
            logger.error("Movie is not loaded.")
            return
        self.player.play_movie()
        self.main_window.after(33, self.next_frame)

    def play_forward_movie(self):
        """
        動画を早送りする
        """
        logger.debug("Forwarding movie...")
        if self.player is None:
            logger.error("Movie is not loaded.")
            return
        self.player.forward_movie()
        frame = self.player.get_current_frame()
        if frame is None:
            logger.debug("No more frames to display.")
            return
        self.render_frame(frame)

    def play_backward_movie(self):
        """
        動画を巻き戻す
        """
        logger.debug("Rewinding movie...")
        if self.player is None:
            logger.error("Movie is not loaded.")
            return
        self.player.backward_movie()
        frame = self.player.get_current_frame()
        if frame is None:
            logger.debug("No more frames to display.")
            return
        self.render_frame(frame)
