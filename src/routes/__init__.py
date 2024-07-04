from aiogram import Router

from . import start, name, question, about, menu, ochenki, minyc, MSHP, olimpiada, teacher, vevod, ydobstva, yrok

router = Router()

router.include_routers(
    about.router,
    start.router,
    menu.router,
    name.router,
    question.router,
    ochenki.router,
    minyc.router,
    MSHP.router,
    olimpiada.router,
    teacher.router,
    vevod.router,
    ydobstva.router,
    yrok.router,
)