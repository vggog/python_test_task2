import os

from .schemas import BotSettings


bot_settings = BotSettings(
    token=os.getenv("TOKEN"),
)
