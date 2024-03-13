from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher

from .router import router
from .config import bot_settings
from .periodic_task import send_notification


class BotFactory:

    def __init__(
            self,
            bot: Bot = Bot(bot_settings.token),
            dp: Dispatcher = Dispatcher(),
            scheduler: AsyncIOScheduler = AsyncIOScheduler(),
    ):
        self.dp = dp
        self.bot = bot
        self.scheduler = scheduler

    async def start_bot(self):
        self._include_routers()
        self._add_periodic_task()

        self.scheduler.start()
        await self.dp.start_polling(self.bot)

    def _include_routers(self):
        self.dp.include_router(router)

    def _add_periodic_task(self):
        self.scheduler.add_job(
            send_notification,
            "interval",
            minutes=5,
            args=(self.bot, )
        )
