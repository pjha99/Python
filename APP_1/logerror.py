import logging
def log_exception(e):
    logging.basicConfig(level=logging.ERROR,
                        format='%(asctime)s %(levelname)s %(message)s',
                        filename='myapp.log',
                        filemode='a')
    logging.exception(e)
