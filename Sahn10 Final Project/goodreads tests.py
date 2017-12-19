from goodreads import client

gc = client.GoodreadsClient("Ha1oKI3R0fqeApxCJIcQ", "wbHQF5APtAgwKrY0kQ9gFSxyVEqt0kEqWwi3HUf0t7A")

book = gc.book(1)
# print(book)
# print(book.title)

shelves = book.popular_shelves
print(shelves)



# books = gc.search_books("lgbt")
# print(books)
