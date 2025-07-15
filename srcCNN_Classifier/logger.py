import logging 
import os 
from datetime import datetime

# Generate log file name
LOG_FILE = f"{datetime.now().strftime('%m%d%Y_%H%M%S')}.log"

# Define logs directory and ensure it exists
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Set up logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger('CNNClassifierLogger')
