from aiogram import Bot, Dispatcher

from .router import router
from .config import bot_settings


class BotFactory:

    def __init__(
            self,
            bot: Bot = Bot(bot_settings.token),
            dp: Dispatcher = Dispatcher(),
    ):
        self.dp = dp
        self.bot = bot

    async def start_bot(self):
        self._include_routers()
        await self.dp.start_polling(self.bot)

    def _include_routers(self):
        self.dp.include_router(router)
