# /*===================================
#     Stock Imports
# ====================================*/

import logging
import os
import sys
from PySide6.QtWidgets import QApplication

# /*===================================
#     Configure Logging
# ====================================*/

# CREATE LOG FILE
log_dir = os.path.join(os.path.dirname(sys.executable), '_internal', 'logs') if getattr(sys, 'frozen', False) else os.path.join(os.getcwd(), 'logs')
logfile = "waw-stock-map-script-placer.log"
log_path = os.path.join(log_dir, logfile)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=log_path,
    filemode='w'
)

# /*===================================
#     Initialize Config
# ====================================*/

# Needs to initialize, even if not used in this file.
import src.core.config as config

# /*===================================
#     Main
# ====================================*/

from src.core.script_placer import ScriptPlacer
from src.core.main_window import MainWindow
from src.utils.message_box import display_message_box

class Entry:

    @classmethod
    def init(cls) -> None:

        if not config.WAW_ROOT_DIR_VALID:
            display_message_box(f"Error: The WaW Root Directory '{config.WAW_ROOT_DIR}' does not exist")
            sys.exit(0)
        
        # Initialize main window
        cls.mainWindow = MainWindow()

        # Initialize script placer
        cls.scriptPlacer = ScriptPlacer(cls.mainWindow)

        # Show main window
        cls.mainWindow.show()

# /*===================================
#     Run Main
# ====================================*/

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        entry = Entry()
        entry.init()
        sys.exit(app.exec())
    except KeyboardInterrupt:
        logging.info("Application closed by user.")
    except Exception as e:
        logging.exception(f"An error occurred: {e}")

"""
# Compile all python files
py -m compileall .

# Build exe (via .spec file)
pyinstaller exe.spec --clean -y

# Run both commands (only executes second one with first one succeeds)
py -m compileall . ; pyinstaller exe.spec --clean -y

# ; is a command separator in powershell
# && is a command separator in cmd
"""

# NOTE: when issues in program, run exe via cmd-prompt to view output
# "C:\Users\Phil-\OneDrive\__Workbase__\ModOps HQ\repos\WaW-Stock-Map-Script-Placer\dist\WaW-Stock-Map-Script-Placer\WaW-Stock-Map-Script-Placer v1.1.1.exe"