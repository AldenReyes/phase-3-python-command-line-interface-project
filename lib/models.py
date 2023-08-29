from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

user_book = Table(
    'user_books',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('book_id', ForeignKey('books.id'), primary_key=True),
    extend_existing=True,
)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String(26))

    books = relationship('Book', secondary=user_book, back_populates='users')


def __repr__(self):
    return f'User(id = {self.id},' f'username={self.username})'


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    author = Column(String())
    year_written = Column(DateTime())
    date_started = Column(DateTime(), nullable=True)
    date_finished = Column(DateTime(), nullable=True)

    users = relationship('User', secondary=user_book, back_populates='books')


def __repr__(self):
    return (
        f'id={self.id},' f'title={self.title}',
        f'author={self.author}',
        f'year_written={self.year_written}',
    )
