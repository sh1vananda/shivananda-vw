from flask import Blueprint, request, render_template, redirect, url_for
from db import db
from models.book import Book

books_bp = Blueprint("books", __name__)

@books_bp.route("/")
def home():
    books = Book.query.all()
    return render_template("books.html", books=books)

@books_bp.route("/books", methods=["POST"])
def add_book():
    title = request.form.get("title")
    author = request.form.get("author")
    copies = int(request.form.get("copies"))
    book = Book(title=title, author=author, copies=copies)
    db.session.add(book)
    db.session.commit()
    return redirect(url_for("books.home"))

@books_bp.route("/borrow/<int:book_id>", methods=["POST"])
def borrow(book_id):
    book = Book.query.get(book_id)
    if book.copies == 0:
        return "Book unavailable"
    book.copies -= 1
    db.session.commit()
    return redirect(url_for("books.home"))

@books_bp.route("/books/unavailable")
def unavailable_books():
    books = Book.query.filter(Book.copies == 0).all()
    return "<br>".join(book.title for book in books)