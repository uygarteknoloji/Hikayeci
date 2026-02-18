from PyQt5 import QtWidgets
from forms.Ui_frmMain import Ui_MainWindow


class frmMain(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
