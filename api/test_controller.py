""" Auth controller
"""
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi_controllers import Controller, get

from api.api_utils.auth_validate import auth_validate_token


class TestController(Controller):
    """_summary_
    """
    prefix = '/test'
    tags = ['test']

    @get('/say_hello')
    def say_hello(self) -> str:
        """Simple method without any auth

        Returns:
            str: simple hello
        """
        return "Hello world"
    
    @get('/say_hello_auth')
    def say_hello_auth(self, credential: Annotated[HTTPAuthorizationCredentials, Depends(auth_validate_token)]) -> str:
        """Simple method with auth. You can see result only after auth

        Returns:
            str: simple hello
        """
        return "Hello world"
