from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass
class BotSettings:
    token: str


@dataclass
class Statics:
    card_info_url: str
