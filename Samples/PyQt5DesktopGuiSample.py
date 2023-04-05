from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    # constructor
    def __init__(self):
        # access properties / methods parent class
        super(QMainWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("My Python Window Title")
        self.InitGui()
    
    def InitGui(self):
         self.label = QtWidgets.QLabel(self)
         self.label.setText("here label text")
         self.label.move(50,50)

         self.button1 = QtWidgets.QPushButton(self)
         self.button1.setText("Click me")
         self.button1.clicked.connect(self.Button1Clicked)

    def Button1Clicked(self):
        self.label.setText("I am clicked this is new label")
        self.UpdateGui()

    def UpdateGui(self):
        self.label.adjustSize()

def Window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

Window()