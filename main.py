import sys
from PyQt5 import QtWidgets
from views.frmMain import frmMain
from views.frmMenu import frmMenu

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = frmMain()
    win.menu = None  # Menü penceresi için bir özellik ekleyelim
    win.mousePressEvent = mousePressEvent.__get__(win, frmMain) 
    win.show()
    sys.exit(app.exec_())

def mousePressEvent(self, event):
        if self.menu is None:
            self.menu = frmMenu()
        self.menu.show()    

if __name__ == "__main__":
    app()