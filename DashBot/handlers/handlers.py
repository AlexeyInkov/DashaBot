import os

from telebot.types import Message

from config_data.config import COMMANDS, DEVELOPER_ID
from database.db_save import save_in_db, save_task
from loader import bot, logger
from servises.bot_states import UserInfoState, get_action
from servises.photo import change_image
from template.answer_text import command_answer


@bot.message_handler(commands=[i for i in COMMANDS])
def bot_select_command(message: Message):
    text = command_answer(message)
    logger.info('{} (id {}) ввел команду {}'.format(
        message.from_user.full_name,
        message.from_user.id,
        message.text[1:]
    ))
    if message.text[1:] in ('start', 'help', 'statistic'):
        bot.delete_state(message.from_user.id, message.chat.id)
    else:
        bot.set_state(message.from_user.id, COMMANDS.get(message.text[1:])[1], message.chat.id)
    save_in_db(message)
    bot.reply_to(message, text, parse_mode='HTML')


@bot.message_handler(content_types=['photo'])
def bot_select_state(message: Message):
    state = bot.get_state(message.from_user.id, message.chat.id)
    action = get_action(state)
    if action:
        file_path = change_image(message.photo[2].file_id, action)
        if state == 'UserInfoState:sticker':
            bot.send_sticker(message.chat.id, open(file_path, "rb"))
        else:
            bot.send_photo(message.chat.id, open(file_path, "rb"))
        bot.delete_state(message.from_user.id, message.chat.id)
        os.remove(file_path)
        logger.info('{} (id {}) команда {}, прислал картинку, статус удален, отправлен ответ, файл удален'.format(
            message.from_user.full_name,
            message.from_user.id, action))
    else:
        logger.info('{} (id {}) состояние {}, прислал картинку'.format(
            message.from_user.full_name,
            message.from_user.id,
            action)
        )
        bot.send_message(message.from_user.id, 'Классное фото, сначала выбери команду')


@bot.message_handler(state=UserInfoState.todo)
def bot_send_todo_developer(message: Message):
    bot.forward_message(DEVELOPER_ID, message.chat.id, message.message_id)
    # Добавляем задание в БД
    save_task(message)
    # TODO Проверять выполнение задания по БД
    bot.delete_state(message.from_user.id, message.chat.id)
    logger.info('{} (id {}) команда {} задание отправлено состояние удалено'.format(
        message.from_user.full_name,
        message.from_user.id, 'todo'))
    save_task(message)
