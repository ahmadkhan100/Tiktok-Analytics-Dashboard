# utils/helpers.py
from datetime import datetime

def log_message(message, level="INFO"):
    """
    Logs a message with a given level and timestamp.

    :param message: The message to log
    :param level: The log level (INFO, DEBUG, ERROR)
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} [{level}] - {message}")

