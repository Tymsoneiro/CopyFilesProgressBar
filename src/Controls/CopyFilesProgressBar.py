from PyQt5.QtWidgets import QProgressBar

class CopyFilesProgressBar(QProgressBar):
    def __init__(self, parent, ax, ay, w, h) -> None:
        super().__init__(parent)
        self.setGeometry(ax, ay, w, h)
        self.show()

    def reportProgress(self, n):
        self.setValue(n)