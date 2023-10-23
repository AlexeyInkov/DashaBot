from telebot.handler_backends import State, StatesGroup


class UserInfoState(StatesGroup):
    todo = State()
    baw = State()
    background = State()
    sticker = State()


def get_action(state: UserInfoState):
    if state == 'UserInfoState:sticker':
        return "photo_to_sticker"
    elif state == 'UserInfoState:baw':
        return "change_to_baw"
    elif state == 'UserInfoState:background':
        return "remove_background"
