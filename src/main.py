from PyQt4 import QtGui
from src.mainWindow import Menu
import sys

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Menu()
    app.exec()

