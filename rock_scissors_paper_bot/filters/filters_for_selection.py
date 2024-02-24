from aiogram.types import Message
from aiogram.filters import BaseFilter
from lexicon.lexicon_ru import LEXICON_RU


class YesAnswer(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.text == LEXICON_RU["yes_button"]


class NoAnswer(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.text == LEXICON_RU["no_button"]
