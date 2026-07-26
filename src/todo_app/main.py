#!/usr/bin/env python3
"""Todo App — Single-user desktop application.

Architecture (C4):
  Layer 1: User → System
  Layer 2: Desktop App (SQLite3)
  Layer 3: UI (Tkinter) → Controller → Service → ORM (Peewee)
"""

import tkinter as tk

from todo_app.db import db
from todo_app.models import Todo
from todo_app.ui import TodoApp


def main():
    # Initialize database
    db.init("todo.db")
    db.connect()
    db.create_tables([Todo])

    # Launch UI
    root = tk.Tk()
    TodoApp(root)
    root.mainloop()

    # Cleanup
    if not db.is_closed():
        db.close()


if __name__ == "__main__":
    main()
