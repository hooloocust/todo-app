# 📝 Todo App

A single-user Todo desktop application built with Python, Tkinter, and Peewee ORM.

## Architecture (C4 Model)

```
Layer 1: User → System
Layer 2: Desktop App (SQLite3)
Layer 3: UI (Tkinter) → Controller → Service → ORM (Peewee)
```

## Features

- ✅ Add new todos with title and description
- ✏️ Edit existing todos
- 🗑️ Delete todos
- ✅ Toggle completion status
- 📊 View all todos in a table

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/todo-app.git
cd todo-app

# Install dependencies with uv
uv sync

# Run the application
uv run todo
```

## Project Structure

```
todo-app/
├── src/todo_app/
│   ├── __init__.py
│   ├── main.py          # Entry point
│   ├── db/              # Database configuration
│   │   └── __init__.py
│   ├── models/          # Peewee ORM models
│   │   └── __init__.py
│   ├── services/        # Business logic
│   │   └── __init__.py
│   ├── controllers/     # Controller layer
│   │   └── __init__.py
│   └── ui/              # Tkinter UI
│       └── __init__.py
├── pyproject.toml       # Project configuration
└── README.md
```

## Development

```bash
# Add dependencies
uv add <package>

# Run in development mode
uv run python -m todo_app.main
```

## License

MIT
