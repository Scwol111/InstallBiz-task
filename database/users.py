""" Module to work with users table in db
"""
import os

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models.users import Users
from utils.crypt import crypt_utils


class UsersDBWorker:
    """DB worker with users table
    """
    engine = create_engine(os.environ['DATABASE_URL'])

    def get_user_by_login(self, login: str) -> Users | None:
        """Get user object by his login from database

        Args:
            login (str): user login

        Returns:
            Users | None: user object if founded else None
        """
        with Session(self.engine) as session:
            return session.scalar(select(Users).where(Users.login == login))

    def create_user(self, login: str, password: str) -> Users:
        """Creating one new user 

        Args:
            login (str): login of user
            password (str): password of user

        Raises:
            ValueError: raises if inputed login duplicates in db

        Returns:
            Users: new created user
        """
        with Session(self.engine) as session:
            if not self.get_user_by_login(login) is None:
                raise ValueError('Login duplicate')
            new_user = Users(login=login, password_hash=crypt_utils.hash_password(password))
            session.add(new_user)
            session.commit()
        return new_user
