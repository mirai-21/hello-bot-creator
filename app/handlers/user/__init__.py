from .start_commands import start_router

# Combine all user routers
from aiogram import Router

user_router = Router()
user_router.include_router(start_router)

__all__ = ['user_router']
