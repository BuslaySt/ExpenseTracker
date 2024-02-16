# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui-main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(728, 429)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.balance_frame = QFrame(self.centralwidget)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.balance_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.lbl_CurrentBalance = QLabel(self.balance_frame)
        self.lbl_CurrentBalance.setObjectName(u"lbl_CurrentBalance")
        self.lbl_CurrentBalance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lbl_CurrentBalance)

        self.lbl_Balance = QLabel(self.balance_frame)
        self.lbl_Balance.setObjectName(u"lbl_Balance")
        self.lbl_Balance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lbl_Balance)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_UpArrow = QLabel(self.balance_frame)
        self.icon_UpArrow.setObjectName(u"icon_UpArrow")
        self.icon_UpArrow.setMaximumSize(QSize(24, 16777215))
        self.icon_UpArrow.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.icon_UpArrow.setPixmap(QPixmap(u":/icons/icons/north_west_white_24dp.svg"))

        self.horizontalLayout.addWidget(self.icon_UpArrow)

        self.lbl_Income = QLabel(self.balance_frame)
        self.lbl_Income.setObjectName(u"lbl_Income")
        self.lbl_Income.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.horizontalLayout.addWidget(self.lbl_Income)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lbl_IncomeBalance = QLabel(self.balance_frame)
        self.lbl_IncomeBalance.setObjectName(u"lbl_IncomeBalance")
        self.lbl_IncomeBalance.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lbl_IncomeBalance)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.icon_DownArrow = QLabel(self.balance_frame)
        self.icon_DownArrow.setObjectName(u"icon_DownArrow")
        self.icon_DownArrow.setMaximumSize(QSize(24, 16777215))
        self.icon_DownArrow.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.icon_DownArrow.setPixmap(QPixmap(u":/icons/icons/call_received_white_24dp.svg"))

        self.horizontalLayout_2.addWidget(self.icon_DownArrow)

        self.lbl_Outcome = QLabel(self.balance_frame)
        self.lbl_Outcome.setObjectName(u"lbl_Outcome")
        self.lbl_Outcome.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.horizontalLayout_2.addWidget(self.lbl_Outcome)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lbl_OutcomeBalance = QLabel(self.balance_frame)
        self.lbl_OutcomeBalance.setObjectName(u"lbl_OutcomeBalance")
        self.lbl_OutcomeBalance.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lbl_OutcomeBalance)


        self.horizontalLayout_7.addWidget(self.balance_frame)

        self.categories_frame = QFrame(self.centralwidget)
        self.categories_frame.setObjectName(u"categories_frame")
        self.categories_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.categories_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.lbl_ExpenseCategory = QLabel(self.categories_frame)
        self.lbl_ExpenseCategory.setObjectName(u"lbl_ExpenseCategory")
        self.lbl_ExpenseCategory.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.lbl_ExpenseCategory)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.icon_Groceries = QLabel(self.categories_frame)
        self.icon_Groceries.setObjectName(u"icon_Groceries")
        self.icon_Groceries.setMaximumSize(QSize(24, 16777215))
        self.icon_Groceries.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_Groceries.setPixmap(QPixmap(u":/icons/icons/local_grocery_store_white_24dp.svg"))

        self.horizontalLayout_6.addWidget(self.icon_Groceries)

        self.lbl_Groceries = QLabel(self.categories_frame)
        self.lbl_Groceries.setObjectName(u"lbl_Groceries")
        self.lbl_Groceries.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.lbl_Groceries)

        self.lbl_GroceriesBalance = QLabel(self.categories_frame)
        self.lbl_GroceriesBalance.setObjectName(u"lbl_GroceriesBalance")
        self.lbl_GroceriesBalance.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.lbl_GroceriesBalance)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.icon_Entertainment = QLabel(self.categories_frame)
        self.icon_Entertainment.setObjectName(u"icon_Entertainment")
        self.icon_Entertainment.setMaximumSize(QSize(24, 16777215))
        self.icon_Entertainment.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_Entertainment.setPixmap(QPixmap(u":/icons/icons/sports_esports_white_24dp.svg"))

        self.horizontalLayout_5.addWidget(self.icon_Entertainment)

        self.lbl_Entertainment = QLabel(self.categories_frame)
        self.lbl_Entertainment.setObjectName(u"lbl_Entertainment")
        self.lbl_Entertainment.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.lbl_Entertainment)

        self.lbl_EntertainmentBalance = QLabel(self.categories_frame)
        self.lbl_EntertainmentBalance.setObjectName(u"lbl_EntertainmentBalance")
        self.lbl_EntertainmentBalance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.lbl_EntertainmentBalance)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.icon_Auto = QLabel(self.categories_frame)
        self.icon_Auto.setObjectName(u"icon_Auto")
        self.icon_Auto.setMaximumSize(QSize(24, 16777215))
        self.icon_Auto.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_Auto.setPixmap(QPixmap(u":/icons/icons/directions_car_white_24dp.svg"))

        self.horizontalLayout_4.addWidget(self.icon_Auto)

        self.lbl_Auto = QLabel(self.categories_frame)
        self.lbl_Auto.setObjectName(u"lbl_Auto")
        self.lbl_Auto.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.lbl_Auto)

        self.lbl_AutoBalance = QLabel(self.categories_frame)
        self.lbl_AutoBalance.setObjectName(u"lbl_AutoBalance")
        self.lbl_AutoBalance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.lbl_AutoBalance)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.icon_Other = QLabel(self.categories_frame)
        self.icon_Other.setObjectName(u"icon_Other")
        self.icon_Other.setMaximumSize(QSize(24, 16777215))
        self.icon_Other.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_Other.setPixmap(QPixmap(u":/icons/icons/list_white_24dp.svg"))

        self.horizontalLayout_3.addWidget(self.icon_Other)

        self.lbl_Other = QLabel(self.categories_frame)
        self.lbl_Other.setObjectName(u"lbl_Other")
        self.lbl_Other.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.lbl_Other)

        self.lbl_OtherBalance = QLabel(self.categories_frame)
        self.lbl_OtherBalance.setObjectName(u"lbl_OtherBalance")
        self.lbl_OtherBalance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.lbl_OtherBalance)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_7.addWidget(self.categories_frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_NewTransaction = QPushButton(self.centralwidget)
        self.btn_NewTransaction.setObjectName(u"btn_NewTransaction")
        self.btn_NewTransaction.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u":/icons/icons/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_NewTransaction.setIcon(icon)
        self.btn_NewTransaction.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_NewTransaction)

        self.btn_EditTransaction = QPushButton(self.centralwidget)
        self.btn_EditTransaction.setObjectName(u"btn_EditTransaction")
        self.btn_EditTransaction.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/edit_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_EditTransaction.setIcon(icon1)
        self.btn_EditTransaction.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_EditTransaction)

        self.btn_DelTransaction = QPushButton(self.centralwidget)
        self.btn_DelTransaction.setObjectName(u"btn_DelTransaction")
        self.btn_DelTransaction.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/delete_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_DelTransaction.setIcon(icon2)
        self.btn_DelTransaction.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_DelTransaction)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"border-button-right-radius: 7px;\n"
