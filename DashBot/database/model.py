from peewee import SqliteDatabase, Model, PrimaryKeyField, ForeignKeyField
from peewee import CharField, IntegerField, DateTimeField, BooleanField, TextField


db = SqliteDatabase('./DashBot/database/stat.db')


def close_db(database: SqliteDatabase):
    database.close()


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class User(BaseModel):
    user_id = IntegerField(unique=True)
    is_bot = BooleanField()
    full_name = CharField(max_length=100)
    language_code = CharField(max_length=20)
    is_premium = BooleanField()
    is_member_club = BooleanField(default=False)

    class Meta:
        bd_table = 'users'


class Command(BaseModel):
    user = ForeignKeyField(User)
    command = CharField()
    chat_id = IntegerField()
    command_time = DateTimeField()

    class Meta:
        bd_table = 'commands'


class Task(BaseModel):
    user = ForeignKeyField(User)
    task = TextField()
    date = DateTimeField()
    is_close = BooleanField(default=False)

    class Meta:
        bd_table = 'tasks'


with db:
    db.create_tables([Command, User, Task])
