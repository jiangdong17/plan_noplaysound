# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stertUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow,QApplication,QInputDialog
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
global t

class Ui_start(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 400)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(80, 280, 491, 80))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(40, 30, 421, 35))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 10, 531, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setGeometry(QtCore.QRect(90, 230, 421, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 230, 58, 16))
        self.label.setObjectName("label")
        self.widget1 = QtWidgets.QWidget(self.groupBox_2)
        self.widget1.setGeometry(QtCore.QRect(330, 180, 141, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber.setObjectName("lcdNumber")

        # self.lcdNumber.display(？？？)#此处倒入倒计时

        self.horizontalLayout_2.addWidget(self.lcdNumber)
        self.widget2 = QtWidgets.QWidget(self.groupBox_2)
        self.widget2.setGeometry(QtCore.QRect(330, 130, 141, 25))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.widget2)
        self.lcdNumber_2.setObjectName("lcdNumber_2")

        # self.lcdNumber_2.display(1000)#此处需倒入计划的时间

        self.horizontalLayout_3.addWidget(self.lcdNumber_2)
        self.widget3 = QtWidgets.QWidget(self.groupBox_2)
        self.widget3.setGeometry(QtCore.QRect(330, 60, 141, 21))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.widget3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.widget4 = QtWidgets.QWidget(self.groupBox_2)
        self.widget4.setGeometry(QtCore.QRect(330, 100, 141, 21))
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.label_6.setBuddy(self.label_6)

        self.setup()




        #
        self.timer = QTimer()

        # self.pushButton.clicked.connect(self.startTimer)
        # self.pushButton_2.clicked.connect(self.showTime)
        # self.pushButton_3.clicked.connect(self.pauseTimer)




        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def setup(self):
        self.lcdNumber_2.display(0)
        # self.lcdNumber.display(0)
        self.number = 0
        self.timer = QTimer()
        self.second = 0
        # self.lcdNumber.display(self.second)
        self.pushButton.clicked.connect(self.timerStart)
        self.pushButton_2.clicked.connect(self.timerRest)

    def timerRest(self):
        self.number = int(QInputDialog.getText(None,"输入时间","请输入您要设置的时间")[0])
        self.lcdNumber_2.display(self.number)

    def timerStart(self):
        self.pushButton.setEnabled(False)
        self.timer.singleShot(10000,self.nextSecond)

    # def nextSecond(self):
    #     if self.number == self.second:
    #         self.timer.stop()
    #         # QMessageBox(self,"提示信息","时间到！",QmessageBox.Yes)
    #         QMessageBox.information(None, "提示", "时间到！", QMessageBox.Ok)
    #         self.pushButton.setEnabled(True)
    #     else:#执行但未显示
    #         self.second += 1
    #         # t = self.second
    #         print(self.second,1)
    #         self.lcdNumber.display(self.number- self.second)
    #         self.timer.singleShot(1000,self.nextSecond())
            # self.show()
    def nextSecond(self):

        self.second += 1
            # t = self.second
        print(self.second, 1)
        self.lcdNumber.display(self.number - self.second)
        self.timer.singleShot(1000, self.ret())
    def ret(self):
        if self.number != self.second:
            self.timer.singleShot(1000, self.nextSecond)
        else:
            self.timer.stop()
            # QMessageBox(self,"提示信息","时间到！",QmessageBox.Yes)
            QMessageBox.information(None, "提示", "时间到！", QMessageBox.Ok)
            self.pushButton.setEnabled(True)



    #
    # def showTime(self):
    #     if self._pause_flag:
    #         self._pause_total += self._restart_time - self._pause_time
    #         self._pause_flag = False
    #
    #     run_time = self._current_time - self._pause_total - self._start_time
    #     text = convert(run_time)
    #     self.label_5.setText(text)
    #
    # def convert(raw_time):
    #     hour = int(raw_time // 3600)
    #     minute = int((raw_time % 3600) // 60)
    #     second = int(raw_time % 60)
    #     fmt = "{:0>2d}:{:0>2d}:{:0>2d}"
    #     return fmt.format(hour,minute,second)
    # def startTimer(self):
    #     self.timer.start(0)
    #     if not  self._pause_flag:
    #         self._start_time = self._current_time
    #     self.setPushBuyyon(btn1=False,btn2=True,btn3=True)
    #
    # def pauseTimer(self):
    #     self._pause_flag = True
    #     self._pause_time = self._current_time
    #     self.timer.stop()
    #     self.setPushButton(btn1=True,btn2=False,btn3=True)
    #
    # def clearTime(self):
    #     self.init_setting()
    #     self.timer.stop()
    #     self.setPishButton()
    #     print(self._pause_time,self._start_time)
    #
    #
    # def now_time(self):
    #     pass
    #
    # def long(self):
    #     pass

    # def

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.pushButton.setText(_translate("Form", "开始"))
        self.pushButton_3.setText(_translate("Form", "暂停"))
        self.pushButton_2.setText(_translate("Form", "完成"))
        self.groupBox_2.setTitle(_translate("Form", "GroupBox"))
        self.label.setText(_translate("Form", "进度："))
        self.label_2.setText(_translate("Form", "倒计时："))
        self.label_3.setText(_translate("Form", "计划时长："))
        self.label_6.setText(_translate("Form", "科      目："))
        self.label_7.setText(_translate("Form", "TextLabel"))
        self.label_4.setText(_translate("Form", "内      容："))
        self.label_5.setText(_translate("Form", "TextLabel"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_start() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程