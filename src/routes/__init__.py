from aiogram import Router

from . import start, name, question, about, menu

router = Router()

router.include_routers(
    about.router,
    start.router,
    menu.router,
    name.router,
    question.router,
)