from aiogram import types


class InlineKeyboardsButtons:
    async def __init__(self) -> None:
        self.button = types.InlineKeyboardButton

    @property
    async def add_task(self) -> types.InlineKeyboardButton:
        return self.button(text="➕", callback_data="add_task")

    @property
    async def delete_task(self) -> types.InlineKeyboardButton:
        return self.button(text="➖", callback_data="delete_task")
