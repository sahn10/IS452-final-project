from goodreads import client

gc = client.GoodreadsClient("Ha1oKI3R0fqeApxCJIcQ", "wbHQF5APtAgwKrY0kQ9gFSxyVEqt0kEqWwi3HUf0t7A")

book = gc.book(1)
# print(book)
# print(book.title)

# shelves = book.popular_shelves
# print(shelves)
# This is promising - can I get a list of fantasy books to loop over and find shelf data, then pull out shelves
# that highlight queer and diverse books?



# books = gc.search_books("lgbt")
# print(books)
# The problem with this command--it only searches title words.
