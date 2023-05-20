from utils import Environs


class ConfigData:
    BOT_TOKEN: str = Environs.get("BOT_TOKEN")
    CURRENCY_API_TOKEN: str = Environs.get("CURRENCY_API_TOKEN")