from PyQt6.QtCore import QThread, pyqtSignal
from Opt_Sta import CompareMain


class MyThread(QThread):
    signalForText = pyqtSignal(str)

    def __init__(self, data=None, parent=None):
        super(MyThread, self).__init__(parent)
        self.data = data

    def write(self, text):
        self.signalForText.emit(str(text))  # 发射信号

    def run(self):
        print("start")
        CompareMain()