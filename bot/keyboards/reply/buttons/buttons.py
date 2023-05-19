from aiogram import types


class ReplyKeyboardsButtons:
    async def __init__(self) -> None:
        self.button = types.KeyboardButton

    @property
    async def test(self) -> types.KeyboardButton:
        return self.button(text="Test")