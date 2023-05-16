from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_inline = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➕", callback_data="add_task"),
            InlineKeyboardButton(text="➖", callback_data="delete_task"),
        ],
    ],
)
