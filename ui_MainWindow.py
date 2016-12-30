# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1108, 618)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.subscriptionsListWidget = QtGui.QListWidget(self.splitter_2)
        self.subscriptionsListWidget.setObjectName(_fromUtf8("subscriptionsListWidget"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.articlesListWidget = QtGui.QListWidget(self.splitter)
        self.articlesListWidget.setObjectName(_fromUtf8("articlesListWidget"))
        self.webView = QtWebKit.QWebView(self.splitter)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuActions = QtGui.QMenu(self.menubar)
        self.menuActions.setObjectName(_fromUtf8("menuActions"))
        self.menuPreferences = QtGui.QMenu(self.menubar)
        self.menuPreferences.setObjectName(_fromUtf8("menuPreferences"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(32, 0))
        self.toolBar.setBaseSize(QtCore.QSize(0, 0))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew_Feed = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/new.png")), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/new.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionNew_Feed.setIcon(icon)
        self.actionNew_Feed.setObjectName(_fromUtf8("actionNew_Feed"))
        self.actionDelete = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionDelete.setIcon(icon1)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.actionRefresh_Feeds = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionRefresh_Feeds.setIcon(icon2)
        self.actionRefresh_Feeds.setObjectName(_fromUtf8("actionRefresh_Feeds"))
        self.actionMenu_New_Feed = QtGui.QAction(MainWindow)
        self.actionMenu_New_Feed.setObjectName(_fromUtf8("actionMenu_New_Feed"))
        self.actionMenu_Close = QtGui.QAction(MainWindow)
        self.actionMenu_Close.setObjectName(_fromUtf8("actionMenu_Close"))
        self.actionMenu_Refresh_All_Feeds = QtGui.QAction(MainWindow)
        self.actionMenu_Refresh_All_Feeds.setObjectName(_fromUtf8("actionMenu_Refresh_All_Feeds"))
        self.actionMenu_Refresh_Selected_Feed = QtGui.QAction(MainWindow)
        self.actionMenu_Refresh_Selected_Feed.setObjectName(_fromUtf8("actionMenu_Refresh_Selected_Feed"))
        self.actionMenu_Delete_Feed = QtGui.QAction(MainWindow)
        self.actionMenu_Delete_Feed.setObjectName(_fromUtf8("actionMenu_Delete_Feed"))
        self.actionMenu_Settings = QtGui.QAction(MainWindow)
        self.actionMenu_Settings.setObjectName(_fromUtf8("actionMenu_Settings"))
        self.menuFile.addAction(self.actionMenu_New_Feed)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionMenu_Close)
        self.menuActions.addAction(self.actionMenu_Refresh_All_Feeds)
        self.menuActions.addAction(self.actionMenu_Refresh_Selected_Feed)
        self.menuActions.addAction(self.actionMenu_Delete_Feed)
        self.menuPreferences.addAction(self.actionMenu_Settings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuPreferences.menuAction())
        self.toolBar.addAction(self.actionNew_Feed)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addAction(self.actionRefresh_Feeds)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Kratom", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuActions.setTitle(_translate("MainWindow", "Actions", None))
        self.menuPreferences.setTitle(_translate("MainWindow", "Preferences", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionNew_Feed.setText(_translate("MainWindow", "New Feed", None))
        self.actionNew_Feed.setToolTip(_translate("MainWindow", "Subscribe to a new RSS feed", None))
        self.actionDelete.setText(_translate("MainWindow", "Delete", None))
        self.actionDelete.setToolTip(_translate("MainWindow", "Remove a feed and all its articles", None))
        self.actionRefresh_Feeds.setText(_translate("MainWindow", "Refresh Feeds", None))
        self.actionRefresh_Feeds.setToolTip(_translate("MainWindow", "Check for new articles", None))
        self.actionMenu_New_Feed.setText(_translate("MainWindow", "New Feed", None))
        self.actionMenu_New_Feed.setShortcut(_translate("MainWindow", "Meta+N", None))
        self.actionMenu_Close.setText(_translate("MainWindow", "Close", None))
        self.actionMenu_Close.setShortcut(_translate("MainWindow", "Meta+W", None))
        self.actionMenu_Refresh_All_Feeds.setText(_translate("MainWindow", "Refresh All Feeds", None))
        self.actionMenu_Refresh_All_Feeds.setShortcut(_translate("MainWindow", "Meta+R", None))
        self.actionMenu_Refresh_Selected_Feed.setText(_translate("MainWindow", "Refresh Selected Feed", None))
        self.actionMenu_Refresh_Selected_Feed.setShortcut(_translate("MainWindow", "Meta+Shift+R", None))
        self.actionMenu_Delete_Feed.setText(_translate("MainWindow", "Delete Feed", None))
        self.actionMenu_Delete_Feed.setShortcut(_translate("MainWindow", "Meta+D", None))
        self.actionMenu_Settings.setText(_translate("MainWindow", "Settings", None))

from PyQt4 import QtWebKit
