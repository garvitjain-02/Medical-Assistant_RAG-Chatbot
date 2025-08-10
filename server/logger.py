import logging

def setup_logger(name="MedicalAssistant"):
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ch=logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter=logging.Formatter("[%(asctime)s] - [%(levelname)s] --- [%(message)s]")
    ch.setFormatter(formatter)
    
    if not logger.hasHandlers():
        logger.addHandler(ch)

    return logger



logger = setup_logger()
logger.info("Logger setup complete for Medical Assistant RAG Chatbot.")
logger.debug("Debugging information can be added here.")
logger.error("Error messages will be logged here.")
logger.critical("Critical issues will be logged here.")