from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow , self).__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle('ESPORTS')
        self.initUI()
    def initUI(self):
        self.lblTitle = QtWidgets.QLabel(self) 
        self.lblTitle.setText('3-Sp0rtz')
        self.lblTitle.move(100,100)

        self.btnSubmit = QtWidgets.QPushButton(self)
        self.btnSubmit.setText('Submit')
        self.btnSubmit.move(100,10)
        self.btnSubmit.clicked.connect(self.clicked)
    def clicked(self):
        self.lblTitle.setText('544444444')
        self.update()
    def update(self):
        self.lblTitle.adjustSize() 

def start():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
start()