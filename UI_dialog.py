# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import numpy
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    def __init__(self):
        self.list = numpy.arange(13)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 317)
        Dialog.setMinimumSize(QtCore.QSize(480, 317))
        Dialog.setMaximumSize(QtCore.QSize(480, 317))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/siren.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(160, 260, 164, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(70, 10, 357, 234))
        self.widget.setObjectName("widget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.c_init = QtWidgets.QDoubleSpinBox(self.widget)
        self.c_init.setProperty("value", 0.1)
        self.c_init.setObjectName("c_init")
        self.gridLayout_2.addWidget(self.c_init, 0, 0, 1, 1)
        self.u_init = QtWidgets.QDoubleSpinBox(self.widget)
        self.u_init.setProperty("value", 0.8)
        self.u_init.setObjectName("u_init")
        self.gridLayout_2.addWidget(self.u_init, 1, 0, 1, 1)
        self.alpha = QtWidgets.QDoubleSpinBox(self.widget)
        self.alpha.setProperty("value", 0.1)
        self.alpha.setObjectName("alpha")
        self.gridLayout_2.addWidget(self.alpha, 2, 0, 1, 1)
        self.beta = QtWidgets.QDoubleSpinBox(self.widget)
        self.beta.setProperty("value", 0.2)
        self.beta.setObjectName("beta")
        self.gridLayout_2.addWidget(self.beta, 3, 0, 1, 1)
        self.delta_init = QtWidgets.QDoubleSpinBox(self.widget)
        self.delta_init.setProperty("value", 0.5)
        self.delta_init.setObjectName("delta_init")
        self.gridLayout_2.addWidget(self.delta_init, 4, 0, 1, 1)
        self.gamma_init = QtWidgets.QDoubleSpinBox(self.widget)
        self.gamma_init.setProperty("value", 0.4)
        self.gamma_init.setObjectName("gamma_init")
        self.gridLayout_2.addWidget(self.gamma_init, 5, 0, 1, 1)
        self.delta_max = QtWidgets.QDoubleSpinBox(self.widget)
        self.delta_max.setProperty("value", 0.5)
        self.delta_max.setObjectName("delta_max")
        self.gridLayout_2.addWidget(self.delta_max, 6, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 4, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 5, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.delta_min = QtWidgets.QDoubleSpinBox(self.widget)
        self.delta_min.setProperty("value", 0.2)
        self.delta_min.setObjectName("delta_min")
        self.gridLayout_5.addWidget(self.delta_min, 0, 0, 1, 1)
        self.gamma_max = QtWidgets.QDoubleSpinBox(self.widget)
        self.gamma_max.setProperty("value", 1.0)
        self.gamma_max.setObjectName("gamma_max")
        self.gridLayout_5.addWidget(self.gamma_max, 1, 0, 1, 1)
        self.gamma_min = QtWidgets.QDoubleSpinBox(self.widget)
        self.gamma_min.setProperty("value", 0.1)
        self.gamma_min.setObjectName("gamma_min")
        self.gridLayout_5.addWidget(self.gamma_min, 2, 0, 1, 1)
        self.maxTimes = QtWidgets.QSpinBox(self.widget)
        self.maxTimes.setProperty("value", 10)
        self.maxTimes.setObjectName("maxTimes")
        self.gridLayout_5.addWidget(self.maxTimes, 3, 0, 1, 1)
        self.T = QtWidgets.QSpinBox(self.widget)
        self.T.setProperty("value", 10)
        self.T.setObjectName("T")
        self.gridLayout_5.addWidget(self.T, 4, 0, 1, 1)
        self.h = QtWidgets.QDoubleSpinBox(self.widget)
        self.h.setProperty("value", 0.01)
        self.h.setObjectName("h")
        self.gridLayout_5.addWidget(self.h, 5, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #def saveArgument(self,Dialog):
        # list[0]=self.c_init.value()
        # list[1] = self.u_init.value()
        # list[2] = self.alpha.value()
        # list[3] = self.beta.value()
        # list[4] = self.delta_init.value()
        # list[5] = self.gamma_init.value()
        # list[6] = self.delta_max.value()
        # list[7] = self.delta_min.value()
        # list[8] = self.gamma_max.value()
        # list[9] = self.gamma_min.value()
        # list[10] = self.maxTimes.value()
        # list[11] = self.T.value()
        # list[12] = self.h.value()







    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "设置参数"))
        self.label.setText(_translate("Dialog", "染毒节点初始值:"))
        self.label_2.setText(_translate("Dialog", "正常节点初始值:"))
        self.label_3.setText(_translate("Dialog", "节点感染率:"))
        self.label_4.setText(_translate("Dialog", "节点间传染率:"))
        self.label_5.setText(_translate("Dialog", "初始隔离率:"))
        self.label_6.setText(_translate("Dialog", "初始恢复率:"))
        self.label_7.setText(_translate("Dialog", "隔离率上限:"))
        self.label_8.setText(_translate("Dialog", "隔离率下限:"))
        self.label_9.setText(_translate("Dialog", "恢复率上限:"))
        self.label_10.setText(_translate("Dialog", "恢复率下限:"))
        self.label_11.setText(_translate("Dialog", "最大迭代次数:"))
        self.label_12.setText(_translate("Dialog", "周期长度:"))
        self.label_13.setText(_translate("Dialog", "步长:"))

#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec())
