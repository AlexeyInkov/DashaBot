import asyncio

from telebot.types import Message

from config_data.config import COMMANDS, DEVELOPER_ID, ADMIN_ID
from database.db_select import count_users, active_user, statistic_command, ADMIN
from loader import bot


def command_answer(message: Message):
    answer = {'start': f"Привет, {message.from_user.full_name}!\n"
                       f"Меня зовут {bot.get_me().full_name}\n"
                       f"Я хочу учится, чтобы быть тебе полезным\n"
                       f"Предложи идею, набери /todo и я буду это изучать\n"
                       f"Узнать, что я уже умею, набери /help\n"
                       f"Сейчас я помогаю всем, по позже я буду дружить только с друзьями <u>{ADMIN}</u> \n",

              "help": "\n".join([f"/{command} - {desc[0]}" for command, desc in COMMANDS.items()]),

              'baw': 'Пришли картинку я сделаю ее ч/б',

              'background': 'Пришли картинку я удалю фон',

              'sticker': 'Пришли картинку я верну стикер',

              'todo': f"Привет, {message.from_user.full_name}!\n"
                      f"Напиши мне, что я должен научиться делать и я это буду изучать"
              }

    if message.text[1:] == 'statistic':
        if message.from_user.id in map(int, (ADMIN_ID, DEVELOPER_ID)):
            return f"Привет, {message.from_user.full_name}!\n\n" \
                   f"Я работал с {count_users()} users\n\n" \
                   f"Самый активный user {active_user()}\n\n" \
                   f"Статистика по командам:{statistic_command()}\n"
        else:
            return f"{message.from_user.full_name}!\nВы не можете смотреть этот раздел"
    else:
        return answer.get(message.text[1:])

