import ui_MainWindow
import addNewFeed as anf
import kratom
import sqlite3
from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit


class UiMainWindow(ui_MainWindow.Ui_MainWindow):
    def __init__(self):
        super(UiMainWindow, self).__init__()

    def setupUi(self, MainWindow):
        super(UiMainWindow, self).setupUi(MainWindow)

        # toolbar actions
        self.actionNew_Feed.triggered.connect(self.add_new_feed)
        self.actionDelete.triggered.connect(self.delete_feed)
        self.actionRefresh_Feeds.triggered.connect(self.refresh_feeds)

        # list widget actions
        self.subscriptionsListWidget.itemClicked.connect(self.load_articles)
        self.articlesListWidget.itemClicked.connect(self.load_summary)

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

    @staticmethod
    def refresh_feeds():
        # get a list of distinct feed urls
        # send them to parse_feed
        # if user has selected a feed - updated the articles list for that feed

        connection = sqlite3.connect('feeds.db')
        cursor = connection.cursor()
        feed_links = cursor.execute("SELECT DISTINCT link FROM subscriptions")
        feed_links = [link[0] for link in feed_links]

        for link in feed_links:
            kratom.parse_feed(link)
            print("Parsing feed: {name}".format(name=link))

    # load a list of articles into the articlesListWidget
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

    # load the summary of the article into the webView
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