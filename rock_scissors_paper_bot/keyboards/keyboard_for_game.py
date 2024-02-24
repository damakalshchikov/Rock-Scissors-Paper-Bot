from buttons.buttons_for_game import rock_button, scissors_button, paper_button
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


game_keyboard_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
game_keyboard_builder.row(rock_button, scissors_button, paper_button, width=1)

game_keyboard: ReplyKeyboardMarkup = game_keyboard_builder.as_markup(
    resize_keyboard=True
)
