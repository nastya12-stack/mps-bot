from tkinter.messagebox import Message

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from src import assets

router = Router()


# def get_description() -> str:
#    filepath = assets.path_to("ochenki.txt")
#    with open(filepath, "r", encoding="utf-8") as my_file:
#       return my_file.read()


def get_description() -> str:
    filepath = assets.path_to("teacher")
    with open(filepath, "r", encoding="utf-8") as my_file:
        return my_file.read()


@router.message(Command("teacher"))
async def command_teacher(message: Message) -> None:
    await message.answer(get_description())


@router.callback_query(F.data == "teacher")
async def on_callback(query: CallbackQuery) -> None:
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Back", callback_data="menu")],
    ])
    await query.message.edit_text(get_description(), reply_markup=markup)