"}\n"
"QTableView:section {\n"
"color:white;\n"
"background-color: rgba(53,53,53);\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"QTableView:item {\n"
"border-style: none;\n"
"border-bottom: rgba(255,255,255,50);\n"
"}\n"
"QTableView:item:selected{\n"
"border: none;\n"
"color: rgba(255,255,255)\n"
"background-color: rgba(255,255,255,50);\n"
"}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setMinimumSectionSize(44)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Expense Tracker", None))
        self.lbl_CurrentBalance.setText(QCoreApplication.translate("MainWindow", u"Current Balance", None))
        self.lbl_Balance.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.icon_UpArrow.setText("")
        self.lbl_Income.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.lbl_IncomeBalance.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.icon_DownArrow.setText("")
        self.lbl_Outcome.setText(QCoreApplication.translate("MainWindow", u"Outcome", None))
        self.lbl_OutcomeBalance.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.lbl_ExpenseCategory.setText(QCoreApplication.translate("MainWindow", u"Expense category", None))
        self.icon_Groceries.setText("")
        self.lbl_Groceries.setText(QCoreApplication.translate("MainWindow", u"Groceries", None))
        self.lbl_GroceriesBalance.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.icon_Entertainment.setText("")
        self.lbl_Entertainment.setText(QCoreApplication.translate("MainWindow", u"Entertainment", None))
        self.lbl_EntertainmentBalance.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.icon_Auto.setText("")
        self.lbl_Auto.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.lbl_AutoBalance.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.icon_Other.setText("")
        self.lbl_Other.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.lbl_OtherBalance.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.btn_NewTransaction.setText(QCoreApplication.translate("MainWindow", u"New transaction", None))
        self.btn_EditTransaction.setText(QCoreApplication.translate("MainWindow", u"Edit transaction", None))
        self.btn_DelTransaction.setText(QCoreApplication.translate("MainWindow", u"Delete transaction", None))
    # retranslateUi

