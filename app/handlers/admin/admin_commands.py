import traceback
import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.filters import IsAdmin

logger = logging.getLogger(__name__)

admin_router = Router()
admin_router.message.filter(IsAdmin())


@admin_router.message(Command("admin"))
async def admin_features(message: Message, state: FSMContext):
    try:
        await state.clear()
        await message.answer("Hello, admin!")
    except Exception as e:
        logger.error(f"Short error message: {e}")
        logger.error(traceback.format_exc())
        await message.answer("There was an error 😞...")
