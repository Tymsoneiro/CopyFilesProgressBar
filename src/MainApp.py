from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QThread
from Controls.CopyFilesButton import CopyFilesButton
from Controls.CopyFilesProgressBar import CopyFilesProgressBar
from Workers.WorkerCopyFiles import WorkerCopyFiles

pathOrigAll = r".\data\original\**"
pathCopyAll = r".\data\copied\**"
pathOrig = r".\data\original"
pathCopy = r".\data\copied"

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.threadCopy = QThread()

        self.copyBtn = CopyFilesButton(self, "Copy files", 10, 10, 100, 25, self.threadCopy)
        self.progressBar = CopyFilesProgressBar(self, 10, 50, 250, 20)

        self.workerCopy = WorkerCopyFiles(pathOrigAll, pathCopy)
        self.workerCopy.moveToThread(self.threadCopy)

        self.threadCopy.started.connect(lambda: self.copyBtn.setEnabled(False))
        self.threadCopy.started.connect(lambda: self.progressBar.setValue(0))
        self.threadCopy.started.connect(self.workerCopy.run)
        self.workerCopy.progress.connect(self.progressBar.reportProgress)
        self.workerCopy.finished.connect(lambda: self.copyBtn.setEnabled(True))
        self.workerCopy.finished.connect(lambda: self.progressBar.setFormat("Copy files completed"))
        self.workerCopy.finished.connect(self.threadCopy.quit)
        self.workerCopy.finished.connect(self.workerCopy.deleteLater)
        self.threadCopy.finished.connect(self.threadCopy.deleteLater)

        self.setWindowTitle('Copy Files Progress Bar')
        self.setGeometry(10, 10, 300, 150)
        self.move(850, 300)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()