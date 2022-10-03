from crypt import methods
from flask import render_template, request, redirect
from app import app
from models.book import *
from models.books import *



@app.route("/books")
def index():
    return render_template("index.html", title = "Home", books = books)

@app.route("/books/<index>", methods=["GET"])
def single_book(index):
    chosen_book = books[int(index)]
    return render_template("index.html", book = chosen_book)

@app.route("/books", methods=["POST"])
def add_task():
    book_title = request.form["title"]
    book_author = request.form["author"]
    book_genre = request.form["genre"]
    new_book = Book(book_title, book_author, book_genre)
    add_new_book(new_book)
    return render_template("index.html", books=books )

@app.route("/books/delete/<title>", methods=['POST'])
def delete(title):
    delete_book(title)
    return redirect("/books")