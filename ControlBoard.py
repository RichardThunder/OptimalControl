import sys

from PyQt6 import QtCore, QtGui,QtWidgets
from PyQt6.QtCore import QEventLoop, QTimer, QObject, pyqtSignal, QThread, QCoreApplication
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from net.LoadGraph import *
from Opt_Sta import CompareMain
from UI_MainWindow import Ui_MainWindow
from UI_dialog import Ui_Dialog
from util.draw import *
class EmitStr(QObject):
    '''
    定义一个信号类，
    sys.stdout有个write方法，通过重定向，
    每当有新字符串输出时就会触发下面定义的write函数，
    进而发出信号
    text：新字符串，会通过信号传递出去
    '''
    textWrit  = pyqtSignal(str)
    def write(self, text):
        self.textWrit.emit(str(text))


class ControlBoard(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ControlBoard, self).__init__()

        self.setupUi(self)


        # 下面将输出重定向到textBrowser中
        sys.stdout = EmitStr(textWrit=self.outputWrite)  # 输出结果重定向
        sys.stderr = EmitStr(textWrit=self.outputWrite)  # 错误输出重定向


        self.pushButton.clicked.connect(self.bClicked)

        self.setArgument1.triggered.connect(self.showDialog)
        self.setArgument2.triggered.connect(self.showDialog)
        self.setArgument3.triggered.connect(self.showDialog)
        self.openNet.triggered.connect(self.openfile)
        self.newRandomNet.triggered.connect(self.newRandom)
        self.saveOPT.triggered.connect(self.save)
        self.actionwfrre.triggered.connect(self.closeapp)
        self.help.triggered.connect(self.showhelp)
        self.AboutThis.triggered.connect(self.showinfo)

    def openfile(self):
        fname, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '文本文件(*.txt)')
        print(fname)
        graph = Get_arenas_email_Network(fname)[3]
        drawClub(graph)
        self.label_34.setPixmap(QtGui.QPixmap("./net/club.png"))



    def outputWrite(self, text):
        self.textBrowser.append(text)
        # cursor = self.textBrowser.textCursor()
        # cursor.movePosition(QtGui.QTextCursor.End)
        # cursor.insertText(text)
        # self.textBrowser.setTextCursor(cursor)
        # self.textBrowser.ensureCursorVisible()

    def bClicked(self):
        """Runs the main function."""
        self.statusbar.showMessage("开始执行最优控制，请勿退出！！！")
        self.mythread=MyThread()
        self.mythread.start()
        self.pushButton.setEnabled(False)
        self.pushButton.setText("运行中")
        self.timer.start(10000, self)
        self.mythread.finished.connect(self.thread_finish_process)

    def thread_finish_process(self):
        self.step=100


    def timerEvent(self, event):
        if self.step >= 100 :
            self.timer.stop()
            # 修改文本标签显示内容
            self.statusbar.showMessage("程序执行完毕，请查看结果 ")
            # 启用按钮
            self.pushButton.setEnabled(True)
            # 修改按钮显示内容
            self.pushButton.setText("运行")
            self.step=0
            self.progressBar.setValue(self.step)
            self.label_35.setPixmap(QtGui.QPixmap("OPtr/61.png"))
            self.label_34.setPixmap(QtGui.QPixmap("net/club.png"))


            return
        # 累计步数
        self.step = self.step + 1
        # 修改进度条的值
        self.progressBar.setValue(self.step)

    def newRandom(self):
        self.label_34.setPixmap(QtGui.QPixmap("net/football.png"))

    def showDialog(self):
        Dialog.show()

    def save(self):

        QMessageBox.information(self, '已保存', '控制策略已保存' )
        # if reply == QMessageBox.StandardButton.Yes:
        #     self.accept()

    def closeapp(self):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            QCoreApplication.instance().quit()

    def showhelp(self):
        QMessageBox.information(self, '帮助', '文件->导入网络->运行。 等待运行结果')
    def showinfo(self):
        QMessageBox.information(self,'关于此程序',"Author:Richard @CopyRight 2022")
    def setNewArgument(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("MainWindow", "染毒节点初始值:"))
        self.label_7.setText(_translate("MainWindow", "正常节点初始值:"))
        self.label_10.setText(_translate("MainWindow", "节点感染率:"))
        self.label_13.setText(_translate("MainWindow", str(Ui_Dialog.c_init )))
        self.label_14.setText(_translate("MainWindow", "0.8"))
        self.label_15.setText(_translate("MainWindow", "0.1"))
        self.label_8.setText(_translate("MainWindow", "节点间传染率:"))
        self.label_9.setText(_translate("MainWindow", "初始隔离率:"))
        self.label_11.setText(_translate("MainWindow", "初始恢复率:"))
        self.label_16.setText(_translate("MainWindow", "0.2"))
        self.label_17.setText(_translate("MainWindow", "0.5"))
        self.label_18.setText(_translate("MainWindow", "0.4"))
        self.label_21.setText(_translate("MainWindow", "隔离率上限:"))
        self.label_22.setText(_translate("MainWindow", "隔离率下限:"))
        self.label_23.setText(_translate("MainWindow", "恢复率上限:"))
        self.label_24.setText(_translate("MainWindow", "恢复率下限:"))
        self.label_27.setText(_translate("MainWindow", "1.2"))
        self.label_28.setText(_translate("MainWindow", "0.2"))
        self.label_29.setText(_translate("MainWindow", "1"))
        self.label_30.setText(_translate("MainWindow", "0.1"))
        self.label_19.setText(_translate("MainWindow", "最大迭代次数:"))
        self.label_25.setText(_translate("MainWindow", "周期长度:"))
        self.label_26.setText(_translate("MainWindow", "步长:"))
        self.label_20.setText(_translate("MainWindow", "10"))
        self.label_31.setText(_translate("MainWindow", "10"))
        self.label_32.setText(_translate("MainWindow", "0.01"))




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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ControlBoard()
    win.show()
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    sys.exit(app.exec())