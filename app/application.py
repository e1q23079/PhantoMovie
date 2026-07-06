from logging import getLogger

from app.controller.app_controller import AppController
from app.ui.main_window import MainWindow

logger = getLogger(__name__)


class Application:
    def __init__(self):
        """
        Applicationクラスの初期化
        """
        logger.info("Application is running.")
        self.main_window = MainWindow()
        self.app_controller = AppController(self.main_window)

    def run(self):
        """
        アプリケーションを実行する
        """
        self.main_window.run()


if __name__ == "__main__":
    app = Application()
    app.run()
