from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery


class IsPrivateChatCallback(BoundFilter):
    async def check(self, call: CallbackQuery):
        return call.message.chat.type == types.ChatType.PRIVATE
