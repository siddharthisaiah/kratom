from PyQt4 import QtCore, QtGui
from threading import Thread

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
    # check for new articles
    ui.refresh_feeds()

    kratom.timed_refresh_feeds(ui)

    MainWindow.show()

    # thread = Thread(target=kratom.timed_refresh_feeds(ui))
    # thread.start()


    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
