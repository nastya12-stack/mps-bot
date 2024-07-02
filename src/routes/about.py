from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

router = Router()


def get_description() -> str:
    with open("assets/description.txt", encoding="utf-8") as text_file:
        return text_file.read()


@router.message(Command("about"))
async def command_about(message: Message) -> None:
    await message.answer(get_description())


@router.callback_query(F.data == "about")
async def on_callback(query: CallbackQuery) -> None:
    await query.message.answer(get_description())
