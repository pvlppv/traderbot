from aiogram import Dispatcher
from filters.chat.group import IsGroupChatCallback, IsGroupChatMessage
from filters.chat.private import IsPrivateChatCallback, IsPrivateChatMessage
from middlewares import ThrottlingMiddleware


def setup(dp: Dispatcher) -> None:
    dp.middleware.setup(ThrottlingMiddleware())
    dp.filters_factory.bind(IsPrivateChatMessage)
    dp.filters_factory.bind(IsPrivateChatCallback)
    dp.filters_factory.bind(IsGroupChatMessage)
    dp.filters_factory.bind(IsGroupChatCallback)
