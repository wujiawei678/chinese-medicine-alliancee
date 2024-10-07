# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mywidget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDial, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QTextBrowser,QLineEdit,
    QWidget)
import sys
from aaa import Ui_Form

class myWidget(object):
    def __init__(self):
        super(myWidget,self).__init__()
        # 设置界面为我们生成的界面
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, myWidget):
        if not myWidget.objectName():
            myWidget.setObjectName(u"myWidget")
        myWidget.resize(530, 687)
        font = QFont()
        font.setPointSize(11)
        myWidget.setFont(font)
        self.label1 = QLabel(myWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(200, 10, 201, 41))
        self.label1.setMinimumSize(QSize(0, 0))
        self.label1.setBaseSize(QSize(0, 0))
        self.groupBox = QGroupBox(myWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 140, 151, 71))
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.groupBox_2 = QGroupBox(myWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(280, 140, 141, 71))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.groupBox_3 = QGroupBox(myWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(50, 260, 361, 341))
        self.textBrowser = QTextBrowser(self.groupBox_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 60, 311, 261))
        font1 = QFont()
        font1.setPointSize(17)
        self.textBrowser.setFont(font1)
        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 10, 161, 51))
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.pushButton_4 = QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.lineEdit = QLineEdit(myWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 70, 311, 41))
        self.label_3 = QLabel(myWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 151, 41))
        self.label_3.setFont(font)

        self.retranslateUi(myWidget)

        QMetaObject.connectSlotsByName(myWidget)
    # setupUi

    def retranslateUi(self, myWidget):
        myWidget.setWindowTitle(QCoreApplication.translate("myWidget", u"myWidget", None))
        self.label1.setText(QCoreApplication.translate("myWidget", u"<html><head/><body><p><span style=\" font-size:20pt;\">\u4e2d\u533b\u8054\u76df</span></p></body></html>", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("myWidget", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.pushButton.setText(QCoreApplication.translate("myWidget", u"start", None))
        self.groupBox_2.setTitle("")
        self.label_2.setText(QCoreApplication.translate("myWidget", u"\u7d27\u6025\u505c\u6b62", None))
        self.pushButton_2.setText(QCoreApplication.translate("myWidget", u"stop", None))
        self.groupBox_3.setTitle("")
        self.groupBox_4.setTitle("")
        self.label_4.setText(QCoreApplication.translate("myWidget", u"\u6570\u636e\u8f93\u51fa", None))
        self.pushButton_4.setText(QCoreApplication.translate("myWidget", u"print", None))
        self.label_3.setText(QCoreApplication.translate("myWidget", u"\u8bf7\u8f93\u5165\u75c5\u7406\u7279\u5f81\uff1a", None))
    # retranslateUi
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myWidget()
    hello_1=Ui_Form()
    window.show()
    sys.exit(app.exec_())
