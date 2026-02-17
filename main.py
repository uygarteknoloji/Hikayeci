import sys
from PyQt5 import QtWidgets
from views.frmMain import frmMain


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = frmMain()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()