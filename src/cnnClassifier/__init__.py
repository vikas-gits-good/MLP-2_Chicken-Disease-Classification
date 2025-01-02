import os
import sys
import logging

log_frmt = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_path = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=log_frmt,
    handlers=[logging.FileHandler(log_path), logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger("cnnClassifierLogger")
