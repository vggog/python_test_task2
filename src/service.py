import requests

from .schemas import CardSchema
from .config import statics
from .repository import Repository


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

        repository.add_query_to_history(
            user_id=user_id,
            vendor_code=int(vendor_code),
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
