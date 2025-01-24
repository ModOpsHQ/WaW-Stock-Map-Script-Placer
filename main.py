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
#     Main
# ====================================*/

from src.core.script_placer import ScriptPlacer
from src.core.main_window import MainWindow
from src.utils.is_executable import is_executable
from src.utils.message_box import display_message_box

ENV = 'PROD' if is_executable() else 'DEV'

currentWorkingDir = os.getcwd()

# Dynamically determine where the ModOps HQ folder should be created.
if is_executable():
    # if not exe, then the template files are in cwd (vscode proj dir), and obv the dest for said files is still waw dir.
    # so place the Stock Base Files folder in your working dir, run program, try to create a mod, it will inform you of missing dir, but it will create a ModOps HQ dir in the working dir, so then navigate to Stock-Map Script-Placer and place the Stock Base Files folder in there. now you can create a mod.
    wawRootDir = currentWorkingDir
else:
    # when pkg'd into an exe, run exe, it prompts u of dir, it creates modops hq dir, you place folder, done. same as above reli, we just switch between where the modops hq dir is created. this is for automatic dev/prod env changes ofc.
    # set YOUR waw root directory here
    wawRootDir = r'D:\SteamLibrary\steamapps\common\Call of Duty World at War'

class Entry:

    @classmethod
    def init(cls) -> None:
        
        # Initialize main window
        cls.mainWindow = MainWindow()

        # Display environment status
        logging.info(f'Running in {ENV} mode')

        # if running via exe, then ensure program is in the correct (waw) directory
        if is_executable():
            if not r'SteamLibrary\steamapps\common\Call of Duty World at War' in os.getcwd():
                display_message_box("Error, Please run this program from the Call of Duty: World at War steam directory")
                sys.exit(0)

        # Initialize script placer
        cls.scriptPlacer = ScriptPlacer(cls.mainWindow, currentWorkingDir, wawRootDir)

        # Show main window
        cls.mainWindow.show()

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
