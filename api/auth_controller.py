""" Auth controller
"""
from fastapi import Response, status
from fastapi_controllers import Controller, get, post
from jose import jwt

from api.schemas.auth_schema import LoginInputSchema, LoginOutSchema
from database.users import UsersDBWorker
from utils.crypt import crypt_utils


class AuthController(Controller):
    """Auth controller. Have routes to auth with
    """
    prefix = '/auth'
    tags = ['authorization']
    user_db_worker = UsersDBWorker()

    @post('/register')
    def register(self, body: LoginInputSchema) -> Response:
        """Create new user

        Args:
            body (LoginInputSchema): request body with user info

        Returns:
            Response: result of creation
        """
        try:
            self.user_db_worker.create_user(body.login, body.password)
        except ValueError:
            return Response({'Error': f'User with {body.login} already exists'},
                                status.HTTP_400_BAD_REQUEST)
        return Response(status_code=status.HTTP_201_CREATED)

    @post('/login')
    def login(self, response: Response, body: LoginInputSchema) -> LoginOutSchema:
        """Login in system by login-password pair

        Args:
            response (Response): _description_
            body (LoginInputSchema): _description_

        Returns:
            LoginOutSchema: _description_
        """
        user = self.user_db_worker.get_user_by_login(body.login)
        if not user is None and crypt_utils.verify_password(body.password, user.password_hash):
            token, exp_at = crypt_utils.encode_jwt(user.login)
            return LoginOutSchema(token=token, expire_at=exp_at)
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return LoginOutSchema()
