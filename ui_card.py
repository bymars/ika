# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\linhongl\Desktop\python\card.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CardWidget(object):
    def setupUi(self, CardWidget):
        CardWidget.setObjectName(_fromUtf8("CardWidget"))
        CardWidget.resize(624, 554)
        self.gridLayout = QtGui.QGridLayout(CardWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnLayout = QtGui.QHBoxLayout()
        self.btnLayout.setObjectName(_fromUtf8("btnLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.btnLayout.addItem(spacerItem)
        self.btnImport = QtGui.QPushButton(CardWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.btnImport.setFont(font)
        self.btnImport.setObjectName(_fromUtf8("btnImport"))
        self.btnLayout.addWidget(self.btnImport)
        self.btnExport = QtGui.QPushButton(CardWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.btnExport.setFont(font)
        self.btnExport.setObjectName(_fromUtf8("btnExport"))
        self.btnLayout.addWidget(self.btnExport)
        self.btnStart = QtGui.QPushButton(CardWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.btnStart.setFont(font)
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.btnLayout.addWidget(self.btnStart)
        self.gridLayout.addLayout(self.btnLayout, 4, 0, 1, 7)
        self.checkLoop = QtGui.QCheckBox(CardWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.checkLoop.setFont(font)
        self.checkLoop.setObjectName(_fromUtf8("checkLoop"))
        self.gridLayout.addWidget(self.checkLoop, 0, 3, 1, 1)
        self.spinBoxThread = QtGui.QSpinBox(CardWidget)
        self.spinBoxThread.setObjectName(_fromUtf8("spinBoxThread"))
        self.gridLayout.addWidget(self.spinBoxThread, 0, 6, 1, 1)
        self.labelThread = QtGui.QLabel(CardWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.labelThread.setFont(font)
        self.labelThread.setObjectName(_fromUtf8("labelThread"))
        self.gridLayout.addWidget(self.labelThread, 0, 5, 1, 1)
        self.labelCard = QtGui.QLabel(CardWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.labelCard.setFont(font)
        self.labelCard.setObjectName(_fromUtf8("labelCard"))
        self.gridLayout.addWidget(self.labelCard, 0, 0, 1, 2)
        self.listTask = QtGui.QTableWidget(CardWidget)
        self.listTask.setObjectName(_fromUtf8("listTask"))
        self.listTask.setColumnCount(6)
        self.listTask.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.listTask.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.listTask.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.listTask.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.listTask.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.listTask.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.listTask.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.listTask, 3, 0, 1, 7)
        self.inputCard = QtGui.QLineEdit(CardWidget)
        self.inputCard.setObjectName(_fromUtf8("inputCard"))
        self.gridLayout.addWidget(self.inputCard, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)

        self.retranslateUi(CardWidget)
        QtCore.QMetaObject.connectSlotsByName(CardWidget)

    def retranslateUi(self, CardWidget):
        CardWidget.setWindowTitle(_translate("CardWidget", "自动领卡", None))
        self.btnImport.setText(_translate("CardWidget", "导入账号", None))
        self.btnExport.setText(_translate("CardWidget", "导出卡密", None))
        self.btnStart.setText(_translate("CardWidget", "开始工作", None))
        self.checkLoop.setText(_translate("CardWidget", "循环领取", None))
        self.labelThread.setText(_translate("CardWidget", "工作线程", None))
        self.labelCard.setText(_translate("CardWidget", "领卡ID:", None))
        item = self.listTask.horizontalHeaderItem(0)
        item.setText(_translate("CardWidget", "序号", None))
        item = self.listTask.horizontalHeaderItem(1)
        item.setText(_translate("CardWidget", "账号", None))
        item = self.listTask.horizontalHeaderItem(2)
        item.setText(_translate("CardWidget", "用户名", None))
        item = self.listTask.horizontalHeaderItem(3)
        item.setText(_translate("CardWidget", "密码", None))
        item = self.listTask.horizontalHeaderItem(4)
        item.setText(_translate("CardWidget", "登录状态", None))
        item = self.listTask.horizontalHeaderItem(5)
        item.setText(_translate("CardWidget", "卡密数据", None))

