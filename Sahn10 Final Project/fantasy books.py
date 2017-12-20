# Task: Get a list of fantasy book IDs to loop through and find shelf data for, then find shelves to do with diverse books, etc.
# Need to come up with shelf keywords to isolate

# get list of books tagged fantasy (genre tag...)
# scrape book IDs from Fantasy pages

from goodreads import client
from lxml import html
import requests

gc = client.GoodreadsClient("Ha1oKI3R0fqeApxCJIcQ", "wbHQF5APtAgwKrY0kQ9gFSxyVEqt0kEqWwi3HUf0t7A")

page = requests.get('https://www.goodreads.com/shelf/show/fantasy')
# thank you internet -- http://docs.python-guide.org/en/latest/scenarios/scrape/

tree = html.fromstring(page.content)

print(tree.xpath("//form[@class='hiddenShelfForm']/input[@name='book_id']/@value"))
# yesssss it worked -- the problem was with my xpath query.
# Next step: set up accumulator to get all the page urls



# Query for getting book ids from fantasy list: //div[@class='wtrRight wtrUp']/form/input[@name="book_id"]/@value

# URL:
# https://www.goodreads.com/shelf/show/fantasy
