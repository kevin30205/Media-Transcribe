import os
import datetime
import inspect
from loguru import logger


class Logger(object):
    """
    Create a logger for saving process.
    """

    def __init__(self, configs, level='DEBUG'):

        self.level = level

        exp_root_dir = configs.exp_setting.exp_dir
        logger_path = os.path.join(exp_root_dir, "logger", f"logger.log")

        if os.path.exists(logger_path):
            user_input = input(
                f'The logger file "{logger_path}" has already existed. \n'
                'Please choose an option and enter the number of your choice:\n'
                '1. Overwrite the existing logger file.\n'
                '2. Create a new logger file, appending the current date to the filename.\n'
                '3. Exit the process.\n'
            )

            if user_input == "1":
                logger.info(f"Overwriting the existing logger file {logger_path}.")
                os.system(f"rm {logger_path}")

            elif user_input == "2":
                date_str = datetime.datetime.now().strftime("%Y%m%d")
                new_logger_path = os.path.join(configs.exp_setting.exp_dir, "logger", f"logger_{date_str}.log")
                logger.info(f"Creating a new logger file {new_logger_path}.")
                logger_path = new_logger_path

            elif user_input == "3":
                logger.info("Exit from the training process.")
                exit(0)
                
            else:
                logger.info("Invalid option. Exit from the training process.")
                exit(0)

        # create a logger
        logger.add(logger_path, level=self.level, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {file}:{function}:{line} | {message}")

    def log_message(self, level, message):

        frame = inspect.currentframe().f_back.f_back

        relative_path = os.path.relpath(frame.f_code.co_filename)

        location = f"{relative_path}:{frame.f_code.co_name}:{frame.f_lineno} | "

        message = location + message

        getattr(logger, level)(message)

    def info(self, message):
        self.log_message("info", message)

    def trace(self, message):
        self.log_message("trace", message)
