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
from wanc import Ui_MainWindow
class myWidget(QWidget):
    def __init__(self):
        super(myWidget,self).__init__()
        # 设置界面为我们生成的界面
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, myWidget):
        if not myWidget.objectName():
            myWidget.setObjectName(u"myWidget")
        myWidget.resize(469, 546)
        self.label1 = QLabel(myWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(180, 10, 201, 41))
        self.label1.setMinimumSize(QSize(0, 0))
        self.label1.setBaseSize(QSize(0, 0))
        self.groupBox = QGroupBox(myWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 90, 191, 81))
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dial = QDial(self.groupBox)
        self.dial.setObjectName(u"dial")

        self.horizontalLayout.addWidget(self.dial)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.groupBox_2 = QGroupBox(myWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(260, 90, 181, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dial_2 = QDial(self.groupBox_2)
        self.dial_2.setObjectName(u"dial_2")

        self.horizontalLayout_2.addWidget(self.dial_2)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.groupBox_3 = QGroupBox(myWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(60, 220, 291, 291))
        self.textBrowser = QTextBrowser(self.groupBox_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 60, 251, 221))
        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 10, 141, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.label5 = QLabel(myWidget)
        self.label5.setObjectName(u"label1")
        self.label5.setGeometry(QRect(10, 40, 311, 41))

        self.lineEdit = QLineEdit(myWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 40, 311, 41))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.pushButton_4 = QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.pushButton.clicked.connect(self.translate)

        self.retranslateUi(myWidget)
        self.pushButton_4.clicked.connect(self.xianshi)
        self.pushButton_2.clicked.connect(myWidget.close)

        QMetaObject.connectSlotsByName(myWidget)
    # setupUi
    def translate(self):
        hello_1.show()
        myWidget.close()
    def xianshi(self):
        self.textBrowser.setText("杭州市御和堂中医\n地址：钱塘区-盛泰名都公寓2幢\n电话：17767113556\n医生主治：腰椎酸痛，疾病预防")
    def retranslateUi(self, myWidget):
        myWidget.setWindowTitle(QCoreApplication.translate("myWidget", u"中医联盟", None))
        self.label1.setText(QCoreApplication.translate("myWidget", u"中医联盟智能推荐系统", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("myWidget", u"\u5f00\u59cb", None))
        self.pushButton.setText(QCoreApplication.translate("myWidget", u"start", None))
        self.groupBox_2.setTitle("")
        self.label_2.setText(QCoreApplication.translate("myWidget", u"暂停", None))
        self.pushButton_2.setText(QCoreApplication.translate("myWidget", u"stop", None))
        self.groupBox_3.setTitle("")
        self.groupBox_4.setTitle("")
        self.label_4.setText(QCoreApplication.translate("myWidget", u"推荐结果", None))
        self.pushButton_4.setText(QCoreApplication.translate("myWidget", u"print", None))
    # retranslateUi
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myWidget()
    hello_1=Ui_Form()
    window.show()
    sys.exit(app.exec_())
