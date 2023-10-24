import os
from dotenv import load_dotenv, find_dotenv
from telebot import TeleBot
from telebot.types import BotCommand

from servises.bot_states import UserInfoState

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")
DEVELOPER_ID = os.getenv("DEVELOPER_ID")

COMMANDS = {
    "start": ("Запустить бота",),
    "help": ("Вывести справку",),
    "baw": ("Цветное фото в оттенки серого", UserInfoState.baw),
    "background": ("Удаляем фон на фото", UserInfoState.background),
    "sticker": ("Стикер из фото", UserInfoState.sticker),
    "statistic": ("Статистика",),
    "todo": ("Книга жалоб и предложений", UserInfoState.todo)
}
