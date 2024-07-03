from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup
from src import assets

router = Router()


def get_description() -> str:
    filepath = assets.path_to("description.txt")
    with open(filepath, encoding="utf-8") as text_file:
        return text_file.read()


@router.message(Command("about"))
async def command_about(message: Message) -> None:
    await message.answer(get_description())


@router.callback_query(F.data == "about")
async def on_callback(query: CallbackQuery) -> None:
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Back", callback_data="menu")],
    ])
    await query.message.edit_text(get_description(), reply_markup=markup)
