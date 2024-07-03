from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

router = Router()


def gen_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Что такое МШП?", callback_data="about")],
        [InlineKeyboardButton(text="What is my name?", callback_data="name")],
        [InlineKeyboardButton(text="Who created you?", callback_data="question")],
    ])


@router.message(Command("menu"))
async def show_menu(message: Message) -> None:
    markup = gen_markup()

    await message.answer("Ask me any of these questions.", reply_markup=markup)


@router.callback_query(F.data == "menu")
async def return_to_menu(query: CallbackQuery) -> None:
    markup = gen_markup()

    await query.message.edit_text("Ask me any of these questions.", reply_markup=markup)
