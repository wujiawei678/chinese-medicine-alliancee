# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '11111.ui'
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
from PySide6.QtWidgets import (QApplication, QDial, QFrame, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QWidget)
from wanc import Ui_MainWindow
class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form,self).__init__()
        # 设置界面为我们生成的界面
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(416, 408)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 60, 71, 16))
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(70, 190, 231, 101))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dial = QDial(self.frame)
        self.dial.setObjectName(u"dial")

        self.gridLayout.addWidget(self.dial, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(60, 90, 241, 21))
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(310, 90, 54, 16))

        self.retranslateUi(Form)

        self.pushButton_2.clicked.connect(Form.close)
        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"机器正在工作中", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6b63\u5728\u8bc6\u522b\u4e2d...", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7d27\u6025\u505c\u6b62", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"stop", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"80%", None))
    # retranslateUi

