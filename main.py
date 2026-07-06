import logging
from logging import getLogger

# from app import app
from app.application import Application


def main():
    """
    アプリケーションのメイン関数
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(filename)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s",
    )
    logger = getLogger(__name__)
    logger.info("Main function is running.")
    # app.app()
    app = Application()
    app.run()


if __name__ == "__main__":
    """
    エントリーポイント
    """
    main()
