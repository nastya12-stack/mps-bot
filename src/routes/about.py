from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from src import assets

router = Router()


def get_minuc() -> str:
    filepath = assets.path_to("minuc.txt")
    with open(filepath, encoding="utf-8") as text_file:
        return text_file.read()


@router.message(Command("about"))
async def command_about(message: Message) -> None:
    await message.answer(get_minuc())

@router.callback_query(F.data == "about")
async def on_callback(query: CallbackQuery) -> None:
    await query.message.answer(get_minuc())
