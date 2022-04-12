from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton(text="Deliver")
        ],
        [
            KeyboardButton(text="Order"),
            KeyboardButton(text="Tester")
        ],
    ],
    resize_keyboard=True
)