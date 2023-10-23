from telebot import TeleBot
from telebot import StateMemoryStorage
from loguru import logger

from config_data import config


storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)
logger.add('../log/info.log', format='{time} {level} {message}', rotation='200kB', compression='zip')
logger.info('Bot загрузился')
