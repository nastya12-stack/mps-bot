from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

router = Router()


@router.message(Command("name"))
async def command_about(message: Message) -> None:
    name = message.from_user.full_name
    await message.answer(f"Your name is {name}.")


@router.callback_query(F.data == "name")
async def on_callback(query: CallbackQuery) -> None:
    name = query.from_user.full_name
    await query.message.answer(f"Your name is {name}.")