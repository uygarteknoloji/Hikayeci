from PyQt5 import QtWidgets
from forms.frmMainUi import Ui_MainWindow

class frmMain(QtWidgets.QWidget):
    def __init__(self):
        super(frmMain, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()