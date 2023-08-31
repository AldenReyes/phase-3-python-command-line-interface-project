#!/usr/bin/env python3
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import ipdb

from models import User, Book, user_book

fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///virtual_bookshelf.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    ipdb.set_trace()
