import logging
import traceback

from aiogram import types, Router
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.filters import CommandStart

from app.database import orm_read, orm_create
from app.database import User

logger = logging.getLogger(__name__)

start_router = Router()


@start_router.message(CommandStart())
async def start_cmd(message: types.Message, session: AsyncSession):
    try:
        tg_id = str(message.from_user.id)
        username = message.from_user.username
        user = await orm_read(session, User, as_iterable=False, tg_id=tg_id)

        if not user:
            result = await orm_create(session, User, {"tg_id": tg_id, "username": username})

            if result:
                user = await orm_read(session, User, as_iterable=False, tg_id=tg_id)
            else:
                raise Exception 

        await message.answer(f"Hello, user! Your ID is {user.tg_id}")
    except Exception as e:
        logger.error(f"Short error message: {e}")
        logger.error(traceback.format_exc())
        await message.answer("There was an error 😞...")
