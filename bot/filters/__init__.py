from aiogram import Dispatcher

from .IsGroupChatMessage import IsGroupChatCallback, IsGroupChatMessage
from .IsPrivateChatMessage import IsPrivateChatCallback, IsPrivateChatMessage


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivateChatMessage)
    dp.filters_factory.bind(IsPrivateChatCallback)
    dp.filters_factory.bind(IsGroupChatMessage)
    dp.filters_factory.bind(IsGroupChatCallback)
