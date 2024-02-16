# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui-new_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import res-new-window-rc_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(325, 286)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans;")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_NewTransaction = QLabel(self.frame)
        self.lbl_NewTransaction.setObjectName(u"lbl_NewTransaction")
        self.lbl_NewTransaction.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_NewTransaction.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_NewTransaction)

        self.cb_Category = QComboBox(self.frame)
        self.cb_Category.addItem("")
        self.cb_Category.addItem("")
        self.cb_Category.addItem("")
        self.cb_Category.addItem("")
        self.cb_Category.addItem("")
        self.cb_Category.setObjectName(u"cb_Category")
        self.cb_Category.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color: black;\n"
"}")

        self.verticalLayout.addWidget(self.cb_Category)

        self.date = QDateEdit(self.frame)
        self.date.setObjectName(u"date")
        self.date.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"")
        self.date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))

        self.verticalLayout.addWidget(self.date)

        self.le_Description = QLineEdit(self.frame)
        self.le_Description.setObjectName(u"le_Description")
        self.le_Description.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"")

        self.verticalLayout.addWidget(self.le_Description)

        self.le_Balance = QLineEdit(self.frame)
        self.le_Balance.setObjectName(u"le_Balance")
        self.le_Balance.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"")

        self.verticalLayout.addWidget(self.le_Balance)

        self.cb_Income = QComboBox(self.frame)
        self.cb_Income.addItem("")
        self.cb_Income.addItem("")
        self.cb_Income.setObjectName(u"cb_Income")
        self.cb_Income.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color: black;\n"
"}")

        self.verticalLayout.addWidget(self.cb_Income)

        self.btn_Newtransaction = QPushButton(self.frame)
        self.btn_Newtransaction.setObjectName(u"btn_Newtransaction")
        self.btn_Newtransaction.setStyleSheet(u"QPushButton {\n"
"color:white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgbe(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,70)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Newtransaction.setIcon(icon)
        self.btn_Newtransaction.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_Newtransaction)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.cb_Category.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_NewTransaction.setText(QCoreApplication.translate("Dialog", u"New transaction", None))
        self.cb_Category.setItemText(0, QCoreApplication.translate("Dialog", u"Groceries", None))
        self.cb_Category.setItemText(1, QCoreApplication.translate("Dialog", u"Entertainment", None))
        self.cb_Category.setItemText(2, QCoreApplication.translate("Dialog", u"Auto", None))
        self.cb_Category.setItemText(3, QCoreApplication.translate("Dialog", u"Other", None))
        self.cb_Category.setItemText(4, QCoreApplication.translate("Dialog", u"Work", None))

        self.cb_Category.setPlaceholderText(QCoreApplication.translate("Dialog", u"Choose category", None))
        self.le_Description.setPlaceholderText(QCoreApplication.translate("Dialog", u"Description", None))
        self.le_Balance.setPlaceholderText(QCoreApplication.translate("Dialog", u"Balance", None))
        self.cb_Income.setItemText(0, QCoreApplication.translate("Dialog", u"Income", None))
        self.cb_Income.setItemText(1, QCoreApplication.translate("Dialog", u"Outcome", None))

        self.btn_Newtransaction.setText(QCoreApplication.translate("Dialog", u"Save new transaction", None))
    # retranslateUi

