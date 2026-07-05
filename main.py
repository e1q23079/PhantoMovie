import logging
from logging import getLogger

from app.application import Application


def main():
    """
    アプリケーションのメイン関数
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logger = getLogger(__name__)
    print("Starting the application...")
    logger.info("Main function is running.")
    app = Application()
    app.run()


if __name__ == "__main__":
    """
    エントリーポイント
    """
    main()
