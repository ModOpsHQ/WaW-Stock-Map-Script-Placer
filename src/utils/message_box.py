# /*===================================
#     Stock Imports
# ====================================*/

from PySide6.QtWidgets import QMessageBox

# /*===================================
#     Main
# ====================================*/

def display_message_box(message, _type=QMessageBox.Information):
    msgBox = QMessageBox()
    msgBox.setText(message)
    msgBox.setIcon(_type)
    msgBox.exec()