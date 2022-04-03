from PyQt5.QtWidgets import QPushButton

class CopyFilesButton(QPushButton):
    def __init__(self, parent=None, text=None, ax=0, ay=0, w=0, h=0, threadCopy=None) -> None:
        super().__init__(parent)
        self.threadCopy = threadCopy
        self.clicked.connect(self.OnClicked)
        self.setGeometry(ax, ay, w, h)
        self.setText(text)
        self.show()

    def OnClicked(self):
        self.threadCopy.start()