import filters
import middlewares
from bot.utils.notify.admins import on_startup_notify
from bot.utils.notify.admins import on_shutdown_notify
from aiogram import executor
from handlers import dp


async def on_startup(dp):
    filters.setup(dp)
    middlewares.setup(dp)
    await on_startup_notify(dp)
    print("Bot is on.")


async def on_shutdown(dp):
    await on_shutdown_notify(dp)
    print("Bot is off.")


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, on_startup=on_startup,
                           on_shutdown=on_shutdown, skip_updates=True)
