from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from .buttons import menu_buttons


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        f'Приветствую <a href="t.me/'f'{message.from_user.username}">'
        f'{message.from_user.first_name}</a>!!!',
        disable_web_page_preview=True,
        parse_mode="HTML",
        reply_markup=menu_buttons(),
    )
