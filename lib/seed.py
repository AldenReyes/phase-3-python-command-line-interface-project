#!/usr/bin/env python3
from faker import Faker
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker

from models import User, Book, user_book

import random

fake = Faker()


def delete_records():
    session.query(Book).delete()
    session.query(User).delete()
    session.query(user_book).delete()
    session.commit()


def create_records():
    print("Seeding books, users...")
    books = [
        Book(title=fake.word(), author=fake.name(), year_published=fake.year())
        for i in range(20)
    ]
    users = [User(username=fake.unique.first_name()) for i in range(5)]
    session.add_all(books + users)
    session.commit()
    return books, users


def associate_books_to_users(books, users):
    print("Associating books to users...")
    for book in books:
        users_for_book = random.sample(users, (random.randint(1, 3)))
        for user in users_for_book:
            entry = {'user_id': (user.id), 'book_id': (book.id)}
            session.execute(insert(user_book), entry)
            session.commit()


if __name__ == '__main__':
    engine = create_engine('sqlite:///virtual_bookshelf.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    delete_records()
    books, users = create_records()
    associate_books_to_users(books, users)
    print("Finished seeding database")
