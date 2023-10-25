from peewee import fn, SQL

from database.model import db, User, Command
from config_data.config import ADMIN_ID


with db:
    ADMIN = User.get(user_id=ADMIN_ID).full_name


def count_users():
    with db:
        return User.select().count()


def active_user():
    with db:
        user = Command.select(Command.user.full_name, Command.user.user_id, fn.Count(Command.user).alias('count')).\
            join(User). \
            group_by(Command.user). \
            order_by(SQL('-count')).limit(1)
        return f"{user[0].user.full_name} id({user[0].user.user_id})"


def statistic_command():
    with db:
        answer = "\n"
        commands = Command.select(Command.command, fn.Count(Command.command).alias("count"))\
            .group_by(Command.command).order_by(SQL('-count'))
        for command in commands:
            answer += f'команду {command.command[1:]} вызывали {command.count} раз\n'
        return answer
