import os

from .schemas import BotSettings, Statics, DBConfig, RabbitMQConfig


bot_settings = BotSettings(
    token=os.getenv("TOKEN"),
)

statics = Statics(
    card_info_url="https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm="
)

db_config = DBConfig(
    db=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT")
)

rabbitmq_config = RabbitMQConfig(
    user=os.getenv('RABBITMQ_DEFAULT_USER'),
    password=os.getenv('RABBITMQ_DEFAULT_PASS'),
    port=os.getenv('RABBITMQ_DEFAULT_PORT'),
    host=os.getenv('RABBITMQ_HOST'),
)
