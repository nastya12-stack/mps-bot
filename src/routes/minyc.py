from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()


def get_description() -> str:
    print("Hello, my friends!")


@router.message(Command("minyc"))
async def command_minyc(message: Message) -> None:
    await message.answer(get_description())


@router.callback_query(F.data == "minyc")
async def on_callback(query: CallbackQuery) -> None:
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Back", callback_data="menu")],
    ])
    await query.message.edit_text(get_description(), reply_markup=markup)
