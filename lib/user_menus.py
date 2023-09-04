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
        edit_book_info(current_book)
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
        display_books()
        view_book_menu()

    if choice == 1:
        return


def update_book_menu():
    entry_items = [
        "[1] Update a book",
        "[2] Return to main menu",
    ]
    terminal_menu = TerminalMenu(entry_items, title="Enter an option below")
    menu_entry_index = terminal_menu.show()
    choice = menu_entry_index
    if choice == 0:
        display_books()
        update_book_by_id()
        update_book_menu()
    if choice == 1:
        return


def delete_book_menu():
    entry_items = [
        "[1] Delete a book",
        "[2] Return to main menu",
    ]
    terminal_menu = TerminalMenu(entry_items, title="Enter an option below")
    menu_entry_index = terminal_menu.show()
    choice = menu_entry_index
    if choice == 0:
        display_books()
        delete_book_by_id()
        delete_book_menu()
    if choice == 1:
        return


def display_books():
    table = PrettyTable()
    table.field_names = ["Id", "Title", "Author", "Year Published"]

    books = tuple(book for book in session.query(Book))
    for book in books:
        table.add_row([book.id, book.title, book.author, book.year_published])
    pp(table)


def update_book_by_id():
    book_to_update = typer.prompt("Enter a book id to update ", type=int)
    book_found = session.query(Book).filter(Book.id == book_to_update).first()
    if not book_found:
        pp("Book not found, please try again")
        entry_items = [
            "[1] Try again",
            "[2] Return to main menu",
        ]
        terminal_menu = TerminalMenu(entry_items, title="Enter an option below")
        menu_entry_index = terminal_menu.show()
        choice = menu_entry_index
        if choice == 0:
            update_book_by_id()
        if choice == 1:
            return
    else:
        table = PrettyTable()
        table.field_names = ["Id", "Title", "Author", "Year Published"]
        table.add_row(
            [
                book_found.id,
                book_found.title,
                book_found.author,
                book_found.year_published,
            ]
        )
        pp(table)
        edit_book_info(book_found)
        pp("Book has been updated")
        return


def edit_book_info(book):
    title = typer.prompt("Enter book title", type=str)
    book.title = title
    author = typer.prompt("Enter book author", type=str)
    book.author = author
    year_published = typer.prompt("Enter book year published", type=int)
    book.year_published = year_published

    session.add(book)
    session.commit()


def delete_book_by_id():
    book_to_delete = typer.prompt("Enter a book id to delete ", type=int)
    book_found = session.query(Book).filter(Book.id == book_to_delete).first()
    if not book_found:
        pp("Book not found, please try again")
        entry_items = [
            "[1] Try again",
            "[2] Return to main menu",
        ]
        terminal_menu = TerminalMenu(entry_items, title="Enter an option below")
        menu_entry_index = terminal_menu.show()
        choice = menu_entry_index
        if choice == 0:
            delete_book_by_id()
        if choice == 1:
            return
    else:
        table = PrettyTable()
        table.field_names = ["Id", "Title", "Author", "Year Published"]
        table.add_row(
            [
                book_found.id,
                book_found.title,
                book_found.author,
                book_found.year_published,
            ]
        )
        pp("Selected book:")
        pp(table)
        session.delete(book_found)
        session.commit()
