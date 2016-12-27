from PyQt4 import QtCore, QtGui

import sqlite3
import feedparser
import uimainwindow as mw


#
# Add a new row to the subscriptions table with feed_name and link
#
def new_subscription(url):
    feed = feedparser.parse(url)
    feed_name = feed.feed.title
    feed_link = feed.href

    connection = sqlite3.connect('feeds.db')
    cursor = connection.cursor()

    cursor.execute("SELECT rowid FROM subscriptions WHERE feed_name = ? AND link = ?", (feed_name, feed_link))
    result = cursor.fetchall()

    if len(result) == 0:
        cursor.execute("INSERT INTO subscriptions (feed_name, link) VALUES(?, ?)", (feed_name, feed_link))

    cursor.close()
    connection.commit()
    connection.close()

    parse_feed(feed_link)


#
# Parse feed url
#
def parse_feed(url):
    feed = feedparser.parse(url)
    feed_name = feed.feed.title

    # Open connection to DB and create cursor
    connection = sqlite3.connect('feeds.db')
    cursor = connection.cursor()

    for item in feed.entries:
        article_title = item.title
        article_summary = item.summary
        article_link = item.link
        article_pubdate = item.published

        # check if post is in db
        cursor.execute("SELECT rowid FROM articles WHERE title = ? AND date_published = ?",
                       (article_title, article_pubdate))
        result = cursor.fetchall()

        # insert values into db
        if len(result) == 0:
            cursor.execute(
                "INSERT INTO articles (feed_name, title, summary, link, date_published) VALUES(?, ?, ?, ?, ?)",
                (feed_name, article_title, article_summary, article_link, article_pubdate))

    cursor.close()
    connection.commit()
    connection.close()


#
# Make sure feeds.db exists and contains two tables - subscriptions and articles
#
def initialize_db():
    connection = sqlite3.connect('feeds.db')
    cursor = connection.cursor()

    # Create the subscriptions table if it doesnt exist
    subscription_table_string = '''CREATE TABLE IF NOT EXISTS subscriptions
                                   (id INTEGER PRIMARY KEY, feed_name TEXT, link TEXT)'''
    cursor.execute(subscription_table_string)

    articles_table_string = '''CREATE TABLE IF NOT EXISTS articles
                               (feed_name TEXT, title TEXT, summary TEXT, link TEXT, date_published TEXT)'''
    cursor.execute(articles_table_string)

    cursor.close()
    connection.close()


#
# Refresh the subscriptionsListWidget
#
def refresh_subscriptions_list(ui):
    # query the db for distinct feed_names
    connection = sqlite3.connect('feeds.db')
    cursor = connection.cursor()
    sql_string = "SELECT DISTINCT feed_name FROM subscriptions"
    cursor.execute(sql_string)

    # add all distinct feed_names  to the subscriptionsListWidget
    feed_names_list = cursor.fetchall()
    # cursor.fetchall() returns a list of tuples - convert to list of strings
    feed_names_list = [''.join(x) for x in feed_names_list]

    # remove old list before populating list
    ui.subscriptionsListWidget.clear()
    ui.subscriptionsListWidget.addItems(feed_names_list)

    cursor.close()
    connection.close()


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


