from aiogram.types import Message
from aiogram.filters import BaseFilter
from lexicon.lexicon_ru import LEXICON_RU


class WichChoice(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.text in (
            LEXICON_RU["rock"],
            LEXICON_RU["scissors"],
            LEXICON_RU["paper"],
        )
