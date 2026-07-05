import logging
from logging import getLogger

from app import app


def main():
    """
    アプリケーションのメイン関数
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(filename)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s",
    )
    logger = getLogger(__name__)
    logger.debug("Main function is running.")
    app.app()


if __name__ == "__main__":
    """
    エントリーポイント
    """
    main()
