# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyJizzMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.categoryScroll = QtWidgets.QScrollArea(self.centralwidget)
        self.categoryScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.categoryScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.categoryScroll.setWidgetResizable(True)
        self.categoryScroll.setObjectName("categoryScroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 621, 87))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.categoryScroll.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.categoryScroll, 0, 0, 1, 2)
        self.vedeoLayout = QtWidgets.QVBoxLayout()
        self.vedeoLayout.setObjectName("vedeoLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.vedeoLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pagePrevButton = QtWidgets.QPushButton(self.centralwidget)
        self.pagePrevButton.setObjectName("pagePrevButton")
        self.horizontalLayout.addWidget(self.pagePrevButton)
        self.pageSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.pageSpinBox.setObjectName("pageSpinBox")
        self.horizontalLayout.addWidget(self.pageSpinBox)
        self.pageNextButton = QtWidgets.QPushButton(self.centralwidget)
        self.pageNextButton.setObjectName("pageNextButton")
        self.horizontalLayout.addWidget(self.pageNextButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.vedeoLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.vedeoLayout, 1, 0, 1, 1)
        self.playerLayout = QtWidgets.QVBoxLayout()
        self.playerLayout.setObjectName("playerLayout")
        self.gridLayout.addLayout(self.playerLayout, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pagePrevButton.setText(_translate("MainWindow", "Prev Page"))
        self.pageNextButton.setText(_translate("MainWindow", "Next Page"))

