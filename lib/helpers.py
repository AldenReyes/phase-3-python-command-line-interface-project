import typer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User, Book

pp = typer.echo
engine = create_engine('sqlite:///virtual_bookshelf.db')
Session = sessionmaker(bind=engine)
session = Session()


class Current_User:
    def __init__(self, name) -> None:
        self.name = name

    def add_self_to_db(self):
        added_user = User(username=self.name)
        session.add(added_user)
        session.commit()
        pp(f"{self.name} added to db")
