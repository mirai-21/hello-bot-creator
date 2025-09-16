from .admin_commands import admin_router as admin_cmd_router

# Combine all admin routers
from aiogram import Router

admin_router = Router()
admin_router.include_router(admin_cmd_router)

__all__ = ['admin_router']
