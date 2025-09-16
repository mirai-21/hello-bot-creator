from .start_commands import start_router
from .help_commands import help_router
from .profile_commands import profile_router

# Combine all user routers
from aiogram import Router

user_router = Router()
user_router.include_router(start_router)
user_router.include_router(help_router)
user_router.include_router(profile_router)

__all__ = ['user_router']
