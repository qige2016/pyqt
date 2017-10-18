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
        self.work_place = ["成都", "全国"]
        for index in range(len(self.work_place)):
            self.comboBox.insertItem(index, self.work_place[index])

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 20, 100, 30))
        self.comboBox_2.setObjectName("comboBox")
        self.publish_time = ["2017"]
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
        self.pushButton.clicked.connect(self.clickedEvent)
        self.url1 = 'http://www.jiuye.org/new/sys/fore.php?op=listRecruit'
        self.pushButton_2.clicked.connect(self.clickedEvent_2)
        self.pushButton_3.clicked.connect(self.clickedEvent_3)


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
    def clickedEvent(self):
        self.tableWidget.clearContents()
        self.find(url=self.url1)
    def clickedEvent_2(self):
        self.tableWidget.clearContents()
        self.find_2()
    def clickedEvent_3(self):
        self.tableWidget.clearContents()
        self.find_3()
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

    def find_2(self):
        def get_content(page):
            if self.comboBox.currentText() == '成都':
                jobarea = '090200'
            else:jobarea = '000000'
            if self.lineEdit.text() == '':
                keyword = ' '
            else: keyword = self.lineEdit.text()
            url = 'http://search.51job.com/list/'+jobarea+',000000,0000,00,9,99,'+keyword+',2,' + str(page)+'.html'
            a = requests.get(url).content
            html = a.decode('gbk')
            return html
        def parse_html(html):
            reg = re.compile(r'class="t1 ">.*? <a target="_blank" title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>',re.S)  # 匹配换行符
            items = re.findall(reg, html)
            return items
        RowCount = self.tableWidget.rowCount()
        count = 0
        for i in range(1, 50):
            html = get_content(i)
            items = parse_html(html)
            for item, row in zip(items, range(0 + count, RowCount - 1)):
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(item[2]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(item[0]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(item[1]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(item[4]))
                count += 1
            RowCount += 50
    def find_3(self):
        def get_content(page):
            if self.lineEdit.text() == '':
                keyword = ' '
            else: keyword = self.lineEdit.text()
            url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl='+self.comboBox.currentText()+'&kw='+keyword+'&p=' + str(page) + '&kt=3'
            a = requests.get(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'
            }).content
            html = a.decode('utf8')
            return html

        def parse_html(html):
            reg = re.compile(
                r'<td class="zwmc.*?<a.*?>(.*?)</a>.*?<td class="gsmc.*?_blank">(.*?)</a>.*?<td class="zwyx">(.*?)</td.*?<td class="gzdd">(.*?)</td.*?<td class="gxsj"><span>(.*?)</span>',
                re.S)  # 匹配换行符
            results = re.findall(reg, html)
            rs_data = []
            for rs in results:
                remove_b = re.compile(r'<.*?>', re.S)
                name = re.sub(remove_b, '', rs[0])
                rs_tp = (name, rs[1], rs[2], rs[3], rs[4])
                rs_data.append(rs_tp)
            return rs_data
        RowCount = self.tableWidget.rowCount()
        count = 0
        for i in range(1, 50):
            html = get_content(i)
            items = parse_html(html)
            for item, row in zip(items, range(0 + count, RowCount - 1)):
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(item[3]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(item[0]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(item[1]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(item[4]))
                count += 1
            RowCount += 60

