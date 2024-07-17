from enum import Enum
import datetime


class LogLevel(Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    FATAL = 4


def log(level: LogLevel, title: str, msg):
    print(f"{str(level)[9:]} | {str(datetime.datetime.now())[:19]} | {title}: {msg}")
