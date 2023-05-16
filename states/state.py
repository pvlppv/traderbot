from aiogram.dispatcher.filters.state import StatesGroup, State


class AddTask(StatesGroup):
    symbol = State()
    target_price = State()

class DeleteTask(StatesGroup):
    id = State()