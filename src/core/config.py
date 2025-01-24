# /*===================================
#     Stock Imports
# ====================================*/

import json
import logging
import os
import sys

# /*===================================
#     Configure Logging
# ====================================*/

logger = logging.getLogger(__name__)

# /*===================================
#     Determine Current Working Directory
# ====================================*/

CWD = os.path.join(os.path.dirname(sys.executable), '_internal') if getattr(sys, 'frozen', False) else os.getcwd()

# /*===================================
#     Add the src directory to the Python path
# ====================================*/

sys.path.insert(0, os.path.join(CWD, 'src'))

# /*===================================
#     Load Config Info
# ====================================*/

try:
    with open(os.path.join(CWD, "json", "config.json")) as f:
        CONFIG = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f"Error loading config.json: {e}")
    raise
except KeyError as e:
    logger.error(f"Directory not found in config.json: {e}")
    raise

WAW_ROOT_DIR = CONFIG["waw_root_dir"]

WAW_ROOT_DIR_VALID = True
if not os.path.exists(WAW_ROOT_DIR):
    logger.error(f"Error: The WaW Root Directory '{WAW_ROOT_DIR}' does not exist")
    WAW_ROOT_DIR_VALID = False