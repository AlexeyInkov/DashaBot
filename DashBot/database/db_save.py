from peewee import DoesNotExist
from telebot.types import Message
from loguru import logger
from .model import db, User, Command, Task


def save_in_db(message: Message) -> None:
    with db:
        try:
            user = User.select().where(User.user_id == message.from_user.id).get()
        except DoesNotExist:
            user = User.create(
                user_id=message.from_user.id,
                is_bot=message.from_user.is_bot,
                full_name=message.from_user.full_name,
                language_code=message.from_user.language_code,
                is_premium=message.from_user.is_premium or False,
                is_member_club=False
            )
            logger.debug('{} Запись таблицы Users(Создание нового)'.format(message.from_user.full_name))
        Command.create(
            user=user,
            command=message.text,
            chat_id=message.chat.id,
            command_time=message.date,
        ).save()
        logger.debug('{} Запись таблицы Commands. Команда {}'.format(message.from_user.full_name, message.text))


def save_task(message: Message) -> None:
    with db:
        user = User.select().where(User.user_id == message.from_user.id)
        if not user:
            user = User.create(
                user_id=message.from_user.id,
                is_bot=message.from_user.is_bot,
                full_name=message.from_user.full_name,
                language_code=message.from_user.language_code,
                is_premium=message.from_user.is_premium or False,
                is_member_club=False
            )
        Task.create(
            user=user,
            task=message.text,
            date=message.date
        ).save()
