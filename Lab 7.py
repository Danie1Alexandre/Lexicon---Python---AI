class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages


book1 = Book(
    title = "REd",
    author= "ben",
    pages = 200
)
book2 = Book(
    title = "green",
    author= "anna",
    pages = 500
)
book3 = Book(
    title = "black",
    author= "david",
    pages = 2000
)
book4 = Book(
    title = "blue",
    author= "jmmy",
    pages = 450
)

print(book1.title, book1.author, book1.pages)
print(book2.title, book2.author, book2.pages)
print(book3.title, book3.author, book3.pages)
print(book4.title, book4.author, book4.pages)