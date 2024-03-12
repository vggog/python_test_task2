from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def menu_buttons() -> ReplyKeyboardMarkup:
    """Кнопки меню"""
    keyboard = [
        [KeyboardButton(text="Получить информацию по товару"), ],
        [KeyboardButton(text="Остановить уведомления"), ],
        [KeyboardButton(text="Получить информацию из БД"), ],
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )
