import asyncio

from src.factory import BotFactory


if __name__ == "__main__":
    bot_factory = BotFactory()

    asyncio.run(bot_factory.start_bot())
