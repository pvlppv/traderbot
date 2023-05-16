from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_default = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Test"),
        ],
        [KeyboardButton(text="Test")],
        [
            KeyboardButton(text="Test"),
        ],
    ],
    resize_keyboard=True,
)
