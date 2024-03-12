import requests

from .schemas import CardSchema
from .config import statics


class Service:

    @staticmethod
    def get_info_from_wb(vendor_code: str) -> str:
        """Метод для получения карточки товара."""
        info = requests.get(statics.card_info_url + vendor_code)

        if info.status_code != 200:
            return "Возникла ошибка"

        try:
            card_info = CardSchema(**(info.json()["data"]["products"][0]))
        except IndexError:
            return "Карточка не найдена, возможно артикул не верный"

        return (
                f"Название товара: {card_info.name}\n"
                f"Рейтинг: {card_info.id}\n"
                f"Цена: {card_info.salePriceU / 100} руб.\n"
                f"Рейтинг: {card_info.supplierRating}\n"
                f"Количество на всех складах: {card_info.wh}\n"
        )
