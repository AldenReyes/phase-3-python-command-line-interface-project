import typer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User, Book, user_book
from helpers import handle_login, handle_create_user

cli = typer.Typer()
pp = typer.echo


class Bookshelf:
    def __init__(self) -> None:
        self.users = [user for user in session.query(User)]
        self.books = [book for book in session.query(Book)]
        self.user_book = [user_book for user_book in session.query(user_book)]


@cli.command()
def login_menu():
    bookshelf = Bookshelf()
    users = tuple(user.username for user in bookshelf.users)
    pp("\n" * 50)
    pp("Existing users: \n")
    pp(users)
    choice = typer.prompt("Enter a name : ")
    while choice:
        if choice in users:
            handle_login(choice)
        else:
            handle_create_user(choice)


@cli.command()
def main_menu():
    menu_items = "1 : Login \n2 : Exit\n"

    pp("\n" * 50)
    pp("Welcome to the Virtual Bookshelf!")
    pp(" ")
    pp("Enter an option below")
    choice = typer.prompt(menu_items)
    while choice:
        if choice == '1':
            login_menu()
        elif choice == '2':
            exit = typer.confirm("Are you sure you want to exit?")
            if not exit:
                main_menu()
            else:
                pp("Exiting...")
                quit()
        else:
            pp("\n" * 50)
            pp("Invalid input")
            choice = input(f"\nEnter your choice : \n{menu_items}")


# pp(tuple(book.title for book in session.query(Book)))

if __name__ == "__main__":
    engine = create_engine('sqlite:///virtual_bookshelf.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    typer.run(main_menu)
