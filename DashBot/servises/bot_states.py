from telebot.handler_backends import State, StatesGroup


class UserInfoState(StatesGroup):
    todo = State()
    baw = State()
    background = State()
    sticker = State()
