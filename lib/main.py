import typer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from simple_term_menu import TerminalMenu

from models import User, Book, user_book
from user_menus import add_book_menu, view_book_menu

cli = typer.Typer()
pp = typer.echo


class Cli:
    current_user = None

    @cli.command()
    def main_menu(self):
        self.clear_screen()
        pp(f"{self.current_user}'s Virtual Bookshelf")
        pp(" ")
        entry_items = [
            "[1] Add books to bookshelf",
            "[2] View books on shelf",
            "[3] Update books",
            "[4] Remove books",
            "[5] Return to login",
            "[6] Exit",
        ]
        terminal_menu = TerminalMenu(entry_items, title="Enter an option below")
        menu_entry_index = terminal_menu.show()
        choice = menu_entry_index
        if choice == 0:
            add_book_menu()
            self.main_menu()
        if choice == 1:
            view_book_menu()
            self.main_menu()
        if choice == 4:
            self.login_menu()
        if choice == 5:
            pp("Exiting...")
            quit()

    @cli.command()
    def login_menu(self):
        logged_users = tuple(user.username for user in session.query(User))
        self.clear_screen()
        pp("Existing users: \n")
        pp(logged_users)
        choice = typer.prompt("Enter a name (limit 26 characters) ")

        if len(choice) > 26:
            self.login_menu()
        while choice:
            if choice in logged_users:
                self.current_user = choice
                self.main_menu()
            else:
                name_confirm = typer.confirm(
                    "Name not found, would you like to use it as a new name?"
                )
                if not name_confirm:
                    self.entry_menu()
                else:
                    user_to_add = User(username=choice)
                    pp(user_to_add)
                    user_to_add.add_self_to_db()
                    self.current_user = choice
                    self.main_menu()

    @cli.command()
    def entry_menu(self):
        self.clear_screen()
        pp("Welcome to the Virtual Bookshelf!")
        pp(" ")
        entry_items = ["[1] Login", "[2] Exit"]
        terminal_menu = TerminalMenu(entry_items, title="Enter an option below")
        menu_entry_index = terminal_menu.show()
        choice = menu_entry_index

        if choice == 0:
            self.login_menu()
        elif choice == 1:
            exit = typer.confirm("Are you sure you want to exit?")
            if not exit:
                self.entry_menu()
            else:
                pp("Exiting...")
                quit()
        else:
            self.clear_screen()
            pp("Invalid input")
            choice = input(f"\nEnter your choice : \n{entry_items}")

    def clear_screen(self):
        pp("\n" * 50)


if __name__ == "__main__":
    engine = create_engine('sqlite:///virtual_bookshelf.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    cli = Cli()
    typer.run(cli.entry_menu())
