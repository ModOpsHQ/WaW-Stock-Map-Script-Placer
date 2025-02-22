# /*===================================
#     Stock Imports
# ====================================*/

from PySide6.QtWidgets import QMainWindow

# /*===================================
#     Main
# ====================================*/

from src.resources.ui.ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)