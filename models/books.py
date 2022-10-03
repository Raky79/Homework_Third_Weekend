from models.book import *
import datetime

book1 = Book("The Hobbit", "J.R.R. Tolkien", "Epic Fantasy")
book2 = Book("Great Expectations", "Charles Dickens", "Graphic Novel")
book3 = Book("Harry Potter and the Philosopher's Stone", "J.K.Rowling", "Fantasy Fiction")

books = [book1, book2, book3]


def add_new_book(book):
    books.append(book) 

def delete_book(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = book
            break
    books.remove(book_to_delete) 