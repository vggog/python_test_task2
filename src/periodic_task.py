from aiogram import Bot

from .repository import Repository
from .service import Service


async def send_notification(bot: Bot):
    """
    Переодичная задача для отправки карточки товара тем,
    кто подписался на уведомление
    """
    repository = Repository()
    service = Service()

    all_subscribers = repository.get_all_subscribers_for_notifications()

    for subscriber in all_subscribers:
        status, info = service.info_from_card(str(subscriber.vendor_code))
        if not status:
            continue

        await bot.send_message(subscriber.user_id, info)
