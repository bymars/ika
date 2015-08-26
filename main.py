#! /usr/bin/env python
import sip, os
sip.setapi('QString', 2)
from PyQt4 import QtCore, QtGui
from ui_card import Ui_CardWidget
from card import Card
import time

class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_CardWidget()
        self.ui.setupUi(self)
        
        self.load_user()
        self.update_list()

    def load_user(self):
        file_path = os.path.join(os.path.dirname(__file__), 'info.txt')
        file = open(file_path)
        lines = file.readlines()
        file.close()
        self.user_list = []
        for line in lines:
            line = line.strip('\n')
            words = line.split(' ---- ')
            if len(words) == 2:
                self.user_list.append({'username':words[0], 'password': words[1], 'state': 0, 'card_no': ''})

    def update_list(self):
        for user in self.user_list:
            row = self.ui.listTask.rowCount()
            self.ui.listTask.insertRow(row)
            newItem = QtGui.QTableWidgetItem(str(row + 1))  
            self.ui.listTask.setItem(row, 0, newItem)
            newItem = QtGui.QTableWidgetItem(user['username'])  
            self.ui.listTask.setItem(row, 1, newItem)
            newItem = QtGui.QTableWidgetItem(user['password'])  
            self.ui.listTask.setItem(row, 2, newItem)
    
    def callback(self, index):
        user = self.user_list[index]
        if user['state'] ==  1:
            newItem = QtGui.QTableWidgetItem('登录中')
            self.ui.listTask.setItem(index, 3, newItem)
        if user['state'] ==  2:
            newItem = QtGui.QTableWidgetItem('成功')
            self.ui.listTask.setItem(index, 3, newItem)
            newItem = QtGui.QTableWidgetItem('领取中，请稍后')
            self.ui.listTask.setItem(index, 4, newItem)
        if user['state'] ==  3:
            newItem = QtGui.QTableWidgetItem('恭喜您，领取成功')
            self.ui.listTask.setItem(index, 4, newItem)
            newItem = QtGui.QTableWidgetItem(user['card_no'])
            self.ui.listTask.setItem(index, 5, newItem)
        
    @QtCore.pyqtSlot(int)
    def on_spinBoxThread_valueChanged(self, value):
        self.ui.inputCard.setText(str(value))
        
    @QtCore.pyqtSlot()
    def on_btnStart_clicked(self):
        threads = []
        for i in range(5):
            card = Card(13091, self.user_list, self.callback)
            threads.append(card)
            card.start()

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())