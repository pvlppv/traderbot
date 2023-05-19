from aiogram import types
from buttons import ReplyKeyboardsButtons


class ReplyKeyboards:
    async def __init__(self) -> None:
        self.keyboard = types.ReplyKeyboardMarkup(row_width=1,
                                                  resize_keyboard=True)
        self.buttons = ReplyKeyboardsButtons()

    async def test(self) -> types.ReplyKeyboardMarkup:
        return self.keyboard.add(self.buttons.test,
                                 self.buttons.test, self.buttons.test)
