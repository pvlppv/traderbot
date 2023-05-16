from aiogram.dispatcher.filters.state import State, StatesGroup


class AddTask(StatesGroup):
    symbol = State()
    target_price = State()


class DeleteTask(StatesGroup):
    id = State()
