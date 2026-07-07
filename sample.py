import logging
from logging import getLogger

from app import app as application


def main():
    """
    アプリケーションのメイン関数
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(filename)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s",
    )
    logger = getLogger(__name__)
    logger.info("Sample is running.")

    application.app()


if __name__ == "__main__":
    """
    エントリーポイント
    """
    main()
