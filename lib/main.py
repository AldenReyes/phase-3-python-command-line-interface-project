import typer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from simple_term_menu import TerminalMenu

from models import User, Book, user_book

cli = typer.Typer()
pp = typer.echo


class Cli:
    @cli.command()
    def main_menu(self, current_user):
        self.clear_screen()
        pp(f"{current_user}'s Virtual Bookshelf")
        pp(" ")
        entry_items = [
            "[1] Add books to shelf",
            "[2] View books on shelf",
            "[3] Update books",
            "[4] Remove books",
            "[5] Exit",
        ]
        terminal_menu = TerminalMenu(entry_items, title="Enter an option below")
        menu_entry_index = terminal_menu.show()
        choice = menu_entry_index
        if choice == 4:
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
                self.main_menu(choice)
            else:
                name_confirm = typer.confirm(
                    "Name not found, would you like to use it as a new name?"
                )
                if not name_confirm:
                    self.entry_menu()
                    break
                else:
                    current_user = User(username=choice)
                    current_user.add_self_to_db()
                    self.main_menu(current_user)
                    break

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
