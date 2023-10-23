import asyncio

from telebot.types import Message

from config_data.config import COMMANDS
from database.db_select import count_users, active_user, statistic_command, ADMIN
from loader import bot


def command_answer(message: Message):
    if message.text[1:] == 'start':
        return f"Привет, {message.from_user.full_name}!\n" \
              f"Меня зовут {bot.get_me().full_name}\n" \
              f"Я хочу учится, чтобы быть тебе полезным\n" \
              f"чтобы предложить идею, набери /todo и я буду это изучать\n" \
              f"Чтобы узнать, что я уже умею, набери /help или выбери команду\n" \
              f"Сейчас я помогаю всем, по позже я буду дружить только с друзьями <u>{ADMIN}</u> \n"
    elif message.text[1:] == 'help':
        return "\n".join([f"/{command} - {desc[0]}" for command, desc in COMMANDS.items()])
    elif message.text[1:] == 'baw':
        return 'Пришли картинку я сделаю ее ч/б'
    elif message.text[1:] == 'background':
        return 'Пришли картинку я удалю фон'
    elif message.text[1:] == 'sticker':
        return 'Пришли картинку я верну стикер'
    elif message.text[1:] == 'todo':
        return f"Привет, {message.from_user.full_name}!\n" \
               f"Напиши мне, что я должен научиться делать и я это буду изучать"
    elif message.text[1:] == 'statistic':
        return f"Привет, {message.from_user.full_name}!\n"\
               f"Я работал с {count_users()} users\n"\
               f"Самый активный user {active_user()}\n"\
               f"Статистика по командам{statistic_command()}\n"



