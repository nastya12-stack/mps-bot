from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

router = Router()


def gen_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Что такое МШП?", callback_data="about")],
        [InlineKeyboardButton(text="Как меня зовут?", callback_data="name")],
        [InlineKeyboardButton(text="Кто создал бота?", callback_data="question")],
    ])


@router.message(Command("menu"))
async def show_menu(message: Message) -> None:
    markup = gen_markup()

    await message.answer("Что вы хотите узнать?", reply_markup=markup)


@router.callback_query(F.data == "menu")
async def return_to_menu(query: CallbackQuery) -> None:
    markup = gen_markup()

    await query.message.edit_text("Что вы хотите узнать?", reply_markup=markup)
