from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QComboBox, QLineEdit
import sys
from PyQt5.QtGui import QFont

from HelperVariables import MyVars


class DbWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,400)
        self.setWindowTitle("Data Base Scanner")
        self.setStyleSheet('background : pink')
        self.createui()
    def createui(self):

        self.txtBx = QLineEdit(self)
        self.txtBx.resize(200,30)
        self.txtBx.move(10,5)

        self.dbutton("Save",10,30,clickbutton=self.SelectedDb)




    def dbutton(self,name,x,y,clickbutton=None):
        btn=QPushButton(self)
        btn.resize(100,30)
        btn.setFont(QFont('times new roman : ',15))
        btn.setText(name)
        btn.move(x,y)
        btn.setStyleSheet('background : white')
        if clickbutton is not None:
            btn.clicked.connect(clickbutton)

    def SelectedDb(self):
        if self.txtBx.text():
            MyVars.DbPath = self.txtBx.text()
            self.close()
        else:
            print("Please enter the DB path")







#
# if __name__ == "__main__":
#
#     App=QApplication(sys.argv)
#     Myapp=DbWindow()
#     sys.exit(App.exec_())