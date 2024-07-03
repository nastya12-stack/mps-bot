from aiogram import Router
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

router = Router()


@router.message(Command("menu"))
async def show_menu(message: Message) -> None:
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="What is МШП?", callback_data="about")],
        [InlineKeyboardButton(text="What is my name?", callback_data="name")],
        [InlineKeyboardButton(text="Who created you?", callback_data="question")],
    ])

    await message.answer("Ask me any of these questions.", reply_markup=markup)
