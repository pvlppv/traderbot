from aiogram import types
from keyboards.inline.buttons import InlineKeyboardsButtons


class InlineKeyboards:
    async def __init__(self) -> None:
        self.keyboard = types.InlineKeyboardMarkup(row_width=1)
        self.buttons = InlineKeyboardsButtons()

    async def manage_task(self) -> types.InlineKeyboardButton:
        return self.keyboard.add(self.buttons.add_task, 
                                 self.buttons.delete_task)
