from PyQt4 import QtGui,QtCore,uic

class Menu(QtGui.QMainWindow):
    def __init__(self):
        super(Menu,self).__init__()
        uic.loadUi("../ui/main.ui",self)
        self.readButton.clicked.connect(self.startReading)
        self.show()


##################Reading Kanjis Functions############################
    #open the gui for reading kanjis and init it
    def startReading(self):
        uic.loadUi("../ui/read_vocab.ui",self)










