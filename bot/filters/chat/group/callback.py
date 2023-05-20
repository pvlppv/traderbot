from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery


class IsGroupChatCallback(BoundFilter):
    async def check(self, call: CallbackQuery):
        return call.message.chat.type == types.ChatType.SUPERGROUP
