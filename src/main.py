import sys
from PyQt6.QtWidgets import QApplication

try:
    from window.mainwindow import MainWindow
except:
    import src
    sys.path.append(src.CURR_PATH)
    from window.mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec();
    
