""" Users model
"""
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import String, LargeBinary, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class BaseUserModel(DeclarativeBase):
    """Base model for ORM
    """

class Users(BaseUserModel):
    """Model for storing users
    """
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(String(50), unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True, default=None)
    password_hash: Mapped[str] = mapped_column(String(60))
