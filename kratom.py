import feedparser
import sqlite3


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