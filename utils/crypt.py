""" Cryptographic utils
"""
import os
from typing import Any
from datetime import datetime, timezone, timedelta

from passlib.context import CryptContext
from jose import jwt, JWTError

class CryptUtils:
    """Class for work with cryptographics
    """
    crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret_key = os.environ['SECRET_KEY']

    def hash_password(self, password: str) -> str:
        """Create hash of password

        Args:
            password (str): raw password string

        Returns:
            str: hash string
        """
        return self.crypt_context.hash(password)

    def verify_password(self, password: str, hashed_password: str) -> bool:
        """Compare password and hashed iterpretation

        Args:
            password (str): raw password string
            hashed_password (str): hashed password string

        Returns:
            bool: True if password match hash, False otherwise
        """
        return self.crypt_context.verify(password, hashed_password)

    def encode_jwt(self, login: str) -> tuple[str, datetime]:
        """Creating jwt token

        Args:
            login (str): _description_

        Returns:
            tuple[str, float]: pair token and token end of life
        """
        expire_at = datetime.now(timezone.utc) + timedelta(minutes=float(os.environ.get('JWT_LIVE_MINUTES', '60')))
        return jwt.encode({
                'login': login,
                'expire_at': expire_at.timestamp()
            }, self.secret_key), expire_at

    def decode_jwt(self, token: str) -> dict[str, Any] | None:
        """Decode jwt to dict

        Args:
            token (str): token previously encoded

        Returns:
            dict[str, Any] | None: content of token or nothing if can't decode
        """
        try:
            return jwt.decode(token, self.secret_key)
        except JWTError:
            return None


crypt_utils = CryptUtils()
