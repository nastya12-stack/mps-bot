from tkinter.messagebox import Message

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()


def get_description() -> str:
    return "Hello, my friends!"


@router.message(Command("ochenki"))
async def command_ochenki(message: Message) -> None:
    await message.answer(get_description())


@router.callback_query(F.data == "ochenki")
async def on_callback(query: CallbackQuery) -> None:
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Back", callback_data="menu")],
    ])
    await query.message.edit_text(get_description(), reply_markup=markup)
