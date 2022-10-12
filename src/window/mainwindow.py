from PyQt6 import QtWidgets, uic

from resources import resourcePath

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        self._initUI()

    def _initUI(self):
        path = resourcePath("src/window/ui/mainwindow.ui") # replaced complicated path logic with resourcePath()
        uic.loadUi(path, self) # Load the .ui file
        self.setWindowTitle("PCO Timer")
        self.show() # Show the GUI

