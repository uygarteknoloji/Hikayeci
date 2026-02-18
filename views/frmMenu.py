from PyQt5 import QtWidgets
from forms.Ui_frmMenu import Ui_frmMenu


class frmMenu(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmMenu()
        self.ui.setupUi(self)