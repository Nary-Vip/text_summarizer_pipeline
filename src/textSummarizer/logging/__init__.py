import os
import sys
import logging

logging_str = '[%(asctime)s - %(levelname)s - %(module)s - %(message)s]'
log_dir = "logs"
log_file_path = os.path.join(log_dir, "logs.log")

os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
    level=logging.INFO, 
    format=logging_str,
    handlers=[
        # Logs to the file
        logging.FileHandler(log_file_path),

        # Logs to the console
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizer")