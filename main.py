from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit

import sqlite3
import feedparser
import uimainwindow as mw
import kratom
import sys


def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = mw.UiMainWindow()
    ui.setupUi(MainWindow)

    # DB STUFF
    kratom.initialize_db()

    # refresh subscriptions list
    kratom.refresh_subscriptions_list(ui)
    # TODO: create a function call to get_new_feeds() or something similar to check for new articles if the last modified date has been changed

    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()





