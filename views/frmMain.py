from PyQt5 import QtWidgets
from forms.Ui_frmMain import Ui_frmMain


class frmMain(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmMain()
        self.ui.setupUi(self)
