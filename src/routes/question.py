from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

router = Router()


@router.message(Command("question"))
async def command_about(message: Message) -> None:
    await message.answer("This bot was created by @agatyny and @Anastatyahohlova. If there are some problems write @agatyny")

@router.callback_query(F.data == "question")
async def on_callback(query: CallbackQuery) -> None:
    await query.message.answer(
        "This bot was created by @agatyny and @Anastatyahohlova. If there are some problems write @agatyny")
