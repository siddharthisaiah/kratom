import ui_MainWindow
import addNewFeed as anf
import kratom
from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit


class UiMainWindow(ui_MainWindow.Ui_MainWindow):
    def __init__(self):
        super(UiMainWindow, self).__init__()

    def setupUi(self, MainWindow):
        super(UiMainWindow, self).setupUi(MainWindow)
        self.actionNew_Feed.triggered.connect(self.add_new_feed)

    def add_new_feed(self):
        new_feed_dialog = QtGui.QDialog()
        dialog = anf.Ui_Dialog()
        dialog.setupUi(new_feed_dialog)
        new_feed_dialog.exec_()

        url = dialog.feedLinkLineEdit.text()

        if url:
            # create row in subscriptions table
            kratom.new_subscription(url)
            # update the subscriptionsListWidget with the new feed name
            kratom.refresh_subscriptions_list(self)
