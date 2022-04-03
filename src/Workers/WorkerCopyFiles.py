from time import sleep
from PyQt5.QtCore import QObject, pyqtSignal
import shutil
import os
import subprocess
import glob

class WorkerCopyFiles(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(float)

    def __init__(self, pathOrig, pathCopy) -> None:
        super().__init__()
        self.pathOrig = pathOrig
        self.pathCopy = pathCopy
        self.numberOfFiles = 0

    def run(self):  
        if os.path.exists(self.pathCopy):
            shutil.rmtree(self.pathCopy)
            os.mkdir(self.pathCopy)

        files = glob.glob(self.pathOrig, recursive=True)
        self.numberOfFiles = len(files)
        for i, file in enumerate(files):
            dst = file.replace(self.pathOrig[:-2], self.pathCopy + "\\")

            if os.path.isdir(file) and not os.path.exists(dst):
                print("Creating dir ", dst)
                os.mkdir(dst)
                self.progress.emit((i + 1) / self.numberOfFiles * 100)
                continue

            cmdStr = 'copy {0} {1}'.format(file, dst)
            subprocess.call(cmdStr, shell=True)
            self.progress.emit((i + 1) / self.numberOfFiles * 100)

        self.finished.emit()