import logging
import colorlog


SUCCESS = 1
logging.addLevelName(SUCCESS, 'SUCCESS')
formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(levelname) s: %(message)s',
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'yellow',
        'WARNING': 'orange',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
        'SUCCESS': 'bold_green'
    },
    secondary_log_colors={
        'message': {
            'ERROR': 'red',
            'CRITICAL': 'red'
        }},
    style='%'
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger('example')
logger.addHandler(handler)
logger.setLevel('SUCCESS')
