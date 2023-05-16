from loader import dp
from aiogram import types
from filters import IsPrivateChatMessage
import finnhub
from data.config import FinnHub_ApiKey, admins
import asyncio
from keyboards.inline import kb_inline
from states import AddTask, DeleteTask
from aiogram.dispatcher import FSMContext
from loader import db


finnhub_client = finnhub.Client(api_key=FinnHub_ApiKey)
taski = {}


async def get_stock_price(symbol, target_price, admins):
    while True:
        price = finnhub_client.quote(symbol)['c']
        for admin in admins:
            if price >= float(target_price):
                await asyncio.sleep(2)
                await dp.bot.send_message(admin, f'🛑 <b>{symbol}</b> достиг цены в {target_price}$!')
                task_key = f'{symbol}_{target_price}'
                taski[task_key].cancel()
                del taski[task_key]
                db.delete_task_2(symbol, target_price)
        await asyncio.sleep(1)


@dp.message_handler(IsPrivateChatMessage(), text='/start')
async def start(message: types.Message):
    print(taski)
    tasks = db.get_all_tasks()
    if not tasks:
        response = '<i>Нет задач.</i>'
    else:
        response = ''
        for idx, task in enumerate(tasks, 1):
            response += f'{idx}. {task[1]}, {task[2]}\n'
    await message.answer(f'<b>Текущие задачи:</b>\n\n{response}', reply_markup=kb_inline)


@dp.message_handler(text='/cancel', state='*', chat_id=admins)
async def cancel_add_task(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Действие отменено.')


@dp.callback_query_handler(text='add_task')
async def add_task(call: types.CallbackQuery):
    await call.message.answer('Тикер:')
    await AddTask.symbol.set()


@dp.message_handler(IsPrivateChatMessage(), state=AddTask.symbol, chat_id=admins)
async def add_task_symbol(message: types.Message, state: FSMContext):
    symbol = message.text.upper()
    if symbol.isdigit():
        await message.answer('Некорректный тикер.')
        return
    await state.update_data(symbol=symbol)
    await message.answer('Целевая цена ($):')
    await AddTask.target_price.set()


@dp.message_handler(IsPrivateChatMessage(), state=AddTask.target_price, chat_id=admins)
async def add_task_target_price(message: types.Message, state: FSMContext):
    target_price = message.text
    if not target_price.isdigit():
        await message.answer('Некорректная целевая цена.')
        return
    data = await state.get_data()
    symbol = data.get('symbol')
    db.add_task(symbol, target_price)
    task_key = f'{symbol}_{target_price}'
    taski[task_key] = asyncio.create_task(get_stock_price(symbol, target_price, admins))
    await state.finish()
    tasks = db.get_all_tasks()
    if not tasks:
        response = '<i>Нет задач.</i>'
    else:
        response = ''
        for idx, task in enumerate(tasks, 1):
            response += f'{idx}. {task[1]}, {task[2]}\n'
    await message.answer(f'<b>Текущие задачи:</b>\n\n{response}', reply_markup=kb_inline)


@dp.callback_query_handler(chat_id=admins, text='delete_task')
async def delete_task(call: types.CallbackQuery):
    await call.message.answer('Номер задачи для удаления:')
    await DeleteTask.id.set()


@dp.message_handler(IsPrivateChatMessage(), state=DeleteTask.id, chat_id=admins)
async def delete_task_id(message: types.Message, state: FSMContext):
    rowid = message.text
    if not rowid.isdigit() or int(rowid) <= 0:
        await message.answer('Некорректный номер.')
        return
    try:
        tasks = db.get_all_tasks()
        new_rowid = int(rowid) - 1
        task = tasks[new_rowid]
        db.delete_task(task[0])
        task_key = f'{task[1]}_{task[2]}'
        taski[task_key].cancel()
        del taski[task_key]
        await state.finish()
        tasks = db.get_all_tasks()
        if not tasks:
            response = '<i>Нет задач.</i>'
        else:
            response = ''
            for idx, task in enumerate(tasks, 1):
                response += f'{idx}. {task[1]}, {task[2]}\n'
        await message.answer(f'<b>Текущие задачи:</b>\n\n{response}', reply_markup=kb_inline)
    except:
        await message.answer('Некорректный номер.')
        return