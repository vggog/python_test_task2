import requests

from .schemas import CardSchema
from .config import statics
from .repository import Repository
from .models import QueryHistoryModel, SubscriptionToNotificationsModel


class Service:

    @staticmethod
    def get_info_from_wb(
            vendor_code: str,
            user_id: int,
            repository: Repository = Repository()
    ) -> str:
        """Метод для получения карточки товара."""
        info = requests.get(statics.card_info_url + vendor_code)

        if info.status_code != 200:
            return "Возникла ошибка"

        try:
            card_info = CardSchema(**(info.json()["data"]["products"][0]))
        except IndexError:
            return "Карточка не найдена, возможно артикул не верный"

        repository.add_record(
            user_id=user_id,
            vendor_code=int(vendor_code),
            table=QueryHistoryModel,
        )

        return (
                f"Название товара: {card_info.name}\n"
                f"Артикул: {card_info.id}\n"
                f"Цена: {card_info.salePriceU / 100} руб.\n"
                f"Рейтинг: {card_info.supplierRating}\n"
                f"Количество на всех складах: {card_info.wh}\n"
        )

    def get_query_history(
            self,
            user_id: int,
            repository=Repository()
    ) -> str:
        """Метод для получения истории запросов"""
        query_history = (
            "Дата    |    Артикул\n"
        )

        queries = repository.get_last_five_queries(user_id=user_id)
        for query in queries:
            query_history += f"{query.created_at: %d.%m.%Y} | {query.vendor_code} \n"

        return query_history

    @staticmethod
    def add_subscribe_to_notification(
            user_id: int,
            vendor_code: int,
            repository: Repository = Repository(),
    ) -> str:
        """Сервис для возможности подписаться на уведомления"""
        if repository.is_subscribe_in_db(user_id, vendor_code) is not None:
            return "Вы уже подписаны на уведомление"

        repository.add_record(
            user_id=user_id,
            vendor_code=vendor_code,
            table=SubscriptionToNotificationsModel,
        )

        return "Вы подписались на уведомления"

    @staticmethod
    def delete_subscribe(
            user_id: int,
            repository: Repository = Repository(),
    ):
        """Сервис для остановки подписка на уведомления"""
        repository.delete_subscribe(user_id)
