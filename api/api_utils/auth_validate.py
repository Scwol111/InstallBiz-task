"""Module with auth utils
"""

from datetime import datetime, timezone

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from utils.crypt import crypt_utils
from models.users import Users
from database.users import UsersDBWorker


security = HTTPBearer()
db_worker = UsersDBWorker()


def auth_validate_token(token: HTTPAuthorizationCredentials = Depends(security)) -> Users:
    """Api credentials validate jwt token

    Args:
        token (HTTPAuthorizationCredentials, optional): auth jwt token. Defaults to Depends(security).

    Raises:
        HTTPException: raises if bad token, or token experied

    Returns:
        Users: requested user
    """
    validate_data = crypt_utils.decode_jwt(token.credentials)
    if not validate_data is None:
        if datetime.now(timezone.utc).timestamp() <= validate_data['expire_at']:
            user = db_worker.get_user_by_login(validate_data['login'])
            if not user is None and user.is_active:
                return user
            raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="User deleted or is unactive",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token experied",
                headers={"WWW-Authenticate": "Bearer"},
            )
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
