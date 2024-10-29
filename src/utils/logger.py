import logging

def setup_logger(name, log_file, level=logging.INFO):
    """Function to setup a logger"""
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Example usage:
# logger = setup_logger('main_logger', 'main.log')
# logger.info('This is an info message')