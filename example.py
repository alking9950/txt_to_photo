import sqlite3
from random import randint

dbpost = "rss.db"

from photo import photo
    

conn = sqlite3.connect(dbpost)
conn.row_factory = sqlite3.Row
c = conn.cursor()
feeds = c.execute('SELECT * FROM RSSEntries').fetchall()
for feed in feeds:
    r = randint(9999,999999999)
    texts = feed['content']
    if texts == '':
        pass
    photo(texts).save(f'photo/{r}.jpg')