from PyQt4 import QtGui,QtCore,uic

class Menu(QtGui.QMainWindow):
    def __init__(self):
        super(Menu,self).__init__()
        uic.loadUi("../ui/main.ui",self)
        self.readButton.clicked.connect(self.readkanji)
        self.show()







