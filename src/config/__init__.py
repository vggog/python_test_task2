import os

from .schemas import BotSettings, Statics


bot_settings = BotSettings(
    token=os.getenv("TOKEN"),
)

statics = Statics(
    card_info_url="https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm="
)
