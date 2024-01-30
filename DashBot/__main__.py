from telebot.types import BotCommand

from config_data.config import COMMANDS
from database.model import db, close_db
from loader import bot
import handlers
from telebot.custom_filters import StateFilter
# from no_close import keep_alive

from loguru import logger


if __name__ == "__main__":
    try:
        bot.add_custom_filter(StateFilter(bot))
        bot.set_my_commands([BotCommand(i, COMMANDS[i][0]) for i in COMMANDS])
        
        # keep_alive()  # обманка для Replit
        
        bot.polling(none_stop=True)

    except Exception:
        import traceback
        logger.warning(traceback.format_exc())
    finally:
        close_db(db)
