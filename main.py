""" Main file for service
"""
import os

from fastapi import FastAPI

from api.auth_controller import AuthController
from api.test_controller import TestController


app = FastAPI(title='InstallBiz test task API', description='Task from InstallBiz company')
app.include_router(AuthController.create_router())
app.include_router(TestController.create_router())