#
# Dialog - Add New Feed
#
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(587, 170)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(220, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.feedLinkLabel = QtGui.QLabel(Dialog)
        self.feedLinkLabel.setGeometry(QtCore.QRect(50, 30, 41, 16))
        self.feedLinkLabel.setObjectName(_fromUtf8("feedLinkLabel"))
        self.feedLinkLineEdit = QtGui.QLineEdit(Dialog)
        self.feedLinkLineEdit.setGeometry(QtCore.QRect(50, 50, 481, 21))
        self.feedLinkLineEdit.setObjectName(_fromUtf8("feedLinkLineEdit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add A New Feed", None))
        self.feedLinkLabel.setText(_translate("Dialog", "URL :", None))


#
# MainWindow class
#
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1068, 804))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.subscriptionsListWidget = QtGui.QListWidget(self.widget)
        self.subscriptionsListWidget.setObjectName(_fromUtf8("subscriptionsListWidget"))
        self.subscriptionsListWidget.itemClicked.connect(self.load_articles)
        self.gridLayout.addWidget(self.subscriptionsListWidget, 0, 0, 2, 1)
        self.articlesListWidget = QtGui.QListWidget(self.widget)
        self.articlesListWidget.setObjectName(_fromUtf8("articlesListWidget"))
        self.articlesListWidget.itemClicked.connect(self.load_summary)
        self.gridLayout.addWidget(self.articlesListWidget, 0, 1, 1, 1)
        self.webView = QtWebKit.QWebView(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew_Feed = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Feed.setIcon(icon)
        self.actionNew_Feed.setObjectName(_fromUtf8("actionNew_Feed"))
        self.actionNew_Feed.triggered.connect(self.add_new_feed)
        self.actionDelete = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon1)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.actionDelete.triggered.connect(self.delete_feed)
        # Refresh toolbar action
        self.actionRefreshFeeds = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefreshFeeds.setIcon(icon2)
        self.actionRefreshFeeds.setObjectName(_fromUtf8("actionRefreshFeeds"))
        self.actionRefreshFeeds.triggered.connect(self.refresh_feeds)
        # End refresh toolbar action
        self.toolBar.addAction(self.actionNew_Feed)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addAction(self.actionRefreshFeeds)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "RSS Feed Reader", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionNew_Feed.setText(_translate("MainWindow", "New Feed", None))
        self.actionNew_Feed.setToolTip(_translate("MainWindow", "Add a New RSS Feed", None))
        self.actionDelete.setText(_translate("MainWindow", "Delete", None))
        self.actionDelete.setToolTip(_translate("MainWindow", "Delete a Feed", None))
        self.actionRefreshFeeds.setText(_translate("MainWindow", "Refresh Feeds", None))
        self.actionRefreshFeeds.setToolTip(_translate("MainWindow", "Refresh Feeds", None))

    def add_new_feed(self):
        newFeedDialog = QtGui.QDialog()
        dialog = Ui_Dialog()
        dialog.setupUi(newFeedDialog)
        newFeedDialog.exec_()

        url = dialog.feedLinkLineEdit.text()

        if url:
            # create row in subscriptions table
            new_subscription(url)
            # update the subscriptionsListWidget with the new feed name
            refresh_subscriptions_list(self)

    def load_articles(self, item):
        feed_name = item.text()

        connection = sqlite3.connect('feeds.db')
        cursor = connection.cursor()
        cursor.execute("SELECT title FROM articles WHERE feed_name = ?", (feed_name,))

        articles = cursor.fetchall()
        articles = [''.join(x) for x in articles]

        cursor.close()
        connection.close()
        self.articlesListWidget.clear()
        self.articlesListWidget.addItems(articles)

    def load_summary(self, item):
        article_title = item.text()

        connection = sqlite3.connect('feeds.db')
        cursor = connection.cursor()
        cursor.execute("SELECT summary FROM articles WHERE title = ?", (article_title,))

        article_summary = cursor.fetchall()
        article_summary = [''.join(x) for x in article_summary]

        html = '''<h1>{title}</h1> <div>{summary}</div>'''.format(title=article_title, summary=article_summary[0])
        self.webView.setHtml(html)

        cursor.close()
        connection.close()

    def delete_feed(self):
        feed_listItemObject = self.subscriptionsListWidget.currentItem()
        feed_name = self.subscriptionsListWidget.currentItem().text()

        connection = sqlite3.connect('feeds.db')
        cursor = connection.cursor()
        articles_string = "DELETE FROM articles WHERE feed_name = {}".format(feed_name)
        subscriptions_string = "DELETE FROM subscriptions WHERE feed_name = {}".format(feed_name)
        cursor.execute("DELETE FROM articles WHERE feed_name = ?", (feed_name,))
        cursor.execute("DELETE FROM subscriptions WHERE feed_name = ?", (feed_name,))
        cursor.close()
        connection.commit()
        connection.close()

        self.articlesListWidget.clear()
        self.webView.setHtml('')
        self.subscriptionsListWidget.takeItem(self.subscriptionsListWidget.row(feed_listItemObject))

    def refresh_feeds(self):
        # get a list of distinct feed urls
        # send them to parse_feed
        # if user has selected a feed - updated the articles list for that feed

        connection = sqlite3.connect('feeds.db')
        cursor = connection.cursor()
        feed_links = cursor.execute("SELECT DISTINCT link FROM subscriptions")
        feed_links = [link[0] for link in feed_links]

        for link in feed_links:
            parse_feed(link)
            print("Parsing feed: {name}".format(name=link))


from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = mw.UiMainWindow()
    ui.setupUi(MainWindow)

    # DB STUFF
    initialize_db()

    # refresh subscriptions list
    refresh_subscriptions_list(ui)
    # get_new_feeds()

    MainWindow.show()
    sys.exit(app.exec_())



