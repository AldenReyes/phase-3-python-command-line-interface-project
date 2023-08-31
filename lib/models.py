from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

user_book = Table(
    'user_books',
    Base.metadata,
    Column('id', Integer(), primary_key=True),
    Column('user_id', ForeignKey('users.id')),
    Column('book_id', ForeignKey('books.id')),
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
    year_published = Column(Integer())

    users = relationship('User', secondary=user_book, back_populates='books')


def __repr__(self):
    return (
        f'id={self.id},' f'title={self.title}',
        f'author={self.author}',
        f'year_published={self.year_published}',
    )
