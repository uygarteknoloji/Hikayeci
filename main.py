import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from PyQt5.QtCore import QTimer
from views.frmMain import frmMain
from views.frmReklam import frmReklam


class AppController(QStackedWidget):

    MainTimer = 10_000  # 120 sn

    def __init__(self):
        super().__init__()

        self.frm_main = frmMain()
        self.frm_reklam = frmReklam()

        self.addWidget(self.frm_main)     # index 0
        self.addWidget(self.frm_reklam)   # index 1

        self.setCurrentWidget(self.frm_main)

        # 120 sn timer (formlar arası)
        self.switch_timer = QTimer(self)
        self.switch_timer.timeout.connect(self.toggle_forms)
        self.switch_timer.start(self.MainTimer)

        # Reklam tıklanınca ana forma dön
        self.frm_reklam.clicked.connect(self.show_main)

    def toggle_forms(self):
        if self.currentWidget() == self.frm_main:
            self.setCurrentWidget(self.frm_reklam)
        else:
            self.setCurrentWidget(self.frm_main)

    def show_main(self):
        self.setCurrentWidget(self.frm_main)
        self.reset_main_timer()

    def reset_main_timer(self):
        self.switch_timer.stop()
        self.switch_timer.start(self.MainTimer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController()
    controller.showFullScreen()   # kiosk için ideal
    sys.exit(app.exec_())
