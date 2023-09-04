import typer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from simple_term_menu import TerminalMenu
from prettytable import PrettyTable

from models import User, Book

pp = typer.echo
engine = create_engine('sqlite:///virtual_bookshelf.db')
Session = sessionmaker(bind=engine)
session = Session()


def add_book_menu():
    current_book = Book()

    entry_items = [
        "[1] Add to bookshelf",
        "[2] Return to main menu",
    ]
    terminal_menu = TerminalMenu(entry_items, title="Enter an option below")
    menu_entry_index = terminal_menu.show()
    choice = menu_entry_index

    if choice == 0:
        title = typer.prompt("Enter book title", type=str)
        current_book.title = title
        author = typer.prompt("Enter book author", type=str)
        current_book.author = author
        year_published = typer.prompt("Enter book year published", type=int)
        current_book.year_published = year_published

        session.add(current_book)
        session.commit()
        pp("Book has been added to shared bookshelf")
        add_book_menu()

    if choice == 1:
        return


def view_book_menu():
    entry_items = [
        "[1] View all books",
        "[2] Return to main menu",
    ]
    terminal_menu = TerminalMenu(entry_items, title="Enter an option below")
    menu_entry_index = terminal_menu.show()
    choice = menu_entry_index

    if choice == 0:
        table = PrettyTable()
        table.field_names = ["Title", "Author", "Year Published"]

        books = tuple(book for book in session.query(Book))
        for book in books:
            table.add_row([book.title, book.author, book.year_published])
        pp(table)
        view_book_menu()

    if choice == 1:
        return
