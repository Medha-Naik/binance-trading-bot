import logging
import os

def setup_logger(name:str)->logging.Logger:
    os.makedirs("logs",exist_ok=True)

    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)


    fh=logging.FileHandler("logs/trading_bot.log")
    fh.setLevel(logging.DEBUG)

    ch=logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter=logging.Formatter(
        "%(asctime)s|%(levelname)-8s|%(name)s|%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(ch)
    
    return logger