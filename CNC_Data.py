from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/drilling.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("/*background color*/\n"
"#MainWindow {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.085, y2:0, stop:0.0845771 rgba(44, 102, 226, 255), stop:1 rgba(110, 221, 237, 255))\n"
"}\n"
"\n"
"#MainWindow QGroupBox {\n"
"    border: 1px solid #c6c6c6;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#groupBox {\n"
"    border: None;\n"
"    background-color: qlineargradient(spread:pad, x1:0.95, y1:0.539409, x2:0, y2:0.545, stop:0.0845771 rgba(173, 122, 240, 251), stop:1 rgba(54, 193, 255, 255))\n"
"}\n"
"\n"
"#groupBox_2{\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"#MainWindow QPushButton {\n"
"    border-radius: 5px;\n"
"    border-color: rgb(127, 127, 127);\n"
"    background-color: #fff;\n"
"    padding: 4px 8px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"#MainWindow QPushButton:hover{\n"
"    background-color:#00aaff;\n"
"    color:#fff;\n"
"}\n"
"\n"
"#MainWindow QPushButton:pressed{\n"
"    padding-left: 10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 0, 961, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(100, 10, 71, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/database.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 71, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icons/drilling.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(220, 20, 611, 51))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 150, 961, 221))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 961, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(155)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(18, 380, 961, 241))
        self.groupBox_4.setObjectName("groupBox_4")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_4)
        self.graphicsView.setGeometry(QtCore.QRect(0, 20, 961, 231))
        self.graphicsView.setObjectName("graphicsView")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 100, 931, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.get_path_btn = QtWidgets.QPushButton(self.widget)
        self.get_path_btn.setMinimumSize(QtCore.QSize(150, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/free-icon-file-and-folder-8326488.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.get_path_btn.setIcon(icon1)
        self.get_path_btn.setObjectName("get_path_btn")
        self.horizontalLayout.addWidget(self.get_path_btn)
        self.save_btn = QtWidgets.QPushButton(self.widget)
        self.save_btn.setMinimumSize(QtCore.QSize(120, 0))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/free-icon-save-2550221.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon2)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.get_data_btn = QtWidgets.QPushButton(self.widget)
        self.get_data_btn.setMinimumSize(QtCore.QSize(120, 0))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/free-icon-search-magnifier-symbol-of-interface-51658.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.get_data_btn.setIcon(icon3)
        self.get_data_btn.setObjectName("get_data_btn")
        self.horizontalLayout.addWidget(self.get_data_btn)
        self.reload_btn = QtWidgets.QPushButton(self.widget)
        self.reload_btn.setEnabled(True)
        self.reload_btn.setMinimumSize(QtCore.QSize(120, 0))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/free-icon-reloading-9043724.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reload_btn.setIcon(icon4)
        self.reload_btn.setObjectName("reload_btn")
        self.horizontalLayout.addWidget(self.reload_btn)
        spacerItem1 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Show Data"))
        self.label_3.setText(_translate("MainWindow", "CNC Machine Data Display"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Spindle_ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Speed"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Gear"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Power"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Position"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Torque"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Spindle_Speed"))
        self.get_path_btn.setText(_translate("MainWindow", "Select Save Path"))
        self.save_btn.setText(_translate("MainWindow", "Save Data"))
        self.get_data_btn.setText(_translate("MainWindow", "Get Data"))
        self.reload_btn.setText(_translate("MainWindow", "Reload Data"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
