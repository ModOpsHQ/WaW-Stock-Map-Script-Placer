# /*===================================
#     Stock Imports
# ====================================*/

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

# /*===================================
#     Main
# ====================================*/

from src.resources.UI.ui_console import Ui_ConsoleWidget

class Console(QWidget):

    def __init__(self):
        super().__init__()

        # remove default window frame / titlebar
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.ui = Ui_ConsoleWidget()
        self.ui.setupUi(self)
        