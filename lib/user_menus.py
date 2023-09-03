import typer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User, Book

pp = typer.echo
engine = create_engine('sqlite:///virtual_bookshelf.db')
Session = sessionmaker(bind=engine)
session = Session()


def add_book_menu(current_user):
    current_book = Book()
    pp(f"{current_user}'s Virtual Bookshelf")
    pp(" ")

    title = typer.prompt("Enter book title", type=str)
    current_book.title = title
    author = typer.prompt("Enter book author", type=str)
    current_book.author = author
    year_published = typer.prompt("Enter book year published", type=int)
    current_book.year_published = year_published

    session.add(current_book)
    session.commit()
    return
