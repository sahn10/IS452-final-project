# Task: Get a list of fantasy book IDs to loop through and find shelf data for, then find shelves to do with diverse books, etc.
# Need to come up with shelf keywords to isolate

# get list of books tagged fantasy (genre tag...)
# scrape book IDs from Fantasy pages

from goodreads import client
from lxml import etree

gc = client.GoodreadsClient("Ha1oKI3R0fqeApxCJIcQ", "wbHQF5APtAgwKrY0kQ9gFSxyVEqt0kEqWwi3HUf0t7A")

infile = open("fantasy_p1.htm", "rb")
xml = infile.read()
infile.close()

tree = etree.fromstring(xml)

print(tree.xpath("//div[@class='wtrRight wtrUp']/form/input[@name='book_id']/@value)")



# Query for getting book ids from fantasy list: //div[@class='wtrRight wtrUp']/form/input[@name="book_id"]/@value

# URL:
# https://www.goodreads.com/shelf/show/fantasy
