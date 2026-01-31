import logging

def setup_logger(level="INFO", log_file="automator.log"):
    logging.basicConfig(
        level=getattr(logging, level),
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename=log_file,
        filemode="a"
    )
