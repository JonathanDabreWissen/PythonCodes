import logging

logging.basicConfig(filename="sample.log", level=logging.DEBUG)
logging.critical("Critical")
logging.error("Error")
logging.info("This is info")
logging.warning("Warning")