from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


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


def subscribe_button(vendor_code: str) -> InlineKeyboardMarkup:
    """Inline-кнопка для возможности подписаться на уведомления."""
    keyboard = [
        [
            InlineKeyboardButton(
                text="Подписаться на уведомления",
                callback_data=f"subscribe_{vendor_code}"
            ),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
