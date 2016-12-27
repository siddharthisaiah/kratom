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
