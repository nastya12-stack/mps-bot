from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup
from src import assets

router = Router()


def get_description() -> str:
        return "Что хотите узнать?"


@router.message(Command("about"))
async def command_about(message: Message) -> None:
    await message.answer(get_description())


@router.callback_query(F.data == "about")
async def on_callback(query: CallbackQuery) -> None:
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="menu")],
        [InlineKeyboardButton(text="Немного о школе", callback_data="MSHP")],
        [InlineKeyboardButton(text="О уроках ", callback_data="yrok")],
        [InlineKeyboardButton(text="О учителях", callback_data="teacher")],
        [InlineKeyboardButton(text="Об оценках", callback_data="ochenki")],
        [InlineKeyboardButton(text="Об олимпиадах", callback_data="olimpiada")],
        [InlineKeyboardButton(text="О удобствах", callback_data="ydobctva")],
        [InlineKeyboardButton(text="О минусах", callback_data="minyc")],
        [InlineKeyboardButton(text="Вывод", callback_data="vevod")],
    ])
    await query.message.edit_text(get_description(), reply_markup=markup)

