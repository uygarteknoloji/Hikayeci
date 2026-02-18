from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer, QRect, pyqtSignal, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QPixmap

class frmReklam(QWidget):
    clicked = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.images = [
            "resimler/reklam1.jpg",
            "resimler/reklam2.jpg",
            "resimler/reklam3.jpg",
        ]
        self.index = 0

        # aktif label
        self.label_current = QLabel(self)
        self.label_current.setAlignment(Qt.AlignCenter)
        self.label_current.setGeometry(self.rect())

        # animasyonla gelecek label
        self.label_next = QLabel(self)
        self.label_next.setAlignment(Qt.AlignCenter)

        self.load_image(self.label_current, self.images[self.index])

        self.slide_timer = QTimer(self)
        self.slide_timer.timeout.connect(self.next_image)
        self.slide_timer.start(2000)

    def resizeEvent(self, event):
        self.label_current.setGeometry(self.rect())

    def load_image(self, label, path):
        pix = QPixmap(path)
        label.setPixmap(
            pix.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

    def next_image(self):
        next_index = (self.index + 1) % len(self.images)
        self.load_image(self.label_next, self.images[next_index])

        w = self.width()
        h = self.height()

        # next label sağdan başlasın
        self.label_next.setGeometry(w, 0, w, h)
        self.label_next.show()

        # mevcut resim sola kayıyor
        anim_out = QPropertyAnimation(self.label_current, b"geometry")
        anim_out.setDuration(600)
        anim_out.setStartValue(QRect(0, 0, w, h))
        anim_out.setEndValue(QRect(-w, 0, w, h))
        anim_out.setEasingCurve(QEasingCurve.OutBack)

        # yeni resim sağdan geliyor
        anim_in = QPropertyAnimation(self.label_next, b"geometry")
        anim_in.setDuration(600)
        anim_in.setStartValue(QRect(w, 0, w, h))
        anim_in.setEndValue(QRect(0, 0, w, h))
        anim_in.setEasingCurve(QEasingCurve.OutBack)

        anim_out.start()
        anim_in.start()

        # animasyon bitince label'ları değiştir
        def finish():
            self.label_current.setGeometry(0, 0, w, h)
            self.label_current.setPixmap(self.label_next.pixmap())
            self.label_next.hide()
            self.index = next_index

        anim_in.finished.connect(finish)

        # referansları tut (GC yemesin)
        self.anim_out = anim_out
        self.anim_in = anim_in

    def mousePressEvent(self, event):
        self.clicked.emit()
