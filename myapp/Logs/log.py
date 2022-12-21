# 紀錄系統訊息等等
import logging
import logging.config

# logging.config.dictConfig(config=LOGGING)
# logger=logging.getLogger('default')

# def getLog(path):
#     return logger

class getLog:
    def __init__(self, path):
        self.path = path

        self.LOGGING = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'normal': {  # the name of formatter
                    'format': '%(asctime)s [%(module)s] %(levelname)s %(message)s'
                },
                'simple': {  # the name of formatter
                    'format': '%(levelname)s - %(message)s'
                },
            },
            'handlers': {
                'time-rotating-file': {  # the name of handler
                    'filename': f'{path}\\Logs\\project.log',
                    'formatter': 'normal',  # use the above "simple" formatter
                    # the log rotation by time interval
                    'class': 'logging.handlers.TimedRotatingFileHandler',
                    # the path of the log file
                    'when': 'midnight',  # time interval
                    'backupCount': 3,
                    'encoding': 'utf-8',
                },
            },
            'loggers': {
                'default': {  # the name of logger
                    # use the above "time-rotating-file" handler
                    'handlers': ['time-rotating-file'],
                    'level': 'INFO',  # logging level
                    'propagate': True,
                },
            },
        }

        logging.config.dictConfig(config=self.LOGGING)
        self.logger=logging.getLogger('default')

    def returnLog(self):
        return self.logger


