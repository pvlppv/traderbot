from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery


class IsPrivateChatMessage(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE
