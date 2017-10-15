# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Crawler.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json
import re

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1100, 20, 220, 30))
        self.lineEdit.setObjectName("lineEdit")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 20, 70, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(600, 20, 200, 30))
        self.comboBox.setObjectName("comboBox")
        self.work_place = ["四川-成都|全国-所有省市", ""]
        for index in range(len(self.work_place)):
            self.comboBox.insertItem(index, self.work_place[index])

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 20, 100, 30))
        self.comboBox_2.setObjectName("comboBox")
        self.publish_time = ["2017", "2016", "2015", ""]
        for index in range(len(self.publish_time)):
            self.comboBox_2.insertItem(index, self.publish_time[index])

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1000, 20, 70, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 70, 30))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 140, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 150, 140, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 230, 140, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 310, 140, 50))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton.clicked.connect(self.clickedEvent)
        self.url1 = 'http://www.jiuye.org/new/sys/fore.php?op=listRecruit'

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(190, 70, 1150, 640))
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(500)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 550)
        self.tableWidget.setColumnWidth(3, 250)
        self.tableWidget.setHorizontalHeaderLabels(['序号', '工作地点', '职位名称', '公司名称', '发布日期'])

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "招聘网爬虫"))
        self.pushButton_3.setText(_translate("MainWindow", "智联招聘"))
        self.label.setText(_translate("MainWindow", "工作地点"))
        self.label_2.setText(_translate("MainWindow", "职位名称"))
        self.label_3.setText(_translate("MainWindow", "发布时间"))
        self.pushButton.setText(_translate("MainWindow", "电子科大就业网"))
        self.pushButton_2.setText(_translate("MainWindow", "前程无忧"))
        self.pushButton_4.setText(_translate("MainWindow", "拉勾网"))
    def clickedEvent(self):
        self.tableWidget.clearContents()
        self.find(url=self.url1)
    def find(self, url):
        RowCount = self.tableWidget.rowCount()
        count = 0
        for i in range(1, 50):
            data = {
                'page': str(i),
                'rec_way': '1',
                    }
    # 使用requests发送post请求
            resp = requests.post(url, data=data).text
            info = json.loads(resp)
    # 正则匹配工作地点
            pattern1 = re.compile(r'(?:%s)' % (self.comboBox.currentText()))
    # 正则匹配职位名称
            pattern2 = re.compile(r'(?:%s)' % (self.lineEdit.text()), re.IGNORECASE)
    # 正则匹配发布时间
            pattern3 = re.compile(r'(?:%s)' % (self.comboBox_2.currentText()))
            for item, row in zip(info['data'], range(0 + count, RowCount - 1)):
                result1 = re.search(pattern1, item['rec_work_place'])
                result2 = re.search(pattern2, item['rec_title'])
                result3 = re.match(pattern3, item['rec_publish_time'])
                if result1 and result2 and result3:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(item['rec_No']))
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(item['rec_work_place']))
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(item['rec_title']))
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(item['rec_enter_name']))
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(item['rec_publish_time']))
                    count += 1
            RowCount += 20



