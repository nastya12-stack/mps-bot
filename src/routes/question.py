from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

router = Router()


@router.message(Command("question"))
async def command_about(message: Message) -> None:
    await message.answer("Этот бот сделали @agatyny и @Anastatyahohlova. Если есть проблемы пишите @agatyny.")


@router.callback_query(F.data == "question")
async def on_callback(query: CallbackQuery) -> None:
    await query.message.answer(
        "Этот бот сделали @agatyny и @Anastatyahohlova. Если есть проблемы пишите @agatyny.")
