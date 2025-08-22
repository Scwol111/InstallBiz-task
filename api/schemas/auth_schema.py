""" Schemas for auth api
"""
from typing import Annotated, Optional
from datetime import datetime

from pydantic import BaseModel, Field, StringConstraints

class LoginInputSchema(BaseModel):
    """Schema for user registarion
    """
    login: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=255)]
    password: Annotated[str, StringConstraints(strip_whitespace=True, min_length=20, pattern="[a-zA-z1-90!\"#$%&'()*+,-.\\/:;<=>?@\[\]^_`{|}~]+")]

class LoginOutSchema(BaseModel):
    """Schema with jwt token
    """
    token: Optional[str] = None
    expire_at: Optional[datetime] = None
