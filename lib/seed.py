#!/usr/bin/env python3
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Book

fake = Faker()


def delete_records():
    session.query(Book).delete()
    session.query(User).delete()
    session.commit()


def seed_db():
    print("Seeding books...")
    books = [
        Book(title=fake.word(), author=fake.name(), year_published=fake.year())
        for i in range(20)
    ]
    print("Seeding users...")
    users = [User(username=fake.unique.first_name()) for i in range(5)]
    session.bulk_save_objects(books)
    session.bulk_save_objects(users)
    session.commit()
    print("Finished seeding...")


if __name__ == '__main__':
    engine = create_engine('sqlite:///virtual_bookshelf.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    delete_records()
    seed_db()
