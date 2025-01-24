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

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
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
from src.utils.is_executable import is_executable
from src.utils.message_box import display_message_box

ENV = 'PROD' if is_executable() else 'DEV'

class Entry:

    @classmethod
    def init(cls) -> None:
        
        # Initialize main window
        cls.mainWindow = MainWindow()

        # Display environment status
        logging.info(f'Running in {ENV} mode')

        # if running via exe, then ensure program is in the correct (waw) directory
        if is_executable():
            if not r'Call of Duty World at War' in os.getcwd():
                display_message_box("Error, Please run this program from the 'Call of Duty World at War' directory")
                sys.exit(0)

        # Initialize script placer
        cls.scriptPlacer = ScriptPlacer(cls.mainWindow, config.CWD, config.WAW_ROOT_DIR)

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
# "C:\Users\Phil-\OneDrive\__Workbase__\ModOps HQ\repos\WaW-Stock-Map-Script-Placer\dist\WaW-Stock-Map-Script-Placer\WaW-Stock-Map-Script-Placer.exe"