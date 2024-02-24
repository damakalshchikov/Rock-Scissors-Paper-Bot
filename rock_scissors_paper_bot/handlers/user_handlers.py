from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from filters.filters_for_selection import YesAnswer, NoAnswer
from filters.game_filter import WichChoice
from keyboards.keyboard_for_game import game_keyboard
from keyboards.keyboard_for_selection import yes_or_no_keyboard
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_bot_choice, get_winner


router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU["/start"],
        reply_markup=yes_or_no_keyboard
    )


@router.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(
        text=LEXICON_RU["/help"],
        reply_markup=yes_or_no_keyboard
    )


@router.message(YesAnswer())
async def process_yes_answer(message: Message):
    await message.answer(
        text=LEXICON_RU["yes"],
        reply_markup=game_keyboard
    )


@router.message(NoAnswer())
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU["no"])


@router.message(WichChoice())
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()

    await message.answer(
        text=f"{LEXICON_RU["bot_choice"]} - {LEXICON_RU[bot_choice]}"
    )

    winner = get_winner(message.text, bot_choice)

    await message.answer(
        text=LEXICON_RU[winner],
        reply_markup=yes_or_no_keyboard
    )
