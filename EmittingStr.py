from PyQt6 import QtCore
from PyQt6.QtCore import QEventLoop, QTimer


class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str) #定义一个发送str的信号
    def write(self, text):
      self.textWritten.emit(str(text))
      loop = QEventLoop()
      QTimer.singleShot(1000, loop.quit)
      loop.exec_()