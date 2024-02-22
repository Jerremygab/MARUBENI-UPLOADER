# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TransactionUploader.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)
import Icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(941, 669)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	margin: 5\n"
"}\n"
"\n"
"QLabel{\n"
"	padding: 3;\n"
"	border-radius: 20px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 6, 0, 1, 6)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 6)

        self.pushButton_browse = QPushButton(self.centralwidget)
        self.pushButton_browse.setObjectName(u"pushButton_browse")
        self.pushButton_browse.setMaximumSize(QSize(75, 16777215))
        self.pushButton_browse.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout.addWidget(self.pushButton_browse, 1, 2, 1, 1)

        self.lineEdit_filename = QLineEdit(self.centralwidget)
        self.lineEdit_filename.setObjectName(u"lineEdit_filename")
        self.lineEdit_filename.setMinimumSize(QSize(500, 0))

        self.gridLayout.addWidget(self.lineEdit_filename, 1, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 1, 1, 3)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 4, 1, 2)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"	background-color: #f3d162\n"
"\n"
"}")
        self.tabWidget.setElideMode(Qt.ElideRight)
        self.tab_grpo = QWidget()
        self.tab_grpo.setObjectName(u"tab_grpo")
        self.tab_grpo.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.tab_grpo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_grpo_total_exist = QLabel(self.tab_grpo)
        self.label_grpo_total_exist.setObjectName(u"label_grpo_total_exist")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_grpo_total_exist.sizePolicy().hasHeightForWidth())
        self.label_grpo_total_exist.setSizePolicy(sizePolicy1)
        self.label_grpo_total_exist.setMinimumSize(QSize(100, 0))
        self.label_grpo_total_exist.setMaximumSize(QSize(200, 16777215))
        self.label_grpo_total_exist.setStyleSheet(u"QLabel {\n"
"background-color:brown;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_2.addWidget(self.label_grpo_total_exist, 2, 2, 1, 1)

        self.label = QLabel(self.tab_grpo)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setMaximumSize(QSize(200, 16777215))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"QLabel {\n"
"background-color:red;\n"
"color:white;\n"
"font-weight: bold;\n"
"border-radius: 25px\n"
"}")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.tableWidget_grpo = QTableWidget(self.tab_grpo)
        if (self.tableWidget_grpo.columnCount() < 26):
            self.tableWidget_grpo.setColumnCount(26)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(21, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(22, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(23, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(24, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_grpo.setHorizontalHeaderItem(25, __qtablewidgetitem25)
        self.tableWidget_grpo.setObjectName(u"tableWidget_grpo")
        self.tableWidget_grpo.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_2.addWidget(self.tableWidget_grpo, 16, 0, 1, 5)

        self.pushButton_upload_grpo = QPushButton(self.tab_grpo)
        self.pushButton_upload_grpo.setObjectName(u"pushButton_upload_grpo")
        sizePolicy.setHeightForWidth(self.pushButton_upload_grpo.sizePolicy().hasHeightForWidth())
        self.pushButton_upload_grpo.setSizePolicy(sizePolicy)
        self.pushButton_upload_grpo.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_upload_grpo, 17, 0, 1, 1)

        self.label_grpo_total_bp_not_exist = QLabel(self.tab_grpo)
        self.label_grpo_total_bp_not_exist.setObjectName(u"label_grpo_total_bp_not_exist")
        sizePolicy1.setHeightForWidth(self.label_grpo_total_bp_not_exist.sizePolicy().hasHeightForWidth())
        self.label_grpo_total_bp_not_exist.setSizePolicy(sizePolicy1)
        self.label_grpo_total_bp_not_exist.setMinimumSize(QSize(200, 0))
        self.label_grpo_total_bp_not_exist.setMaximumSize(QSize(200, 16777215))
        self.label_grpo_total_bp_not_exist.setStyleSheet(u"QLabel {\n"
"background-color:orange;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_2.addWidget(self.label_grpo_total_bp_not_exist, 1, 0, 1, 2, Qt.AlignTop)

        self.pushButton_2 = QPushButton(self.tab_grpo)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_2, 12, 0, 1, 2)

        self.label_4 = QLabel(self.tab_grpo)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(200, 0))
        self.label_4.setMaximumSize(QSize(200, 16777215))
        self.label_4.setStyleSheet(u"QLabel {\n"
"background-color:green;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 1)

        self.pushButton_show_grpo = QPushButton(self.tab_grpo)
        self.pushButton_show_grpo.setObjectName(u"pushButton_show_grpo")
        self.pushButton_show_grpo.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_show_grpo, 0, 4, 1, 1)

        self.lineEdit_2 = QLineEdit(self.tab_grpo)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 12, 2, 1, 1)

        self.label_grpo_total_ready = QLabel(self.tab_grpo)
        self.label_grpo_total_ready.setObjectName(u"label_grpo_total_ready")
        self.label_grpo_total_ready.setStyleSheet(u"QLabel {\n"
"background-color:rgb(173, 216, 230);\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_2.addWidget(self.label_grpo_total_ready, 0, 3, 1, 1)

        self.line = QFrame(self.tab_grpo)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 11, 0, 1, 5)

        self.label_grpo_total_item_not_exist = QLabel(self.tab_grpo)
        self.label_grpo_total_item_not_exist.setObjectName(u"label_grpo_total_item_not_exist")
        sizePolicy1.setHeightForWidth(self.label_grpo_total_item_not_exist.sizePolicy().hasHeightForWidth())
        self.label_grpo_total_item_not_exist.setSizePolicy(sizePolicy1)
        self.label_grpo_total_item_not_exist.setMinimumSize(QSize(200, 0))
        self.label_grpo_total_item_not_exist.setMaximumSize(QSize(200, 16777215))
        self.label_grpo_total_item_not_exist.setStyleSheet(u"QLabel {\n"
"background-color:yellow;\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_2.addWidget(self.label_grpo_total_item_not_exist, 0, 2, 1, 1)

        self.pushButton_grpo_clear = QPushButton(self.tab_grpo)
        self.pushButton_grpo_clear.setObjectName(u"pushButton_grpo_clear")

        self.gridLayout_2.addWidget(self.pushButton_grpo_clear, 1, 4, 1, 1)

        self.tabWidget.addTab(self.tab_grpo, "")
        self.tab_apinvoice = QWidget()
        self.tab_apinvoice.setObjectName(u"tab_apinvoice")
        self.gridLayout_3 = QGridLayout(self.tab_apinvoice)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget_apinvoice = QTableWidget(self.tab_apinvoice)
        if (self.tableWidget_apinvoice.columnCount() < 31):
            self.tableWidget_apinvoice.setColumnCount(31)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(5, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(6, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(7, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(8, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(9, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(10, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(11, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(12, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(13, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(14, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(15, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(16, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(17, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(18, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(19, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(20, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(21, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(22, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(23, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(24, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(25, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(26, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(27, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(28, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(29, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget_apinvoice.setHorizontalHeaderItem(30, __qtablewidgetitem56)
        self.tableWidget_apinvoice.setObjectName(u"tableWidget_apinvoice")
        self.tableWidget_apinvoice.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_3.addWidget(self.tableWidget_apinvoice, 5, 0, 1, 4)

        self.lineEdit_3 = QLineEdit(self.tab_apinvoice)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 4, 1, 1, 1)

        self.label_apinvoice_total_bp_not_exist = QLabel(self.tab_apinvoice)
        self.label_apinvoice_total_bp_not_exist.setObjectName(u"label_apinvoice_total_bp_not_exist")
        sizePolicy1.setHeightForWidth(self.label_apinvoice_total_bp_not_exist.sizePolicy().hasHeightForWidth())
        self.label_apinvoice_total_bp_not_exist.setSizePolicy(sizePolicy1)
        self.label_apinvoice_total_bp_not_exist.setMinimumSize(QSize(200, 0))
        self.label_apinvoice_total_bp_not_exist.setMaximumSize(QSize(200, 16777215))
        self.label_apinvoice_total_bp_not_exist.setStyleSheet(u"QLabel {\n"
"background-color:orange;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_3.addWidget(self.label_apinvoice_total_bp_not_exist, 1, 0, 1, 1)

        self.label_2 = QLabel(self.tab_apinvoice)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setMaximumSize(QSize(200, 16777215))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"QLabel {\n"
"background-color:red;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_apinvoice_total_exist = QLabel(self.tab_apinvoice)
        self.label_apinvoice_total_exist.setObjectName(u"label_apinvoice_total_exist")
        sizePolicy1.setHeightForWidth(self.label_apinvoice_total_exist.sizePolicy().hasHeightForWidth())
        self.label_apinvoice_total_exist.setSizePolicy(sizePolicy1)
        self.label_apinvoice_total_exist.setMinimumSize(QSize(100, 0))
        self.label_apinvoice_total_exist.setMaximumSize(QSize(200, 16777215))
        self.label_apinvoice_total_exist.setStyleSheet(u"QLabel {\n"
"background-color:brown;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_3.addWidget(self.label_apinvoice_total_exist, 2, 1, 1, 1)

        self.label_apinvoice_total_item_not_exist = QLabel(self.tab_apinvoice)
        self.label_apinvoice_total_item_not_exist.setObjectName(u"label_apinvoice_total_item_not_exist")
        sizePolicy1.setHeightForWidth(self.label_apinvoice_total_item_not_exist.sizePolicy().hasHeightForWidth())
        self.label_apinvoice_total_item_not_exist.setSizePolicy(sizePolicy1)
        self.label_apinvoice_total_item_not_exist.setMinimumSize(QSize(200, 0))
        self.label_apinvoice_total_item_not_exist.setMaximumSize(QSize(200, 16777215))
        self.label_apinvoice_total_item_not_exist.setStyleSheet(u"QLabel {\n"
"background-color:yellow;\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_3.addWidget(self.label_apinvoice_total_item_not_exist, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.tab_apinvoice)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_3, 4, 0, 1, 1)

        self.line_2 = QFrame(self.tab_apinvoice)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 3, 0, 1, 4)

        self.pushButton_upload_apinvoice = QPushButton(self.tab_apinvoice)
        self.pushButton_upload_apinvoice.setObjectName(u"pushButton_upload_apinvoice")
        self.pushButton_upload_apinvoice.setMaximumSize(QSize(75, 16777215))
        self.pushButton_upload_apinvoice.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_upload_apinvoice, 6, 0, 1, 1)

        self.pushButton_show_apinvoice = QPushButton(self.tab_apinvoice)
        self.pushButton_show_apinvoice.setObjectName(u"pushButton_show_apinvoice")
        self.pushButton_show_apinvoice.setAutoFillBackground(False)
        self.pushButton_show_apinvoice.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_show_apinvoice, 0, 3, 1, 1)

        self.label_5 = QLabel(self.tab_apinvoice)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(200, 0))
        self.label_5.setMaximumSize(QSize(200, 16777215))
        self.label_5.setStyleSheet(u"QLabel {\n"
"background-color:green;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_3.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_apinvoice_total_ready = QLabel(self.tab_apinvoice)
        self.label_apinvoice_total_ready.setObjectName(u"label_apinvoice_total_ready")
        self.label_apinvoice_total_ready.setStyleSheet(u"QLabel {\n"
"background-color:rgb(173, 216, 230);\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_3.addWidget(self.label_apinvoice_total_ready, 0, 2, 1, 1)

        self.pushButton_apinvoice_clear = QPushButton(self.tab_apinvoice)
        self.pushButton_apinvoice_clear.setObjectName(u"pushButton_apinvoice_clear")

        self.gridLayout_3.addWidget(self.pushButton_apinvoice_clear, 1, 3, 1, 1)

        self.tabWidget.addTab(self.tab_apinvoice, "")
        self.tab_creditmemo = QWidget()
        self.tab_creditmemo.setObjectName(u"tab_creditmemo")
        self.gridLayout_4 = QGridLayout(self.tab_creditmemo)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.tab_creditmemo)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setMaximumSize(QSize(200, 16777215))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"QLabel {\n"
"background-color:red;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.tableWidget_apcm = QTableWidget(self.tab_creditmemo)
        if (self.tableWidget_apcm.columnCount() < 26):
            self.tableWidget_apcm.setColumnCount(26)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(2, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(3, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(4, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(5, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(6, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(7, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(8, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(9, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(10, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(11, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(12, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(13, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(14, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(15, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(16, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(17, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(18, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(19, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(20, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(21, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(22, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(23, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(24, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget_apcm.setHorizontalHeaderItem(25, __qtablewidgetitem82)
        self.tableWidget_apcm.setObjectName(u"tableWidget_apcm")
        self.tableWidget_apcm.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_4.addWidget(self.tableWidget_apcm, 6, 0, 1, 4)

        self.pushButton_show_apcm = QPushButton(self.tab_creditmemo)
        self.pushButton_show_apcm.setObjectName(u"pushButton_show_apcm")
        self.pushButton_show_apcm.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_4.addWidget(self.pushButton_show_apcm, 0, 3, 1, 1)

        self.lineEdit_4 = QLineEdit(self.tab_creditmemo)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_4.addWidget(self.lineEdit_4, 5, 1, 1, 1)

        self.line_3 = QFrame(self.tab_creditmemo)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 3, 0, 1, 4)

        self.pushButton_upload_apcm = QPushButton(self.tab_creditmemo)
        self.pushButton_upload_apcm.setObjectName(u"pushButton_upload_apcm")
        self.pushButton_upload_apcm.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_4.addWidget(self.pushButton_upload_apcm, 7, 0, 1, 1)

        self.label_6 = QLabel(self.tab_creditmemo)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(200, 0))
        self.label_6.setMaximumSize(QSize(200, 16777215))
        self.label_6.setStyleSheet(u"QLabel {\n"
"background-color:green;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_4.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_apcm_total_bp_not_exist = QLabel(self.tab_creditmemo)
        self.label_apcm_total_bp_not_exist.setObjectName(u"label_apcm_total_bp_not_exist")
        sizePolicy1.setHeightForWidth(self.label_apcm_total_bp_not_exist.sizePolicy().hasHeightForWidth())
        self.label_apcm_total_bp_not_exist.setSizePolicy(sizePolicy1)
        self.label_apcm_total_bp_not_exist.setMinimumSize(QSize(200, 0))
        self.label_apcm_total_bp_not_exist.setMaximumSize(QSize(200, 16777215))
        self.label_apcm_total_bp_not_exist.setStyleSheet(u"QLabel {\n"
"background-color:orange;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_4.addWidget(self.label_apcm_total_bp_not_exist, 1, 0, 1, 1)

        self.label_apcm_total_item_not_exist = QLabel(self.tab_creditmemo)
        self.label_apcm_total_item_not_exist.setObjectName(u"label_apcm_total_item_not_exist")
        sizePolicy1.setHeightForWidth(self.label_apcm_total_item_not_exist.sizePolicy().hasHeightForWidth())
        self.label_apcm_total_item_not_exist.setSizePolicy(sizePolicy1)
        self.label_apcm_total_item_not_exist.setMinimumSize(QSize(200, 0))
        self.label_apcm_total_item_not_exist.setMaximumSize(QSize(200, 16777215))
        self.label_apcm_total_item_not_exist.setStyleSheet(u"QLabel {\n"
"background-color:yellow;\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_4.addWidget(self.label_apcm_total_item_not_exist, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.tab_creditmemo)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_4.addWidget(self.pushButton_4, 4, 0, 2, 1)

        self.label_apcm_total_exist = QLabel(self.tab_creditmemo)
        self.label_apcm_total_exist.setObjectName(u"label_apcm_total_exist")
        sizePolicy1.setHeightForWidth(self.label_apcm_total_exist.sizePolicy().hasHeightForWidth())
        self.label_apcm_total_exist.setSizePolicy(sizePolicy1)
        self.label_apcm_total_exist.setMinimumSize(QSize(100, 0))
        self.label_apcm_total_exist.setMaximumSize(QSize(200, 16777215))
        self.label_apcm_total_exist.setStyleSheet(u"QLabel {\n"
"background-color:brown;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_4.addWidget(self.label_apcm_total_exist, 2, 1, 1, 1)

        self.label_apcm_total_ready = QLabel(self.tab_creditmemo)
        self.label_apcm_total_ready.setObjectName(u"label_apcm_total_ready")
        self.label_apcm_total_ready.setStyleSheet(u"QLabel {\n"
"background-color:rgb(173, 216, 230);\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_4.addWidget(self.label_apcm_total_ready, 0, 2, 1, 1)

        self.pushButton_apcm_clear = QPushButton(self.tab_creditmemo)
        self.pushButton_apcm_clear.setObjectName(u"pushButton_apcm_clear")

        self.gridLayout_4.addWidget(self.pushButton_apcm_clear, 1, 3, 1, 1)

        self.tabWidget.addTab(self.tab_creditmemo, "")
        self.tab_arinvoice = QWidget()
        self.tab_arinvoice.setObjectName(u"tab_arinvoice")
        self.gridLayout_6 = QGridLayout(self.tab_arinvoice)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_arinvoice_total_bp_not_exist = QLabel(self.tab_arinvoice)
        self.label_arinvoice_total_bp_not_exist.setObjectName(u"label_arinvoice_total_bp_not_exist")
        sizePolicy1.setHeightForWidth(self.label_arinvoice_total_bp_not_exist.sizePolicy().hasHeightForWidth())
        self.label_arinvoice_total_bp_not_exist.setSizePolicy(sizePolicy1)
        self.label_arinvoice_total_bp_not_exist.setMinimumSize(QSize(200, 0))
        self.label_arinvoice_total_bp_not_exist.setMaximumSize(QSize(200, 16777215))
        self.label_arinvoice_total_bp_not_exist.setStyleSheet(u"QLabel {\n"
"background-color:orange;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_6.addWidget(self.label_arinvoice_total_bp_not_exist, 1, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.tab_arinvoice)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_6.addWidget(self.lineEdit_6, 4, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.tab_arinvoice)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_6.addWidget(self.pushButton_6, 4, 0, 2, 1)

        self.pushButton_upload_arinvoice = QPushButton(self.tab_arinvoice)
        self.pushButton_upload_arinvoice.setObjectName(u"pushButton_upload_arinvoice")
        self.pushButton_upload_arinvoice.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_6.addWidget(self.pushButton_upload_arinvoice, 7, 0, 1, 1)

        self.tableWidget_arinvoice = QTableWidget(self.tab_arinvoice)
        if (self.tableWidget_arinvoice.columnCount() < 27):
            self.tableWidget_arinvoice.setColumnCount(27)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(0, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(1, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(2, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(3, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(4, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(5, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(6, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(7, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(8, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(9, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(10, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(11, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(12, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(13, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(14, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(15, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(16, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(17, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(18, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(19, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(20, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(21, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(22, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(23, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(24, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(25, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tableWidget_arinvoice.setHorizontalHeaderItem(26, __qtablewidgetitem109)
        self.tableWidget_arinvoice.setObjectName(u"tableWidget_arinvoice")
        self.tableWidget_arinvoice.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_6.addWidget(self.tableWidget_arinvoice, 6, 0, 1, 5)

        self.label_arinvoice_total_item_not_exist = QLabel(self.tab_arinvoice)
        self.label_arinvoice_total_item_not_exist.setObjectName(u"label_arinvoice_total_item_not_exist")
        sizePolicy1.setHeightForWidth(self.label_arinvoice_total_item_not_exist.sizePolicy().hasHeightForWidth())
        self.label_arinvoice_total_item_not_exist.setSizePolicy(sizePolicy1)
        self.label_arinvoice_total_item_not_exist.setMinimumSize(QSize(200, 0))
        self.label_arinvoice_total_item_not_exist.setMaximumSize(QSize(200, 16777215))
        self.label_arinvoice_total_item_not_exist.setStyleSheet(u"QLabel {\n"
"background-color:yellow;\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_6.addWidget(self.label_arinvoice_total_item_not_exist, 0, 1, 1, 1)

        self.line_5 = QFrame(self.tab_arinvoice)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_5, 3, 0, 1, 5)

        self.label_arinvoice_total_required_fields = QLabel(self.tab_arinvoice)
        self.label_arinvoice_total_required_fields.setObjectName(u"label_arinvoice_total_required_fields")
        sizePolicy1.setHeightForWidth(self.label_arinvoice_total_required_fields.sizePolicy().hasHeightForWidth())
        self.label_arinvoice_total_required_fields.setSizePolicy(sizePolicy1)
        self.label_arinvoice_total_required_fields.setMinimumSize(QSize(100, 0))
        self.label_arinvoice_total_required_fields.setMaximumSize(QSize(200, 16777215))
        self.label_arinvoice_total_required_fields.setAutoFillBackground(False)
        self.label_arinvoice_total_required_fields.setStyleSheet(u"QLabel {\n"
"background-color:red;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_6.addWidget(self.label_arinvoice_total_required_fields, 0, 0, 1, 1)

        self.pushButton_show_arinvoice = QPushButton(self.tab_arinvoice)
        self.pushButton_show_arinvoice.setObjectName(u"pushButton_show_arinvoice")
        self.pushButton_show_arinvoice.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_6.addWidget(self.pushButton_show_arinvoice, 0, 4, 1, 1)

        self.label_10 = QLabel(self.tab_arinvoice)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setMinimumSize(QSize(200, 0))
        self.label_10.setMaximumSize(QSize(200, 16777215))
        self.label_10.setStyleSheet(u"QLabel {\n"
"background-color:green;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_6.addWidget(self.label_10, 1, 1, 1, 1)

        self.label_arinvoice_total_exist = QLabel(self.tab_arinvoice)
        self.label_arinvoice_total_exist.setObjectName(u"label_arinvoice_total_exist")
        sizePolicy1.setHeightForWidth(self.label_arinvoice_total_exist.sizePolicy().hasHeightForWidth())
        self.label_arinvoice_total_exist.setSizePolicy(sizePolicy1)
        self.label_arinvoice_total_exist.setMinimumSize(QSize(100, 0))
        self.label_arinvoice_total_exist.setMaximumSize(QSize(200, 16777215))
        self.label_arinvoice_total_exist.setStyleSheet(u"QLabel {\n"
"background-color:brown;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_6.addWidget(self.label_arinvoice_total_exist, 2, 1, 1, 1)

        self.label_arinvoice_total_ready = QLabel(self.tab_arinvoice)
        self.label_arinvoice_total_ready.setObjectName(u"label_arinvoice_total_ready")
        sizePolicy1.setHeightForWidth(self.label_arinvoice_total_ready.sizePolicy().hasHeightForWidth())
        self.label_arinvoice_total_ready.setSizePolicy(sizePolicy1)
        self.label_arinvoice_total_ready.setMaximumSize(QSize(700, 16777215))
        self.label_arinvoice_total_ready.setStyleSheet(u"QLabel {\n"
"background-color:rgb(173, 216, 230);\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_6.addWidget(self.label_arinvoice_total_ready, 0, 2, 1, 1)

        self.pushButton_arinvoice_clear = QPushButton(self.tab_arinvoice)
        self.pushButton_arinvoice_clear.setObjectName(u"pushButton_arinvoice_clear")

        self.gridLayout_6.addWidget(self.pushButton_arinvoice_clear, 1, 4, 1, 1)

        self.tabWidget.addTab(self.tab_arinvoice, "")
        self.tab_billingstatement = QWidget()
        self.tab_billingstatement.setObjectName(u"tab_billingstatement")
        self.gridLayout_8 = QGridLayout(self.tab_billingstatement)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_arinvoice_total_required_fields_2 = QLabel(self.tab_billingstatement)
        self.label_arinvoice_total_required_fields_2.setObjectName(u"label_arinvoice_total_required_fields_2")
        sizePolicy1.setHeightForWidth(self.label_arinvoice_total_required_fields_2.sizePolicy().hasHeightForWidth())
        self.label_arinvoice_total_required_fields_2.setSizePolicy(sizePolicy1)
        self.label_arinvoice_total_required_fields_2.setMinimumSize(QSize(100, 0))
        self.label_arinvoice_total_required_fields_2.setMaximumSize(QSize(200, 16777215))
        self.label_arinvoice_total_required_fields_2.setAutoFillBackground(False)
        self.label_arinvoice_total_required_fields_2.setStyleSheet(u"QLabel {\n"
"background-color:red;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_8.addWidget(self.label_arinvoice_total_required_fields_2, 0, 0, 1, 1)

        self.label_arinvoice_total_item_not_exist_2 = QLabel(self.tab_billingstatement)
        self.label_arinvoice_total_item_not_exist_2.setObjectName(u"label_arinvoice_total_item_not_exist_2")
        sizePolicy1.setHeightForWidth(self.label_arinvoice_total_item_not_exist_2.sizePolicy().hasHeightForWidth())
        self.label_arinvoice_total_item_not_exist_2.setSizePolicy(sizePolicy1)
        self.label_arinvoice_total_item_not_exist_2.setMinimumSize(QSize(200, 0))
        self.label_arinvoice_total_item_not_exist_2.setMaximumSize(QSize(200, 16777215))
        self.label_arinvoice_total_item_not_exist_2.setStyleSheet(u"QLabel {\n"
"background-color:yellow;\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_8.addWidget(self.label_arinvoice_total_item_not_exist_2, 0, 1, 1, 1)

        self.label_arinvoice_total_ready_2 = QLabel(self.tab_billingstatement)
        self.label_arinvoice_total_ready_2.setObjectName(u"label_arinvoice_total_ready_2")
        sizePolicy1.setHeightForWidth(self.label_arinvoice_total_ready_2.sizePolicy().hasHeightForWidth())
        self.label_arinvoice_total_ready_2.setSizePolicy(sizePolicy1)
        self.label_arinvoice_total_ready_2.setMaximumSize(QSize(700, 16777215))
        self.label_arinvoice_total_ready_2.setStyleSheet(u"QLabel {\n"
"background-color:rgb(173, 216, 230);\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_8.addWidget(self.label_arinvoice_total_ready_2, 0, 2, 1, 1)

        self.pushButton_show_arinvoice_2 = QPushButton(self.tab_billingstatement)
        self.pushButton_show_arinvoice_2.setObjectName(u"pushButton_show_arinvoice_2")
        self.pushButton_show_arinvoice_2.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_8.addWidget(self.pushButton_show_arinvoice_2, 0, 3, 1, 1)

        self.label_arinvoice_total_bp_not_exist_2 = QLabel(self.tab_billingstatement)
        self.label_arinvoice_total_bp_not_exist_2.setObjectName(u"label_arinvoice_total_bp_not_exist_2")
        sizePolicy1.setHeightForWidth(self.label_arinvoice_total_bp_not_exist_2.sizePolicy().hasHeightForWidth())
        self.label_arinvoice_total_bp_not_exist_2.setSizePolicy(sizePolicy1)
        self.label_arinvoice_total_bp_not_exist_2.setMinimumSize(QSize(200, 0))
        self.label_arinvoice_total_bp_not_exist_2.setMaximumSize(QSize(200, 16777215))
        self.label_arinvoice_total_bp_not_exist_2.setStyleSheet(u"QLabel {\n"
"background-color:orange;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_8.addWidget(self.label_arinvoice_total_bp_not_exist_2, 1, 0, 1, 1)

        self.label_13 = QLabel(self.tab_billingstatement)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setMinimumSize(QSize(200, 0))
        self.label_13.setMaximumSize(QSize(200, 16777215))
        self.label_13.setStyleSheet(u"QLabel {\n"
"background-color:green;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_8.addWidget(self.label_13, 1, 1, 1, 1)

        self.label_arinvoice_total_exist_2 = QLabel(self.tab_billingstatement)
        self.label_arinvoice_total_exist_2.setObjectName(u"label_arinvoice_total_exist_2")
        sizePolicy1.setHeightForWidth(self.label_arinvoice_total_exist_2.sizePolicy().hasHeightForWidth())
        self.label_arinvoice_total_exist_2.setSizePolicy(sizePolicy1)
        self.label_arinvoice_total_exist_2.setMinimumSize(QSize(100, 0))
        self.label_arinvoice_total_exist_2.setMaximumSize(QSize(200, 16777215))
        self.label_arinvoice_total_exist_2.setStyleSheet(u"QLabel {\n"
"background-color:brown;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_8.addWidget(self.label_arinvoice_total_exist_2, 2, 1, 1, 1)

        self.line_7 = QFrame(self.tab_billingstatement)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_8.addWidget(self.line_7, 3, 0, 1, 4)

        self.pushButton_8 = QPushButton(self.tab_billingstatement)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_8.addWidget(self.pushButton_8, 4, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.tab_billingstatement)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_8.addWidget(self.lineEdit_8, 4, 1, 1, 1)

        self.tableWidget_arinvoice_2 = QTableWidget(self.tab_billingstatement)
        if (self.tableWidget_arinvoice_2.columnCount() < 28):
            self.tableWidget_arinvoice_2.setColumnCount(28)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(0, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(1, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(2, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(3, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(4, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(5, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(6, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(7, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(8, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(9, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(10, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(11, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(12, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(13, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(14, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(15, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(16, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(17, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(18, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(19, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(20, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(21, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(22, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(23, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(24, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(25, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(26, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tableWidget_arinvoice_2.setHorizontalHeaderItem(27, __qtablewidgetitem137)
        self.tableWidget_arinvoice_2.setObjectName(u"tableWidget_arinvoice_2")
        self.tableWidget_arinvoice_2.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_8.addWidget(self.tableWidget_arinvoice_2, 5, 0, 1, 4)

        self.pushButton_upload_arinvoice_2 = QPushButton(self.tab_billingstatement)
        self.pushButton_upload_arinvoice_2.setObjectName(u"pushButton_upload_arinvoice_2")
        self.pushButton_upload_arinvoice_2.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_8.addWidget(self.pushButton_upload_arinvoice_2, 6, 0, 1, 1)

        self.pushButton_arinvoice_clear_2 = QPushButton(self.tab_billingstatement)
        self.pushButton_arinvoice_clear_2.setObjectName(u"pushButton_arinvoice_clear_2")

        self.gridLayout_8.addWidget(self.pushButton_arinvoice_clear_2, 1, 3, 1, 1)

        self.tabWidget.addTab(self.tab_billingstatement, "")
        self.tab_debitmemo = QWidget()
        self.tab_debitmemo.setObjectName(u"tab_debitmemo")
        self.gridLayout_7 = QGridLayout(self.tab_debitmemo)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_show_arcm = QPushButton(self.tab_debitmemo)
        self.pushButton_show_arcm.setObjectName(u"pushButton_show_arcm")

        self.gridLayout_7.addWidget(self.pushButton_show_arcm, 0, 3, 1, 1)

        self.label_11 = QLabel(self.tab_debitmemo)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setMinimumSize(QSize(100, 0))
        self.label_11.setMaximumSize(QSize(200, 16777215))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet(u"QLabel {\n"
"background-color:red;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_7.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_arcm_total_bp_not_exist = QLabel(self.tab_debitmemo)
        self.label_arcm_total_bp_not_exist.setObjectName(u"label_arcm_total_bp_not_exist")
        sizePolicy1.setHeightForWidth(self.label_arcm_total_bp_not_exist.sizePolicy().hasHeightForWidth())
        self.label_arcm_total_bp_not_exist.setSizePolicy(sizePolicy1)
        self.label_arcm_total_bp_not_exist.setMinimumSize(QSize(200, 0))
        self.label_arcm_total_bp_not_exist.setMaximumSize(QSize(200, 16777215))
        self.label_arcm_total_bp_not_exist.setStyleSheet(u"QLabel {\n"
"background-color:orange;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_7.addWidget(self.label_arcm_total_bp_not_exist, 1, 0, 1, 1)

        self.label_arcm_total_exist = QLabel(self.tab_debitmemo)
        self.label_arcm_total_exist.setObjectName(u"label_arcm_total_exist")
        sizePolicy1.setHeightForWidth(self.label_arcm_total_exist.sizePolicy().hasHeightForWidth())
        self.label_arcm_total_exist.setSizePolicy(sizePolicy1)
        self.label_arcm_total_exist.setMinimumSize(QSize(100, 0))
        self.label_arcm_total_exist.setMaximumSize(QSize(200, 16777215))
        self.label_arcm_total_exist.setStyleSheet(u"QLabel {\n"
"background-color:brown;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_7.addWidget(self.label_arcm_total_exist, 2, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.tab_debitmemo)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_7.addWidget(self.lineEdit_7, 4, 1, 1, 1)

        self.line_6 = QFrame(self.tab_debitmemo)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line_6, 3, 0, 1, 4)

        self.tableWidget_arcm = QTableWidget(self.tab_debitmemo)
        if (self.tableWidget_arcm.columnCount() < 26):
            self.tableWidget_arcm.setColumnCount(26)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(0, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(1, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(2, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(3, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(4, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(5, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(6, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(7, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(8, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(9, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(10, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(11, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(12, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(13, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(14, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(15, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(16, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(17, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(18, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(19, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(20, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(21, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(22, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(23, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(24, __qtablewidgetitem162)
        __qtablewidgetitem163 = QTableWidgetItem()
        self.tableWidget_arcm.setHorizontalHeaderItem(25, __qtablewidgetitem163)
        self.tableWidget_arcm.setObjectName(u"tableWidget_arcm")
        self.tableWidget_arcm.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_7.addWidget(self.tableWidget_arcm, 6, 0, 1, 4)

        self.pushButton_upload_arcm = QPushButton(self.tab_debitmemo)
        self.pushButton_upload_arcm.setObjectName(u"pushButton_upload_arcm")
        self.pushButton_upload_arcm.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_upload_arcm, 7, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.tab_debitmemo)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_7.addWidget(self.pushButton_7, 4, 0, 1, 1)

        self.label_arcm_total_item_not_exist = QLabel(self.tab_debitmemo)
        self.label_arcm_total_item_not_exist.setObjectName(u"label_arcm_total_item_not_exist")
        sizePolicy1.setHeightForWidth(self.label_arcm_total_item_not_exist.sizePolicy().hasHeightForWidth())
        self.label_arcm_total_item_not_exist.setSizePolicy(sizePolicy1)
        self.label_arcm_total_item_not_exist.setMinimumSize(QSize(200, 0))
        self.label_arcm_total_item_not_exist.setMaximumSize(QSize(200, 16777215))
        self.label_arcm_total_item_not_exist.setStyleSheet(u"QLabel {\n"
"background-color:yellow;\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_7.addWidget(self.label_arcm_total_item_not_exist, 0, 1, 1, 1)

        self.label_12 = QLabel(self.tab_debitmemo)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setMinimumSize(QSize(200, 0))
        self.label_12.setMaximumSize(QSize(200, 16777215))
        self.label_12.setStyleSheet(u"QLabel {\n"
"background-color:green;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_7.addWidget(self.label_12, 1, 1, 1, 1)

        self.label_arcm_total_ready = QLabel(self.tab_debitmemo)
        self.label_arcm_total_ready.setObjectName(u"label_arcm_total_ready")
        self.label_arcm_total_ready.setStyleSheet(u"QLabel {\n"
"background-color:rgb(173, 216, 230);\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_7.addWidget(self.label_arcm_total_ready, 0, 2, 1, 1)

        self.pushButton_arcm_clear = QPushButton(self.tab_debitmemo)
        self.pushButton_arcm_clear.setObjectName(u"pushButton_arcm_clear")

        self.gridLayout_7.addWidget(self.pushButton_arcm_clear, 1, 3, 1, 1)

        self.tabWidget.addTab(self.tab_debitmemo, "")
        self.tab_journalentry = QWidget()
        self.tab_journalentry.setObjectName(u"tab_journalentry")
        self.gridLayout_10 = QGridLayout(self.tab_journalentry)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_ojdt_total_required_fields = QLabel(self.tab_journalentry)
        self.label_ojdt_total_required_fields.setObjectName(u"label_ojdt_total_required_fields")
        sizePolicy1.setHeightForWidth(self.label_ojdt_total_required_fields.sizePolicy().hasHeightForWidth())
        self.label_ojdt_total_required_fields.setSizePolicy(sizePolicy1)
        self.label_ojdt_total_required_fields.setMinimumSize(QSize(100, 0))
        self.label_ojdt_total_required_fields.setMaximumSize(QSize(200, 16777215))
        self.label_ojdt_total_required_fields.setAutoFillBackground(False)
        self.label_ojdt_total_required_fields.setStyleSheet(u"QLabel {\n"
"background-color:red;\n"
"color:white;\n"
"font-weight: bold;\n"
"border-radius: 25px\n"
"}")

        self.gridLayout_10.addWidget(self.label_ojdt_total_required_fields, 0, 0, 1, 1)

        self.label_ojdt_total_item_not_exist = QLabel(self.tab_journalentry)
        self.label_ojdt_total_item_not_exist.setObjectName(u"label_ojdt_total_item_not_exist")
        sizePolicy1.setHeightForWidth(self.label_ojdt_total_item_not_exist.sizePolicy().hasHeightForWidth())
        self.label_ojdt_total_item_not_exist.setSizePolicy(sizePolicy1)
        self.label_ojdt_total_item_not_exist.setMinimumSize(QSize(200, 0))
        self.label_ojdt_total_item_not_exist.setMaximumSize(QSize(200, 16777215))
        self.label_ojdt_total_item_not_exist.setStyleSheet(u"QLabel {\n"
"background-color:yellow;\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_10.addWidget(self.label_ojdt_total_item_not_exist, 0, 1, 1, 1)

        self.label_ojdt_total_ready = QLabel(self.tab_journalentry)
        self.label_ojdt_total_ready.setObjectName(u"label_ojdt_total_ready")
        self.label_ojdt_total_ready.setStyleSheet(u"QLabel {\n"
"background-color:rgb(173, 216, 230);\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_10.addWidget(self.label_ojdt_total_ready, 0, 2, 1, 1)

        self.pushButton_show_ojdt = QPushButton(self.tab_journalentry)
        self.pushButton_show_ojdt.setObjectName(u"pushButton_show_ojdt")
        self.pushButton_show_ojdt.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_10.addWidget(self.pushButton_show_ojdt, 0, 3, 1, 1)

        self.label_ojdt_total_bp_not_exist = QLabel(self.tab_journalentry)
        self.label_ojdt_total_bp_not_exist.setObjectName(u"label_ojdt_total_bp_not_exist")
        sizePolicy1.setHeightForWidth(self.label_ojdt_total_bp_not_exist.sizePolicy().hasHeightForWidth())
        self.label_ojdt_total_bp_not_exist.setSizePolicy(sizePolicy1)
        self.label_ojdt_total_bp_not_exist.setMinimumSize(QSize(200, 0))
        self.label_ojdt_total_bp_not_exist.setMaximumSize(QSize(200, 16777215))
        self.label_ojdt_total_bp_not_exist.setStyleSheet(u"QLabel {\n"
"background-color:orange;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_10.addWidget(self.label_ojdt_total_bp_not_exist, 1, 0, 1, 1)

        self.label_ojdt_total_gl_not_exist = QLabel(self.tab_journalentry)
        self.label_ojdt_total_gl_not_exist.setObjectName(u"label_ojdt_total_gl_not_exist")
        sizePolicy1.setHeightForWidth(self.label_ojdt_total_gl_not_exist.sizePolicy().hasHeightForWidth())
        self.label_ojdt_total_gl_not_exist.setSizePolicy(sizePolicy1)
        self.label_ojdt_total_gl_not_exist.setMinimumSize(QSize(200, 0))
        self.label_ojdt_total_gl_not_exist.setMaximumSize(QSize(200, 16777215))
        self.label_ojdt_total_gl_not_exist.setStyleSheet(u"QLabel {\n"
"background-color:green;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_10.addWidget(self.label_ojdt_total_gl_not_exist, 1, 1, 1, 1)

        self.label_ojdt_total_ready_2 = QPushButton(self.tab_journalentry)
        self.label_ojdt_total_ready_2.setObjectName(u"label_ojdt_total_ready_2")

        self.gridLayout_10.addWidget(self.label_ojdt_total_ready_2, 1, 3, 1, 1)

        self.label_ojdt_total_exist = QLabel(self.tab_journalentry)
        self.label_ojdt_total_exist.setObjectName(u"label_ojdt_total_exist")
        sizePolicy1.setHeightForWidth(self.label_ojdt_total_exist.sizePolicy().hasHeightForWidth())
        self.label_ojdt_total_exist.setSizePolicy(sizePolicy1)
        self.label_ojdt_total_exist.setMinimumSize(QSize(100, 0))
        self.label_ojdt_total_exist.setMaximumSize(QSize(200, 16777215))
        self.label_ojdt_total_exist.setStyleSheet(u"QLabel {\n"
"background-color:brown;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_10.addWidget(self.label_ojdt_total_exist, 2, 1, 1, 1)

        self.line_9 = QFrame(self.tab_journalentry)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_10.addWidget(self.line_9, 3, 0, 1, 4)

        self.pushButton_10 = QPushButton(self.tab_journalentry)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_10.addWidget(self.pushButton_10, 4, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.tab_journalentry)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_10.addWidget(self.lineEdit_10, 4, 1, 1, 1)

        self.tableWidget_ojdt = QTableWidget(self.tab_journalentry)
        if (self.tableWidget_ojdt.columnCount() < 24):
            self.tableWidget_ojdt.setColumnCount(24)
        __qtablewidgetitem164 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(0, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(1, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(2, __qtablewidgetitem166)
        __qtablewidgetitem167 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(3, __qtablewidgetitem167)
        __qtablewidgetitem168 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(4, __qtablewidgetitem168)
        __qtablewidgetitem169 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(5, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(6, __qtablewidgetitem170)
        __qtablewidgetitem171 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(7, __qtablewidgetitem171)
        __qtablewidgetitem172 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(8, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(9, __qtablewidgetitem173)
        __qtablewidgetitem174 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(10, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(11, __qtablewidgetitem175)
        __qtablewidgetitem176 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(12, __qtablewidgetitem176)
        __qtablewidgetitem177 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(13, __qtablewidgetitem177)
        __qtablewidgetitem178 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(14, __qtablewidgetitem178)
        __qtablewidgetitem179 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(15, __qtablewidgetitem179)
        __qtablewidgetitem180 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(16, __qtablewidgetitem180)
        __qtablewidgetitem181 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(17, __qtablewidgetitem181)
        __qtablewidgetitem182 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(18, __qtablewidgetitem182)
        __qtablewidgetitem183 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(19, __qtablewidgetitem183)
        __qtablewidgetitem184 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(20, __qtablewidgetitem184)
        __qtablewidgetitem185 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(21, __qtablewidgetitem185)
        __qtablewidgetitem186 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(22, __qtablewidgetitem186)
        __qtablewidgetitem187 = QTableWidgetItem()
        self.tableWidget_ojdt.setHorizontalHeaderItem(23, __qtablewidgetitem187)
        self.tableWidget_ojdt.setObjectName(u"tableWidget_ojdt")
        self.tableWidget_ojdt.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_10.addWidget(self.tableWidget_ojdt, 5, 0, 1, 4)

        self.pushButton_upload_ojdt = QPushButton(self.tab_journalentry)
        self.pushButton_upload_ojdt.setObjectName(u"pushButton_upload_ojdt")
        sizePolicy.setHeightForWidth(self.pushButton_upload_ojdt.sizePolicy().hasHeightForWidth())
        self.pushButton_upload_ojdt.setSizePolicy(sizePolicy)
        self.pushButton_upload_ojdt.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_10.addWidget(self.pushButton_upload_ojdt, 6, 0, 1, 1)

        self.tabWidget.addTab(self.tab_journalentry, "")
        self.tab_collection = QWidget()
        self.tab_collection.setObjectName(u"tab_collection")
        self.gridLayout_9 = QGridLayout(self.tab_collection)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_show_outgoing_2 = QPushButton(self.tab_collection)
        self.pushButton_show_outgoing_2.setObjectName(u"pushButton_show_outgoing_2")

        self.gridLayout_9.addWidget(self.pushButton_show_outgoing_2, 0, 3, 1, 1)

        self.pushButton_upload_outgoing_2 = QPushButton(self.tab_collection)
        self.pushButton_upload_outgoing_2.setObjectName(u"pushButton_upload_outgoing_2")
        self.pushButton_upload_outgoing_2.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_9.addWidget(self.pushButton_upload_outgoing_2, 6, 0, 1, 1)

        self.label_ovpm_total_bp_not_exist_2 = QLabel(self.tab_collection)
        self.label_ovpm_total_bp_not_exist_2.setObjectName(u"label_ovpm_total_bp_not_exist_2")
        sizePolicy1.setHeightForWidth(self.label_ovpm_total_bp_not_exist_2.sizePolicy().hasHeightForWidth())
        self.label_ovpm_total_bp_not_exist_2.setSizePolicy(sizePolicy1)
        self.label_ovpm_total_bp_not_exist_2.setMinimumSize(QSize(200, 0))
        self.label_ovpm_total_bp_not_exist_2.setMaximumSize(QSize(200, 16777215))
        self.label_ovpm_total_bp_not_exist_2.setStyleSheet(u"QLabel {\n"
"background-color:orange;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_9.addWidget(self.label_ovpm_total_bp_not_exist_2, 1, 0, 1, 1)

        self.label_9 = QLabel(self.tab_collection)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMinimumSize(QSize(200, 0))
        self.label_9.setMaximumSize(QSize(200, 16777215))
        self.label_9.setStyleSheet(u"QLabel {\n"
"background-color:green;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_9.addWidget(self.label_9, 1, 1, 1, 1)

        self.tableWidget_ovpm_2 = QTableWidget(self.tab_collection)
        if (self.tableWidget_ovpm_2.columnCount() < 25):
            self.tableWidget_ovpm_2.setColumnCount(25)
        __qtablewidgetitem188 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(0, __qtablewidgetitem188)
        __qtablewidgetitem189 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(1, __qtablewidgetitem189)
        __qtablewidgetitem190 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(2, __qtablewidgetitem190)
        __qtablewidgetitem191 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(3, __qtablewidgetitem191)
        __qtablewidgetitem192 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(4, __qtablewidgetitem192)
        __qtablewidgetitem193 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(5, __qtablewidgetitem193)
        __qtablewidgetitem194 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(6, __qtablewidgetitem194)
        __qtablewidgetitem195 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(7, __qtablewidgetitem195)
        __qtablewidgetitem196 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(8, __qtablewidgetitem196)
        __qtablewidgetitem197 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(9, __qtablewidgetitem197)
        __qtablewidgetitem198 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(10, __qtablewidgetitem198)
        __qtablewidgetitem199 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(11, __qtablewidgetitem199)
        __qtablewidgetitem200 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(12, __qtablewidgetitem200)
        __qtablewidgetitem201 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(13, __qtablewidgetitem201)
        __qtablewidgetitem202 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(14, __qtablewidgetitem202)
        __qtablewidgetitem203 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(15, __qtablewidgetitem203)
        __qtablewidgetitem204 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(16, __qtablewidgetitem204)
        __qtablewidgetitem205 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(17, __qtablewidgetitem205)
        __qtablewidgetitem206 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(18, __qtablewidgetitem206)
        __qtablewidgetitem207 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(19, __qtablewidgetitem207)
        __qtablewidgetitem208 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(20, __qtablewidgetitem208)
        __qtablewidgetitem209 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(21, __qtablewidgetitem209)
        __qtablewidgetitem210 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(22, __qtablewidgetitem210)
        __qtablewidgetitem211 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(23, __qtablewidgetitem211)
        __qtablewidgetitem212 = QTableWidgetItem()
        self.tableWidget_ovpm_2.setHorizontalHeaderItem(24, __qtablewidgetitem212)
        self.tableWidget_ovpm_2.setObjectName(u"tableWidget_ovpm_2")
        self.tableWidget_ovpm_2.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_9.addWidget(self.tableWidget_ovpm_2, 5, 0, 1, 4)

        self.label_14 = QLabel(self.tab_collection)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setMinimumSize(QSize(100, 0))
        self.label_14.setMaximumSize(QSize(200, 16777215))
        self.label_14.setAutoFillBackground(False)
        self.label_14.setStyleSheet(u"QLabel {\n"
"background-color:red;\n"
"color:white;\n"
"font-weight: bold;\n"
"padding: 3px;\n"
"}")

        self.gridLayout_9.addWidget(self.label_14, 0, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.tab_collection)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_9.addWidget(self.lineEdit_9, 4, 1, 1, 1)

        self.label_ovpm_total_exist_2 = QLabel(self.tab_collection)
        self.label_ovpm_total_exist_2.setObjectName(u"label_ovpm_total_exist_2")
        sizePolicy1.setHeightForWidth(self.label_ovpm_total_exist_2.sizePolicy().hasHeightForWidth())
        self.label_ovpm_total_exist_2.setSizePolicy(sizePolicy1)
        self.label_ovpm_total_exist_2.setMinimumSize(QSize(100, 0))
        self.label_ovpm_total_exist_2.setMaximumSize(QSize(200, 16777215))
        self.label_ovpm_total_exist_2.setStyleSheet(u"QLabel {\n"
"background-color:brown;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_9.addWidget(self.label_ovpm_total_exist_2, 2, 1, 1, 1)

        self.label_ovpm_total_item_not_exist_2 = QLabel(self.tab_collection)
        self.label_ovpm_total_item_not_exist_2.setObjectName(u"label_ovpm_total_item_not_exist_2")
        sizePolicy1.setHeightForWidth(self.label_ovpm_total_item_not_exist_2.sizePolicy().hasHeightForWidth())
        self.label_ovpm_total_item_not_exist_2.setSizePolicy(sizePolicy1)
        self.label_ovpm_total_item_not_exist_2.setMinimumSize(QSize(200, 0))
        self.label_ovpm_total_item_not_exist_2.setMaximumSize(QSize(200, 16777215))
        self.label_ovpm_total_item_not_exist_2.setStyleSheet(u"QLabel {\n"
"background-color:yellow;\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_9.addWidget(self.label_ovpm_total_item_not_exist_2, 0, 1, 1, 1)

        self.label_ovpm_total_ready_2 = QLabel(self.tab_collection)
        self.label_ovpm_total_ready_2.setObjectName(u"label_ovpm_total_ready_2")
        self.label_ovpm_total_ready_2.setStyleSheet(u"QLabel {\n"
"background-color:rgb(173, 216, 230);\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_9.addWidget(self.label_ovpm_total_ready_2, 0, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.tab_collection)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_9.addWidget(self.pushButton_9, 4, 0, 1, 1)

        self.line_8 = QFrame(self.tab_collection)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_8, 3, 0, 1, 4)

        self.pushButton_incoming_clear = QPushButton(self.tab_collection)
        self.pushButton_incoming_clear.setObjectName(u"pushButton_incoming_clear")

        self.gridLayout_9.addWidget(self.pushButton_incoming_clear, 1, 3, 1, 1)

        self.tabWidget.addTab(self.tab_collection, "")
        self.tab_disbursement = QWidget()
        self.tab_disbursement.setObjectName(u"tab_disbursement")
        self.gridLayout_5 = QGridLayout(self.tab_disbursement)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.line_4 = QFrame(self.tab_disbursement)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_4, 3, 0, 1, 4)

        self.label_ovpm_total_item_not_exist = QLabel(self.tab_disbursement)
        self.label_ovpm_total_item_not_exist.setObjectName(u"label_ovpm_total_item_not_exist")
        sizePolicy1.setHeightForWidth(self.label_ovpm_total_item_not_exist.sizePolicy().hasHeightForWidth())
        self.label_ovpm_total_item_not_exist.setSizePolicy(sizePolicy1)
        self.label_ovpm_total_item_not_exist.setMinimumSize(QSize(200, 0))
        self.label_ovpm_total_item_not_exist.setMaximumSize(QSize(200, 16777215))
        self.label_ovpm_total_item_not_exist.setStyleSheet(u"QLabel {\n"
"background-color:yellow;\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_5.addWidget(self.label_ovpm_total_item_not_exist, 0, 1, 1, 1)

        self.tableWidget_ovpm = QTableWidget(self.tab_disbursement)
        if (self.tableWidget_ovpm.columnCount() < 24):
            self.tableWidget_ovpm.setColumnCount(24)
        __qtablewidgetitem213 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(0, __qtablewidgetitem213)
        __qtablewidgetitem214 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(1, __qtablewidgetitem214)
        __qtablewidgetitem215 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(2, __qtablewidgetitem215)
        __qtablewidgetitem216 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(3, __qtablewidgetitem216)
        __qtablewidgetitem217 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(4, __qtablewidgetitem217)
        __qtablewidgetitem218 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(5, __qtablewidgetitem218)
        __qtablewidgetitem219 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(6, __qtablewidgetitem219)
        __qtablewidgetitem220 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(7, __qtablewidgetitem220)
        __qtablewidgetitem221 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(8, __qtablewidgetitem221)
        __qtablewidgetitem222 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(9, __qtablewidgetitem222)
        __qtablewidgetitem223 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(10, __qtablewidgetitem223)
        __qtablewidgetitem224 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(11, __qtablewidgetitem224)
        __qtablewidgetitem225 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(12, __qtablewidgetitem225)
        __qtablewidgetitem226 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(13, __qtablewidgetitem226)
        __qtablewidgetitem227 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(14, __qtablewidgetitem227)
        __qtablewidgetitem228 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(15, __qtablewidgetitem228)
        __qtablewidgetitem229 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(16, __qtablewidgetitem229)
        __qtablewidgetitem230 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(17, __qtablewidgetitem230)
        __qtablewidgetitem231 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(18, __qtablewidgetitem231)
        __qtablewidgetitem232 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(19, __qtablewidgetitem232)
        __qtablewidgetitem233 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(20, __qtablewidgetitem233)
        __qtablewidgetitem234 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(21, __qtablewidgetitem234)
        __qtablewidgetitem235 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(22, __qtablewidgetitem235)
        __qtablewidgetitem236 = QTableWidgetItem()
        self.tableWidget_ovpm.setHorizontalHeaderItem(23, __qtablewidgetitem236)
        self.tableWidget_ovpm.setObjectName(u"tableWidget_ovpm")
        self.tableWidget_ovpm.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_5.addWidget(self.tableWidget_ovpm, 7, 0, 1, 4)

        self.label_ovpm_total_bp_not_exist = QLabel(self.tab_disbursement)
        self.label_ovpm_total_bp_not_exist.setObjectName(u"label_ovpm_total_bp_not_exist")
        sizePolicy1.setHeightForWidth(self.label_ovpm_total_bp_not_exist.sizePolicy().hasHeightForWidth())
        self.label_ovpm_total_bp_not_exist.setSizePolicy(sizePolicy1)
        self.label_ovpm_total_bp_not_exist.setMinimumSize(QSize(200, 0))
        self.label_ovpm_total_bp_not_exist.setMaximumSize(QSize(200, 16777215))
        self.label_ovpm_total_bp_not_exist.setStyleSheet(u"QLabel {\n"
"background-color:orange;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_5.addWidget(self.label_ovpm_total_bp_not_exist, 1, 0, 1, 1)

        self.label_ovpm_total_exist = QLabel(self.tab_disbursement)
        self.label_ovpm_total_exist.setObjectName(u"label_ovpm_total_exist")
        sizePolicy1.setHeightForWidth(self.label_ovpm_total_exist.sizePolicy().hasHeightForWidth())
        self.label_ovpm_total_exist.setSizePolicy(sizePolicy1)
        self.label_ovpm_total_exist.setMinimumSize(QSize(100, 0))
        self.label_ovpm_total_exist.setMaximumSize(QSize(200, 16777215))
        self.label_ovpm_total_exist.setStyleSheet(u"QLabel {\n"
"background-color:brown;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_5.addWidget(self.label_ovpm_total_exist, 2, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.tab_disbursement)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_5.addWidget(self.lineEdit_5, 4, 1, 1, 1)

        self.label_8 = QLabel(self.tab_disbursement)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMinimumSize(QSize(200, 0))
        self.label_8.setMaximumSize(QSize(200, 16777215))
        self.label_8.setStyleSheet(u"QLabel {\n"
"background-color:green;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_5.addWidget(self.label_8, 1, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.tab_disbursement)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	background-color: #f3d162\n"
"}")

        self.gridLayout_5.addWidget(self.pushButton_5, 4, 0, 1, 1)

        self.label_7 = QLabel(self.tab_disbursement)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setMinimumSize(QSize(100, 0))
        self.label_7.setMaximumSize(QSize(200, 16777215))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet(u"QLabel {\n"
"background-color:red;\n"
"color:white;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.pushButton_show_outgoing = QPushButton(self.tab_disbursement)
        self.pushButton_show_outgoing.setObjectName(u"pushButton_show_outgoing")

        self.gridLayout_5.addWidget(self.pushButton_show_outgoing, 0, 3, 1, 1)

        self.pushButton_upload_outgoing = QPushButton(self.tab_disbursement)
        self.pushButton_upload_outgoing.setObjectName(u"pushButton_upload_outgoing")
        self.pushButton_upload_outgoing.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_5.addWidget(self.pushButton_upload_outgoing, 8, 0, 1, 1)

        self.label_ovpm_total_ready = QLabel(self.tab_disbursement)
        self.label_ovpm_total_ready.setObjectName(u"label_ovpm_total_ready")
        self.label_ovpm_total_ready.setStyleSheet(u"QLabel {\n"
"background-color:rgb(173, 216, 230);\n"
"color:black;\n"
"font-weight: bold\n"
"}")

        self.gridLayout_5.addWidget(self.label_ovpm_total_ready, 0, 2, 1, 1)

        self.pushButton_outgoing_clear = QPushButton(self.tab_disbursement)
        self.pushButton_outgoing_clear.setObjectName(u"pushButton_outgoing_clear")

        self.gridLayout_5.addWidget(self.pushButton_outgoing_clear, 1, 3, 1, 1)

        self.tabWidget.addTab(self.tab_disbursement, "")

        self.gridLayout.addWidget(self.tabWidget, 5, 0, 1, 7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 941, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Transaction Uploader", None))
        self.pushButton_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_grpo_total_exist.setText(QCoreApplication.translate("MainWindow", u"Doc. Already Exist: 0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Required Fields: 0", None))
        ___qtablewidgetitem = self.tableWidget_grpo.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem1 = self.tableWidget_grpo.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"DT", None));
        ___qtablewidgetitem2 = self.tableWidget_grpo.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Posting Date", None));
        ___qtablewidgetitem3 = self.tableWidget_grpo.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Document Date", None));
        ___qtablewidgetitem4 = self.tableWidget_grpo.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Due Date", None));
        ___qtablewidgetitem5 = self.tableWidget_grpo.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Ref. No.", None));
        ___qtablewidgetitem6 = self.tableWidget_grpo.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"BP Code", None));
        ___qtablewidgetitem7 = self.tableWidget_grpo.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"BP Name", None));
        ___qtablewidgetitem8 = self.tableWidget_grpo.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Ctrl Acct", None));
        ___qtablewidgetitem9 = self.tableWidget_grpo.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Unit", None));
        ___qtablewidgetitem10 = self.tableWidget_grpo.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Unit Name", None));
        ___qtablewidgetitem11 = self.tableWidget_grpo.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Doc. No.", None));
        ___qtablewidgetitem12 = self.tableWidget_grpo.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Remarks", None));
        ___qtablewidgetitem13 = self.tableWidget_grpo.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Intsr. No", None));
        ___qtablewidgetitem14 = self.tableWidget_grpo.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Cont. No.", None));
        ___qtablewidgetitem15 = self.tableWidget_grpo.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Clrng Doc.", None));
        ___qtablewidgetitem16 = self.tableWidget_grpo.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Clrng DT", None));
        ___qtablewidgetitem17 = self.tableWidget_grpo.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"2nd Sub Acct", None));
        ___qtablewidgetitem18 = self.tableWidget_grpo.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Line No.", None));
        ___qtablewidgetitem19 = self.tableWidget_grpo.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Currency", None));
        ___qtablewidgetitem20 = self.tableWidget_grpo.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Trans Amount", None));
        ___qtablewidgetitem21 = self.tableWidget_grpo.horizontalHeaderItem(21)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Line Total", None));
        ___qtablewidgetitem22 = self.tableWidget_grpo.horizontalHeaderItem(22)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Item Code", None));
        ___qtablewidgetitem23 = self.tableWidget_grpo.horizontalHeaderItem(23)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Vat Group", None));
        ___qtablewidgetitem24 = self.tableWidget_grpo.horizontalHeaderItem(24)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem25 = self.tableWidget_grpo.horizontalHeaderItem(25)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"UoM Code", None));
        self.pushButton_upload_grpo.setText(QCoreApplication.translate("MainWindow", u"Post", None))
        self.label_grpo_total_bp_not_exist.setText(QCoreApplication.translate("MainWindow", u"BP Does Not Exist: 0", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"GL Does Not Exist: 0", None))
        self.pushButton_show_grpo.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_grpo_total_ready.setText(QCoreApplication.translate("MainWindow", u"GRPO READY TO POST:", None))
        self.label_grpo_total_item_not_exist.setText(QCoreApplication.translate("MainWindow", u"Item Does Not Exist: 0", None))
        self.pushButton_grpo_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_grpo), QCoreApplication.translate("MainWindow", u"GRPO", None))
        ___qtablewidgetitem26 = self.tableWidget_apinvoice.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem27 = self.tableWidget_apinvoice.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"DT", None));
        ___qtablewidgetitem28 = self.tableWidget_apinvoice.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Posting Date", None));
        ___qtablewidgetitem29 = self.tableWidget_apinvoice.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Document Date", None));
        ___qtablewidgetitem30 = self.tableWidget_apinvoice.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Due Date", None));
        ___qtablewidgetitem31 = self.tableWidget_apinvoice.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Ref. No.", None));
        ___qtablewidgetitem32 = self.tableWidget_apinvoice.horizontalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"BP Code", None));
        ___qtablewidgetitem33 = self.tableWidget_apinvoice.horizontalHeaderItem(7)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"BP Name", None));
        ___qtablewidgetitem34 = self.tableWidget_apinvoice.horizontalHeaderItem(8)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Ctrl Acct", None));
        ___qtablewidgetitem35 = self.tableWidget_apinvoice.horizontalHeaderItem(9)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Unit", None));
        ___qtablewidgetitem36 = self.tableWidget_apinvoice.horizontalHeaderItem(10)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Unit Name", None));
        ___qtablewidgetitem37 = self.tableWidget_apinvoice.horizontalHeaderItem(11)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Doc. No.", None));
        ___qtablewidgetitem38 = self.tableWidget_apinvoice.horizontalHeaderItem(12)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Remarks", None));
        ___qtablewidgetitem39 = self.tableWidget_apinvoice.horizontalHeaderItem(13)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Intsr. No", None));
        ___qtablewidgetitem40 = self.tableWidget_apinvoice.horizontalHeaderItem(14)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Cont. No.", None));
        ___qtablewidgetitem41 = self.tableWidget_apinvoice.horizontalHeaderItem(15)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Clrng Doc.", None));
        ___qtablewidgetitem42 = self.tableWidget_apinvoice.horizontalHeaderItem(16)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Clrng DT", None));
        ___qtablewidgetitem43 = self.tableWidget_apinvoice.horizontalHeaderItem(17)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"2nd Sub Acct", None));
        ___qtablewidgetitem44 = self.tableWidget_apinvoice.horizontalHeaderItem(18)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Line No.", None));
        ___qtablewidgetitem45 = self.tableWidget_apinvoice.horizontalHeaderItem(19)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Currency", None));
        ___qtablewidgetitem46 = self.tableWidget_apinvoice.horizontalHeaderItem(20)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Trans Amount", None));
        ___qtablewidgetitem47 = self.tableWidget_apinvoice.horizontalHeaderItem(21)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Line Total", None));
        ___qtablewidgetitem48 = self.tableWidget_apinvoice.horizontalHeaderItem(22)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Item Code", None));
        ___qtablewidgetitem49 = self.tableWidget_apinvoice.horizontalHeaderItem(23)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Vat Group", None));
        ___qtablewidgetitem50 = self.tableWidget_apinvoice.horizontalHeaderItem(24)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"WTax Liable", None));
        ___qtablewidgetitem51 = self.tableWidget_apinvoice.horizontalHeaderItem(25)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem52 = self.tableWidget_apinvoice.horizontalHeaderItem(26)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"UoM Code", None));
        ___qtablewidgetitem53 = self.tableWidget_apinvoice.horizontalHeaderItem(27)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"WT Code 1", None));
        ___qtablewidgetitem54 = self.tableWidget_apinvoice.horizontalHeaderItem(28)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"WT Code 2", None));
        ___qtablewidgetitem55 = self.tableWidget_apinvoice.horizontalHeaderItem(29)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"WT Amount", None));
        ___qtablewidgetitem56 = self.tableWidget_apinvoice.horizontalHeaderItem(30)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"GRPO Doc. Entry", None));
        self.label_apinvoice_total_bp_not_exist.setText(QCoreApplication.translate("MainWindow", u"BP Does Not Exist:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Required Fields: ", None))
        self.label_apinvoice_total_exist.setText(QCoreApplication.translate("MainWindow", u"Doc. Already Exist:", None))
        self.label_apinvoice_total_item_not_exist.setText(QCoreApplication.translate("MainWindow", u"Item Does Not Exist:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.pushButton_upload_apinvoice.setText(QCoreApplication.translate("MainWindow", u"Post", None))
        self.pushButton_show_apinvoice.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"GL Does Not Exist:", None))
        self.label_apinvoice_total_ready.setText(QCoreApplication.translate("MainWindow", u"AP INVOICE READY TO POST:", None))
        self.pushButton_apinvoice_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_apinvoice), QCoreApplication.translate("MainWindow", u"AP Invoice", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Required Fields: ", None))
        ___qtablewidgetitem57 = self.tableWidget_apcm.horizontalHeaderItem(0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem58 = self.tableWidget_apcm.horizontalHeaderItem(1)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"DT", None));
        ___qtablewidgetitem59 = self.tableWidget_apcm.horizontalHeaderItem(2)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Posting Date", None));
        ___qtablewidgetitem60 = self.tableWidget_apcm.horizontalHeaderItem(3)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Document Date", None));
        ___qtablewidgetitem61 = self.tableWidget_apcm.horizontalHeaderItem(4)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Due Date", None));
        ___qtablewidgetitem62 = self.tableWidget_apcm.horizontalHeaderItem(5)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Ref. No.", None));
        ___qtablewidgetitem63 = self.tableWidget_apcm.horizontalHeaderItem(6)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"BP Code", None));
        ___qtablewidgetitem64 = self.tableWidget_apcm.horizontalHeaderItem(7)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"BP Name", None));
        ___qtablewidgetitem65 = self.tableWidget_apcm.horizontalHeaderItem(8)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Ctrl Acct", None));
        ___qtablewidgetitem66 = self.tableWidget_apcm.horizontalHeaderItem(9)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Unit", None));
        ___qtablewidgetitem67 = self.tableWidget_apcm.horizontalHeaderItem(10)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Unit Name", None));
        ___qtablewidgetitem68 = self.tableWidget_apcm.horizontalHeaderItem(11)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Doc. No.", None));
        ___qtablewidgetitem69 = self.tableWidget_apcm.horizontalHeaderItem(12)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Remarks", None));
        ___qtablewidgetitem70 = self.tableWidget_apcm.horizontalHeaderItem(13)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Intsr. No", None));
        ___qtablewidgetitem71 = self.tableWidget_apcm.horizontalHeaderItem(14)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Cont. No.", None));
        ___qtablewidgetitem72 = self.tableWidget_apcm.horizontalHeaderItem(15)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Clrng Doc.", None));
        ___qtablewidgetitem73 = self.tableWidget_apcm.horizontalHeaderItem(16)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Clrng DT", None));
        ___qtablewidgetitem74 = self.tableWidget_apcm.horizontalHeaderItem(17)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"2nd Sub Acct", None));
        ___qtablewidgetitem75 = self.tableWidget_apcm.horizontalHeaderItem(18)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Line No.", None));
        ___qtablewidgetitem76 = self.tableWidget_apcm.horizontalHeaderItem(19)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Currency", None));
        ___qtablewidgetitem77 = self.tableWidget_apcm.horizontalHeaderItem(20)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Trans Amount", None));
        ___qtablewidgetitem78 = self.tableWidget_apcm.horizontalHeaderItem(21)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"Line Total", None));
        ___qtablewidgetitem79 = self.tableWidget_apcm.horizontalHeaderItem(22)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"Item Code", None));
        ___qtablewidgetitem80 = self.tableWidget_apcm.horizontalHeaderItem(23)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Vat Group", None));
        ___qtablewidgetitem81 = self.tableWidget_apcm.horizontalHeaderItem(24)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem82 = self.tableWidget_apcm.horizontalHeaderItem(25)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"UoM Code", None));
        self.pushButton_show_apcm.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.pushButton_upload_apcm.setText(QCoreApplication.translate("MainWindow", u"Post", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"GL Does Not Exist:", None))
        self.label_apcm_total_bp_not_exist.setText(QCoreApplication.translate("MainWindow", u"BP Does Not Exist:", None))
        self.label_apcm_total_item_not_exist.setText(QCoreApplication.translate("MainWindow", u"Item Does Not Exist:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_apcm_total_exist.setText(QCoreApplication.translate("MainWindow", u"Doc. Already Exist:", None))
        self.label_apcm_total_ready.setText(QCoreApplication.translate("MainWindow", u"AP CREDIT MEMO READY TO POST:", None))
        self.pushButton_apcm_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_creditmemo), QCoreApplication.translate("MainWindow", u"Credit Memo", None))
        self.label_arinvoice_total_bp_not_exist.setText(QCoreApplication.translate("MainWindow", u"BP Does Not Exist:", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.pushButton_upload_arinvoice.setText(QCoreApplication.translate("MainWindow", u"Post", None))
        ___qtablewidgetitem83 = self.tableWidget_arinvoice.horizontalHeaderItem(0)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem84 = self.tableWidget_arinvoice.horizontalHeaderItem(1)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"DT", None));
        ___qtablewidgetitem85 = self.tableWidget_arinvoice.horizontalHeaderItem(2)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"Posting Date", None));
        ___qtablewidgetitem86 = self.tableWidget_arinvoice.horizontalHeaderItem(3)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Document Date", None));
        ___qtablewidgetitem87 = self.tableWidget_arinvoice.horizontalHeaderItem(4)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Due Date", None));
        ___qtablewidgetitem88 = self.tableWidget_arinvoice.horizontalHeaderItem(5)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Ref. No.", None));
        ___qtablewidgetitem89 = self.tableWidget_arinvoice.horizontalHeaderItem(6)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"BP Code", None));
        ___qtablewidgetitem90 = self.tableWidget_arinvoice.horizontalHeaderItem(7)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"BP Name", None));
        ___qtablewidgetitem91 = self.tableWidget_arinvoice.horizontalHeaderItem(8)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"Ctrl Acct", None));
        ___qtablewidgetitem92 = self.tableWidget_arinvoice.horizontalHeaderItem(9)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"Unit", None));
        ___qtablewidgetitem93 = self.tableWidget_arinvoice.horizontalHeaderItem(10)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"Unit Name", None));
        ___qtablewidgetitem94 = self.tableWidget_arinvoice.horizontalHeaderItem(11)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"Doc. No.", None));
        ___qtablewidgetitem95 = self.tableWidget_arinvoice.horizontalHeaderItem(12)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"Remarks", None));
        ___qtablewidgetitem96 = self.tableWidget_arinvoice.horizontalHeaderItem(13)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"Intsr. No", None));
        ___qtablewidgetitem97 = self.tableWidget_arinvoice.horizontalHeaderItem(14)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Cont. No.", None));
        ___qtablewidgetitem98 = self.tableWidget_arinvoice.horizontalHeaderItem(15)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"Clrng Doc.", None));
        ___qtablewidgetitem99 = self.tableWidget_arinvoice.horizontalHeaderItem(16)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"Clrng DT", None));
        ___qtablewidgetitem100 = self.tableWidget_arinvoice.horizontalHeaderItem(17)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"2nd Sub Acct", None));
        ___qtablewidgetitem101 = self.tableWidget_arinvoice.horizontalHeaderItem(18)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"Line No.", None));
        ___qtablewidgetitem102 = self.tableWidget_arinvoice.horizontalHeaderItem(19)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"Currency", None));
        ___qtablewidgetitem103 = self.tableWidget_arinvoice.horizontalHeaderItem(20)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"Trans Amount", None));
        ___qtablewidgetitem104 = self.tableWidget_arinvoice.horizontalHeaderItem(21)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"Line Total", None));
        ___qtablewidgetitem105 = self.tableWidget_arinvoice.horizontalHeaderItem(22)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"Item Code", None));
        ___qtablewidgetitem106 = self.tableWidget_arinvoice.horizontalHeaderItem(23)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"Vat Group", None));
        ___qtablewidgetitem107 = self.tableWidget_arinvoice.horizontalHeaderItem(24)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem108 = self.tableWidget_arinvoice.horizontalHeaderItem(25)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"UoM Code", None));
        ___qtablewidgetitem109 = self.tableWidget_arinvoice.horizontalHeaderItem(26)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"SAP DocEntry", None));
        self.label_arinvoice_total_item_not_exist.setText(QCoreApplication.translate("MainWindow", u"Item Does Not Exist:", None))
        self.label_arinvoice_total_required_fields.setText(QCoreApplication.translate("MainWindow", u"Required Fields: ", None))
        self.pushButton_show_arinvoice.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"GL Does Not Exist:", None))
        self.label_arinvoice_total_exist.setText(QCoreApplication.translate("MainWindow", u"Doc. Already Exist:", None))
        self.label_arinvoice_total_ready.setText(QCoreApplication.translate("MainWindow", u"AR INVOICES READY TO POST:", None))
        self.pushButton_arinvoice_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_arinvoice), QCoreApplication.translate("MainWindow", u"AR Invoice", None))
        self.label_arinvoice_total_required_fields_2.setText(QCoreApplication.translate("MainWindow", u"Required Fields: ", None))
        self.label_arinvoice_total_item_not_exist_2.setText(QCoreApplication.translate("MainWindow", u"Item Does Not Exist:", None))
        self.label_arinvoice_total_ready_2.setText(QCoreApplication.translate("MainWindow", u"BILLING STATEMENT READY TO POST:", None))
        self.pushButton_show_arinvoice_2.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_arinvoice_total_bp_not_exist_2.setText(QCoreApplication.translate("MainWindow", u"BP Does Not Exist:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"GL Does Not Exist:", None))
        self.label_arinvoice_total_exist_2.setText(QCoreApplication.translate("MainWindow", u"Doc. Already Exist:", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        ___qtablewidgetitem110 = self.tableWidget_arinvoice_2.horizontalHeaderItem(0)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem111 = self.tableWidget_arinvoice_2.horizontalHeaderItem(1)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"DT", None));
        ___qtablewidgetitem112 = self.tableWidget_arinvoice_2.horizontalHeaderItem(2)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"Posting Date", None));
        ___qtablewidgetitem113 = self.tableWidget_arinvoice_2.horizontalHeaderItem(3)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"Document Date", None));
        ___qtablewidgetitem114 = self.tableWidget_arinvoice_2.horizontalHeaderItem(4)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"Due Date", None));
        ___qtablewidgetitem115 = self.tableWidget_arinvoice_2.horizontalHeaderItem(5)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"Ref. No.", None));
        ___qtablewidgetitem116 = self.tableWidget_arinvoice_2.horizontalHeaderItem(6)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"BP Code", None));
        ___qtablewidgetitem117 = self.tableWidget_arinvoice_2.horizontalHeaderItem(7)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"BP Name", None));
        ___qtablewidgetitem118 = self.tableWidget_arinvoice_2.horizontalHeaderItem(8)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"Ctrl Acct", None));
        ___qtablewidgetitem119 = self.tableWidget_arinvoice_2.horizontalHeaderItem(9)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"Unit", None));
        ___qtablewidgetitem120 = self.tableWidget_arinvoice_2.horizontalHeaderItem(10)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"Unit Name", None));
        ___qtablewidgetitem121 = self.tableWidget_arinvoice_2.horizontalHeaderItem(11)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"Doc. No.", None));
        ___qtablewidgetitem122 = self.tableWidget_arinvoice_2.horizontalHeaderItem(12)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"Remarks", None));
        ___qtablewidgetitem123 = self.tableWidget_arinvoice_2.horizontalHeaderItem(13)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"Intsr. No", None));
        ___qtablewidgetitem124 = self.tableWidget_arinvoice_2.horizontalHeaderItem(14)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"Cont. No.", None));
        ___qtablewidgetitem125 = self.tableWidget_arinvoice_2.horizontalHeaderItem(15)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"Clrng Doc.", None));
        ___qtablewidgetitem126 = self.tableWidget_arinvoice_2.horizontalHeaderItem(16)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"Clrng DT", None));
        ___qtablewidgetitem127 = self.tableWidget_arinvoice_2.horizontalHeaderItem(17)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"2nd Sub Acct", None));
        ___qtablewidgetitem128 = self.tableWidget_arinvoice_2.horizontalHeaderItem(18)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("MainWindow", u"Line No.", None));
        ___qtablewidgetitem129 = self.tableWidget_arinvoice_2.horizontalHeaderItem(19)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("MainWindow", u"Currency", None));
        ___qtablewidgetitem130 = self.tableWidget_arinvoice_2.horizontalHeaderItem(20)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("MainWindow", u"Trans Amount", None));
        ___qtablewidgetitem131 = self.tableWidget_arinvoice_2.horizontalHeaderItem(21)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("MainWindow", u"Line Total", None));
        ___qtablewidgetitem132 = self.tableWidget_arinvoice_2.horizontalHeaderItem(22)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("MainWindow", u"Item Code", None));
        ___qtablewidgetitem133 = self.tableWidget_arinvoice_2.horizontalHeaderItem(23)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("MainWindow", u"Vat Group", None));
        ___qtablewidgetitem134 = self.tableWidget_arinvoice_2.horizontalHeaderItem(24)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem135 = self.tableWidget_arinvoice_2.horizontalHeaderItem(25)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("MainWindow", u"UoM Code", None));
        ___qtablewidgetitem136 = self.tableWidget_arinvoice_2.horizontalHeaderItem(26)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("MainWindow", u"Rate", None));
        ___qtablewidgetitem137 = self.tableWidget_arinvoice_2.horizontalHeaderItem(27)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("MainWindow", u"SAP DocEntry", None));
        self.pushButton_upload_arinvoice_2.setText(QCoreApplication.translate("MainWindow", u"Post", None))
        self.pushButton_arinvoice_clear_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_billingstatement), QCoreApplication.translate("MainWindow", u"Billing Statement", None))
        self.pushButton_show_arcm.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Required Fields: ", None))
        self.label_arcm_total_bp_not_exist.setText(QCoreApplication.translate("MainWindow", u"BP Does Not Exist:", None))
        self.label_arcm_total_exist.setText(QCoreApplication.translate("MainWindow", u"Doc. Already Exist:", None))
        ___qtablewidgetitem138 = self.tableWidget_arcm.horizontalHeaderItem(0)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem139 = self.tableWidget_arcm.horizontalHeaderItem(1)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("MainWindow", u"DT", None));
        ___qtablewidgetitem140 = self.tableWidget_arcm.horizontalHeaderItem(2)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("MainWindow", u"Posting Date", None));
        ___qtablewidgetitem141 = self.tableWidget_arcm.horizontalHeaderItem(3)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("MainWindow", u"Document Date", None));
        ___qtablewidgetitem142 = self.tableWidget_arcm.horizontalHeaderItem(4)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("MainWindow", u"Due Date", None));
        ___qtablewidgetitem143 = self.tableWidget_arcm.horizontalHeaderItem(5)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("MainWindow", u"Ref. No.", None));
        ___qtablewidgetitem144 = self.tableWidget_arcm.horizontalHeaderItem(6)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("MainWindow", u"BP Code", None));
        ___qtablewidgetitem145 = self.tableWidget_arcm.horizontalHeaderItem(7)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("MainWindow", u"BP Name", None));
        ___qtablewidgetitem146 = self.tableWidget_arcm.horizontalHeaderItem(8)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("MainWindow", u"Ctrl Acct", None));
        ___qtablewidgetitem147 = self.tableWidget_arcm.horizontalHeaderItem(9)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("MainWindow", u"Unit", None));
        ___qtablewidgetitem148 = self.tableWidget_arcm.horizontalHeaderItem(10)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("MainWindow", u"Unit Name", None));
        ___qtablewidgetitem149 = self.tableWidget_arcm.horizontalHeaderItem(11)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("MainWindow", u"Doc. No.", None));
        ___qtablewidgetitem150 = self.tableWidget_arcm.horizontalHeaderItem(12)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("MainWindow", u"Remarks", None));
        ___qtablewidgetitem151 = self.tableWidget_arcm.horizontalHeaderItem(13)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("MainWindow", u"Intsr. No", None));
        ___qtablewidgetitem152 = self.tableWidget_arcm.horizontalHeaderItem(14)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("MainWindow", u"Cont. No.", None));
        ___qtablewidgetitem153 = self.tableWidget_arcm.horizontalHeaderItem(15)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("MainWindow", u"Clrng Doc.", None));
        ___qtablewidgetitem154 = self.tableWidget_arcm.horizontalHeaderItem(16)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("MainWindow", u"Clrng DT", None));
        ___qtablewidgetitem155 = self.tableWidget_arcm.horizontalHeaderItem(17)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("MainWindow", u"2nd Sub Acct", None));
        ___qtablewidgetitem156 = self.tableWidget_arcm.horizontalHeaderItem(18)
        ___qtablewidgetitem156.setText(QCoreApplication.translate("MainWindow", u"Line No.", None));
        ___qtablewidgetitem157 = self.tableWidget_arcm.horizontalHeaderItem(19)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("MainWindow", u"Currency", None));
        ___qtablewidgetitem158 = self.tableWidget_arcm.horizontalHeaderItem(20)
        ___qtablewidgetitem158.setText(QCoreApplication.translate("MainWindow", u"Trans Amount", None));
        ___qtablewidgetitem159 = self.tableWidget_arcm.horizontalHeaderItem(21)
        ___qtablewidgetitem159.setText(QCoreApplication.translate("MainWindow", u"Line Total", None));
        ___qtablewidgetitem160 = self.tableWidget_arcm.horizontalHeaderItem(22)
        ___qtablewidgetitem160.setText(QCoreApplication.translate("MainWindow", u"Item Code", None));
        ___qtablewidgetitem161 = self.tableWidget_arcm.horizontalHeaderItem(23)
        ___qtablewidgetitem161.setText(QCoreApplication.translate("MainWindow", u"Vat Group", None));
        ___qtablewidgetitem162 = self.tableWidget_arcm.horizontalHeaderItem(24)
        ___qtablewidgetitem162.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem163 = self.tableWidget_arcm.horizontalHeaderItem(25)
        ___qtablewidgetitem163.setText(QCoreApplication.translate("MainWindow", u"UoM Code", None));
        self.pushButton_upload_arcm.setText(QCoreApplication.translate("MainWindow", u"Post", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_arcm_total_item_not_exist.setText(QCoreApplication.translate("MainWindow", u"Item Does Not Exist:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"GL Does Not Exist:", None))
        self.label_arcm_total_ready.setText(QCoreApplication.translate("MainWindow", u"AR CREDIT MEMO READY TO POST:", None))
        self.pushButton_arcm_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_debitmemo), QCoreApplication.translate("MainWindow", u"Debit Memo", None))
        self.label_ojdt_total_required_fields.setText(QCoreApplication.translate("MainWindow", u"Required Fields: 0", None))
        self.label_ojdt_total_item_not_exist.setText(QCoreApplication.translate("MainWindow", u"Item Does Not Exist: 0", None))
        self.label_ojdt_total_ready.setText(QCoreApplication.translate("MainWindow", u"JE READY TO POST:", None))
        self.pushButton_show_ojdt.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_ojdt_total_bp_not_exist.setText(QCoreApplication.translate("MainWindow", u"BP Does Not Exist: 0", None))
        self.label_ojdt_total_gl_not_exist.setText(QCoreApplication.translate("MainWindow", u"GL Does Not Exist: 0", None))
        self.label_ojdt_total_ready_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_ojdt_total_exist.setText(QCoreApplication.translate("MainWindow", u"Doc. Already Exist: 0", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        ___qtablewidgetitem164 = self.tableWidget_ojdt.horizontalHeaderItem(0)
        ___qtablewidgetitem164.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem165 = self.tableWidget_ojdt.horizontalHeaderItem(1)
        ___qtablewidgetitem165.setText(QCoreApplication.translate("MainWindow", u"DT", None));
        ___qtablewidgetitem166 = self.tableWidget_ojdt.horizontalHeaderItem(2)
        ___qtablewidgetitem166.setText(QCoreApplication.translate("MainWindow", u"Posting Date", None));
        ___qtablewidgetitem167 = self.tableWidget_ojdt.horizontalHeaderItem(3)
        ___qtablewidgetitem167.setText(QCoreApplication.translate("MainWindow", u"Document Date", None));
        ___qtablewidgetitem168 = self.tableWidget_ojdt.horizontalHeaderItem(4)
        ___qtablewidgetitem168.setText(QCoreApplication.translate("MainWindow", u"Due Date", None));
        ___qtablewidgetitem169 = self.tableWidget_ojdt.horizontalHeaderItem(5)
        ___qtablewidgetitem169.setText(QCoreApplication.translate("MainWindow", u"Ref. No.", None));
        ___qtablewidgetitem170 = self.tableWidget_ojdt.horizontalHeaderItem(6)
        ___qtablewidgetitem170.setText(QCoreApplication.translate("MainWindow", u"BP Code", None));
        ___qtablewidgetitem171 = self.tableWidget_ojdt.horizontalHeaderItem(7)
        ___qtablewidgetitem171.setText(QCoreApplication.translate("MainWindow", u"BP Name", None));
        ___qtablewidgetitem172 = self.tableWidget_ojdt.horizontalHeaderItem(8)
        ___qtablewidgetitem172.setText(QCoreApplication.translate("MainWindow", u"Ctrl Acct", None));
        ___qtablewidgetitem173 = self.tableWidget_ojdt.horizontalHeaderItem(9)
        ___qtablewidgetitem173.setText(QCoreApplication.translate("MainWindow", u"Unit", None));
        ___qtablewidgetitem174 = self.tableWidget_ojdt.horizontalHeaderItem(10)
        ___qtablewidgetitem174.setText(QCoreApplication.translate("MainWindow", u"Unit Name", None));
        ___qtablewidgetitem175 = self.tableWidget_ojdt.horizontalHeaderItem(11)
        ___qtablewidgetitem175.setText(QCoreApplication.translate("MainWindow", u"Doc. No.", None));
        ___qtablewidgetitem176 = self.tableWidget_ojdt.horizontalHeaderItem(12)
        ___qtablewidgetitem176.setText(QCoreApplication.translate("MainWindow", u"Remarks", None));
        ___qtablewidgetitem177 = self.tableWidget_ojdt.horizontalHeaderItem(13)
        ___qtablewidgetitem177.setText(QCoreApplication.translate("MainWindow", u"Intsr. No", None));
        ___qtablewidgetitem178 = self.tableWidget_ojdt.horizontalHeaderItem(14)
        ___qtablewidgetitem178.setText(QCoreApplication.translate("MainWindow", u"Cont. No.", None));
        ___qtablewidgetitem179 = self.tableWidget_ojdt.horizontalHeaderItem(15)
        ___qtablewidgetitem179.setText(QCoreApplication.translate("MainWindow", u"Clrng Doc.", None));
        ___qtablewidgetitem180 = self.tableWidget_ojdt.horizontalHeaderItem(16)
        ___qtablewidgetitem180.setText(QCoreApplication.translate("MainWindow", u"Clrng DT", None));
        ___qtablewidgetitem181 = self.tableWidget_ojdt.horizontalHeaderItem(17)
        ___qtablewidgetitem181.setText(QCoreApplication.translate("MainWindow", u"2nd Sub Acct", None));
        ___qtablewidgetitem182 = self.tableWidget_ojdt.horizontalHeaderItem(18)
        ___qtablewidgetitem182.setText(QCoreApplication.translate("MainWindow", u"Line No.", None));
        ___qtablewidgetitem183 = self.tableWidget_ojdt.horizontalHeaderItem(19)
        ___qtablewidgetitem183.setText(QCoreApplication.translate("MainWindow", u"Currency", None));
        ___qtablewidgetitem184 = self.tableWidget_ojdt.horizontalHeaderItem(20)
        ___qtablewidgetitem184.setText(QCoreApplication.translate("MainWindow", u"Trans Amount", None));
        ___qtablewidgetitem185 = self.tableWidget_ojdt.horizontalHeaderItem(21)
        ___qtablewidgetitem185.setText(QCoreApplication.translate("MainWindow", u"Line Total", None));
        ___qtablewidgetitem186 = self.tableWidget_ojdt.horizontalHeaderItem(22)
        ___qtablewidgetitem186.setText(QCoreApplication.translate("MainWindow", u"Vat Group", None));
        ___qtablewidgetitem187 = self.tableWidget_ojdt.horizontalHeaderItem(23)
        ___qtablewidgetitem187.setText(QCoreApplication.translate("MainWindow", u"DR / CR", None));
        self.pushButton_upload_ojdt.setText(QCoreApplication.translate("MainWindow", u"Post", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_journalentry), QCoreApplication.translate("MainWindow", u"Journal Entry", None))
        self.pushButton_show_outgoing_2.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.pushButton_upload_outgoing_2.setText(QCoreApplication.translate("MainWindow", u"Post", None))
        self.label_ovpm_total_bp_not_exist_2.setText(QCoreApplication.translate("MainWindow", u"BP Does Not Exist:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"GL Does Not Exist:", None))
        ___qtablewidgetitem188 = self.tableWidget_ovpm_2.horizontalHeaderItem(0)
        ___qtablewidgetitem188.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem189 = self.tableWidget_ovpm_2.horizontalHeaderItem(1)
        ___qtablewidgetitem189.setText(QCoreApplication.translate("MainWindow", u"DT", None));
        ___qtablewidgetitem190 = self.tableWidget_ovpm_2.horizontalHeaderItem(2)
        ___qtablewidgetitem190.setText(QCoreApplication.translate("MainWindow", u"Posting Date", None));
        ___qtablewidgetitem191 = self.tableWidget_ovpm_2.horizontalHeaderItem(3)
        ___qtablewidgetitem191.setText(QCoreApplication.translate("MainWindow", u"Document Date", None));
        ___qtablewidgetitem192 = self.tableWidget_ovpm_2.horizontalHeaderItem(4)
        ___qtablewidgetitem192.setText(QCoreApplication.translate("MainWindow", u"Due Date", None));
        ___qtablewidgetitem193 = self.tableWidget_ovpm_2.horizontalHeaderItem(5)
        ___qtablewidgetitem193.setText(QCoreApplication.translate("MainWindow", u"Ref. No.", None));
        ___qtablewidgetitem194 = self.tableWidget_ovpm_2.horizontalHeaderItem(6)
        ___qtablewidgetitem194.setText(QCoreApplication.translate("MainWindow", u"BP Code", None));
        ___qtablewidgetitem195 = self.tableWidget_ovpm_2.horizontalHeaderItem(7)
        ___qtablewidgetitem195.setText(QCoreApplication.translate("MainWindow", u"BP Name", None));
        ___qtablewidgetitem196 = self.tableWidget_ovpm_2.horizontalHeaderItem(8)
        ___qtablewidgetitem196.setText(QCoreApplication.translate("MainWindow", u"Ctrl Acct", None));
        ___qtablewidgetitem197 = self.tableWidget_ovpm_2.horizontalHeaderItem(9)
        ___qtablewidgetitem197.setText(QCoreApplication.translate("MainWindow", u"Unit", None));
        ___qtablewidgetitem198 = self.tableWidget_ovpm_2.horizontalHeaderItem(10)
        ___qtablewidgetitem198.setText(QCoreApplication.translate("MainWindow", u"Unit Name", None));
        ___qtablewidgetitem199 = self.tableWidget_ovpm_2.horizontalHeaderItem(11)
        ___qtablewidgetitem199.setText(QCoreApplication.translate("MainWindow", u"Doc. No.", None));
        ___qtablewidgetitem200 = self.tableWidget_ovpm_2.horizontalHeaderItem(12)
        ___qtablewidgetitem200.setText(QCoreApplication.translate("MainWindow", u"Remarks", None));
        ___qtablewidgetitem201 = self.tableWidget_ovpm_2.horizontalHeaderItem(13)
        ___qtablewidgetitem201.setText(QCoreApplication.translate("MainWindow", u"Intsr. No", None));
        ___qtablewidgetitem202 = self.tableWidget_ovpm_2.horizontalHeaderItem(14)
        ___qtablewidgetitem202.setText(QCoreApplication.translate("MainWindow", u"Cont. No.", None));
        ___qtablewidgetitem203 = self.tableWidget_ovpm_2.horizontalHeaderItem(15)
        ___qtablewidgetitem203.setText(QCoreApplication.translate("MainWindow", u"Clrng Doc.", None));
        ___qtablewidgetitem204 = self.tableWidget_ovpm_2.horizontalHeaderItem(16)
        ___qtablewidgetitem204.setText(QCoreApplication.translate("MainWindow", u"Clrng DT", None));
        ___qtablewidgetitem205 = self.tableWidget_ovpm_2.horizontalHeaderItem(17)
        ___qtablewidgetitem205.setText(QCoreApplication.translate("MainWindow", u"2nd Sub Acct", None));
        ___qtablewidgetitem206 = self.tableWidget_ovpm_2.horizontalHeaderItem(18)
        ___qtablewidgetitem206.setText(QCoreApplication.translate("MainWindow", u"Line No.", None));
        ___qtablewidgetitem207 = self.tableWidget_ovpm_2.horizontalHeaderItem(19)
        ___qtablewidgetitem207.setText(QCoreApplication.translate("MainWindow", u"Currency", None));
        ___qtablewidgetitem208 = self.tableWidget_ovpm_2.horizontalHeaderItem(20)
        ___qtablewidgetitem208.setText(QCoreApplication.translate("MainWindow", u"Trans Amount", None));
        ___qtablewidgetitem209 = self.tableWidget_ovpm_2.horizontalHeaderItem(21)
        ___qtablewidgetitem209.setText(QCoreApplication.translate("MainWindow", u"Line Total", None));
        ___qtablewidgetitem210 = self.tableWidget_ovpm_2.horizontalHeaderItem(22)
        ___qtablewidgetitem210.setText(QCoreApplication.translate("MainWindow", u"SAP Doc Entry", None));
        ___qtablewidgetitem211 = self.tableWidget_ovpm_2.horizontalHeaderItem(23)
        ___qtablewidgetitem211.setText(QCoreApplication.translate("MainWindow", u"Obj Type", None));
        ___qtablewidgetitem212 = self.tableWidget_ovpm_2.horizontalHeaderItem(24)
        ___qtablewidgetitem212.setText(QCoreApplication.translate("MainWindow", u"Rate", None));
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Required Fields: ", None))
        self.label_ovpm_total_exist_2.setText(QCoreApplication.translate("MainWindow", u"Doc. Already Exist:", None))
        self.label_ovpm_total_item_not_exist_2.setText(QCoreApplication.translate("MainWindow", u"Item Does Not Exist:", None))
        self.label_ovpm_total_ready_2.setText(QCoreApplication.translate("MainWindow", u"INCOMING PAYMENTS READY TO POST:", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.pushButton_incoming_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_collection), QCoreApplication.translate("MainWindow", u"Collections", None))
        self.label_ovpm_total_item_not_exist.setText(QCoreApplication.translate("MainWindow", u"Item Does Not Exist:", None))
        ___qtablewidgetitem213 = self.tableWidget_ovpm.horizontalHeaderItem(0)
        ___qtablewidgetitem213.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem214 = self.tableWidget_ovpm.horizontalHeaderItem(1)
        ___qtablewidgetitem214.setText(QCoreApplication.translate("MainWindow", u"DT", None));
        ___qtablewidgetitem215 = self.tableWidget_ovpm.horizontalHeaderItem(2)
        ___qtablewidgetitem215.setText(QCoreApplication.translate("MainWindow", u"Posting Date", None));
        ___qtablewidgetitem216 = self.tableWidget_ovpm.horizontalHeaderItem(3)
        ___qtablewidgetitem216.setText(QCoreApplication.translate("MainWindow", u"Document Date", None));
        ___qtablewidgetitem217 = self.tableWidget_ovpm.horizontalHeaderItem(4)
        ___qtablewidgetitem217.setText(QCoreApplication.translate("MainWindow", u"Due Date", None));
        ___qtablewidgetitem218 = self.tableWidget_ovpm.horizontalHeaderItem(5)
        ___qtablewidgetitem218.setText(QCoreApplication.translate("MainWindow", u"Ref. No.", None));
        ___qtablewidgetitem219 = self.tableWidget_ovpm.horizontalHeaderItem(6)
        ___qtablewidgetitem219.setText(QCoreApplication.translate("MainWindow", u"BP Code", None));
        ___qtablewidgetitem220 = self.tableWidget_ovpm.horizontalHeaderItem(7)
        ___qtablewidgetitem220.setText(QCoreApplication.translate("MainWindow", u"BP Name", None));
        ___qtablewidgetitem221 = self.tableWidget_ovpm.horizontalHeaderItem(8)
        ___qtablewidgetitem221.setText(QCoreApplication.translate("MainWindow", u"Ctrl Acct", None));
        ___qtablewidgetitem222 = self.tableWidget_ovpm.horizontalHeaderItem(9)
        ___qtablewidgetitem222.setText(QCoreApplication.translate("MainWindow", u"Unit", None));
        ___qtablewidgetitem223 = self.tableWidget_ovpm.horizontalHeaderItem(10)
        ___qtablewidgetitem223.setText(QCoreApplication.translate("MainWindow", u"Unit Name", None));
        ___qtablewidgetitem224 = self.tableWidget_ovpm.horizontalHeaderItem(11)
        ___qtablewidgetitem224.setText(QCoreApplication.translate("MainWindow", u"Doc. No.", None));
        ___qtablewidgetitem225 = self.tableWidget_ovpm.horizontalHeaderItem(12)
        ___qtablewidgetitem225.setText(QCoreApplication.translate("MainWindow", u"Remarks", None));
        ___qtablewidgetitem226 = self.tableWidget_ovpm.horizontalHeaderItem(13)
        ___qtablewidgetitem226.setText(QCoreApplication.translate("MainWindow", u"Intsr. No", None));
        ___qtablewidgetitem227 = self.tableWidget_ovpm.horizontalHeaderItem(14)
        ___qtablewidgetitem227.setText(QCoreApplication.translate("MainWindow", u"Cont. No.", None));
        ___qtablewidgetitem228 = self.tableWidget_ovpm.horizontalHeaderItem(15)
        ___qtablewidgetitem228.setText(QCoreApplication.translate("MainWindow", u"Clrng Doc.", None));
        ___qtablewidgetitem229 = self.tableWidget_ovpm.horizontalHeaderItem(16)
        ___qtablewidgetitem229.setText(QCoreApplication.translate("MainWindow", u"Clrng DT", None));
        ___qtablewidgetitem230 = self.tableWidget_ovpm.horizontalHeaderItem(17)
        ___qtablewidgetitem230.setText(QCoreApplication.translate("MainWindow", u"2nd Sub Acct", None));
        ___qtablewidgetitem231 = self.tableWidget_ovpm.horizontalHeaderItem(18)
        ___qtablewidgetitem231.setText(QCoreApplication.translate("MainWindow", u"Line No.", None));
        ___qtablewidgetitem232 = self.tableWidget_ovpm.horizontalHeaderItem(19)
        ___qtablewidgetitem232.setText(QCoreApplication.translate("MainWindow", u"Currency", None));
        ___qtablewidgetitem233 = self.tableWidget_ovpm.horizontalHeaderItem(20)
        ___qtablewidgetitem233.setText(QCoreApplication.translate("MainWindow", u"Trans Amount", None));
        ___qtablewidgetitem234 = self.tableWidget_ovpm.horizontalHeaderItem(21)
        ___qtablewidgetitem234.setText(QCoreApplication.translate("MainWindow", u"Line Total", None));
        ___qtablewidgetitem235 = self.tableWidget_ovpm.horizontalHeaderItem(22)
        ___qtablewidgetitem235.setText(QCoreApplication.translate("MainWindow", u"SAP Doc Entry", None));
        ___qtablewidgetitem236 = self.tableWidget_ovpm.horizontalHeaderItem(23)
        ___qtablewidgetitem236.setText(QCoreApplication.translate("MainWindow", u"Obj Type", None));
        self.label_ovpm_total_bp_not_exist.setText(QCoreApplication.translate("MainWindow", u"BP Does Not Exist:", None))
        self.label_ovpm_total_exist.setText(QCoreApplication.translate("MainWindow", u"Doc. Already Exist:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"GL Does Not Exist:", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Required Fields: ", None))
        self.pushButton_show_outgoing.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.pushButton_upload_outgoing.setText(QCoreApplication.translate("MainWindow", u"Post", None))
        self.label_ovpm_total_ready.setText(QCoreApplication.translate("MainWindow", u"OUTGOING PAYMENTS READY TO POST:", None))
        self.pushButton_outgoing_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_disbursement), QCoreApplication.translate("MainWindow", u"Disbursement", None))
    # retranslateUi

