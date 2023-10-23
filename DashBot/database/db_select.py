from peewee import fn

from database.model import db, User, Command
from config_data.config import ADMIN_ID


with db:
    ADMIN = User.get(user_id=ADMIN_ID).full_name


def count_users():
    with db:
        return User.select().count()


def active_user():
    with db:
        user = Command.select(fn.Max(fn.Count(Command.user)).group_by(Command.user))
        print(user)
        return user.get()


def statistic_command():
    with db:
        commands = Command.select(Command.command, fn.Count(Command.command).alias("count"))\
            .group_by(Command.command).order_by('count')
        for command in commands:
            print(command.command, " - ", command.count)
        return commands
