from datetime import datetime

from peewee import (
    AutoField,
    BooleanField,
    CharField,
    DateTimeField,
    Model,
    TextField,
)

from todo_app.db import db


class Todo(Model):
    id = AutoField(primary_key=True)
    title = CharField(max_length=200)
    description = TextField(null=True)
    is_completed = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = "todos"

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)
