from buttons.buttons_for_selection import yes_button, no_button
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


yes_or_no_keyboard_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
yes_or_no_keyboard_builder.row(yes_button, no_button, width=2)

yes_or_no_keyboard: ReplyKeyboardMarkup = yes_or_no_keyboard_builder.as_markup(
    one_time_keyboard=True, resize_keyboard=True
)
