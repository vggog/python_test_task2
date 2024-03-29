from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from .buttons import menu_buttons, subscribe_button
from .states import VendorCodeState
from .service import Service


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


@router.message(F.text == "Получить информацию по товару")
async def get_vendor_code(message: Message, state: FSMContext):
    """Метод для запроса у пользователя артикула"""
    await message.answer("Введите артикул:")
    await state.set_state(VendorCodeState.vendor_code)


@router.message(VendorCodeState.vendor_code)
async def get_info_from_wb(message: Message, state: FSMContext):
    """Метод для получения информации с карточки"""
    service = Service()

    await message.answer(
        service.get_info_from_wb(message.text, message.from_user.id),
        reply_markup=subscribe_button(message.text),
    )
    await state.clear()


@router.callback_query(F.data.startswith("subscribe_"))
async def subscribe_to_notifications(callback: CallbackQuery):
    """Ручка для заненсения информации о подписи на уведосление"""
    await callback.answer()

    service = Service()
    description = service.add_subscribe_to_notification(
        user_id=callback.from_user.id,
        vendor_code=int(callback.data.split("_")[1]),
    )

    await callback.message.answer(description)


@router.message(F.text == "Остановить уведомления")
async def get_query_history(message: Message):
    """Ручка для остановки уведомлений"""
    Service.delete_subscribe(message.from_user.id)
    await message.answer("Уведомления остановлены")


@router.message(F.text == "Получить информацию из БД")
async def get_query_history(message: Message):
    """Ручка для получения истории запросов пользователя"""
    service = Service()

    await message.answer(
        service.get_query_history(message.from_user.id),
        reply_markup=menu_buttons(),
    )
