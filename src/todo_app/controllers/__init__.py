from todo_app.services import TodoService


class TodoController:
    """Controller layer — mediates between UI and Service."""

    def __init__(self):
        self.service = TodoService()

    def add_todo(self, title: str, description: str | None = None):
        return self.service.create(title, description)

    def list_todos(self) -> list:
        return self.service.get_all()

    def toggle_complete(self, todo_id: int):
        return self.service.toggle_complete(todo_id)

    def edit_todo(self, todo_id: int, title: str, description: str | None = None):
        return self.service.update(todo_id, title=title, description=description)

    def remove_todo(self, todo_id: int) -> bool:
        return self.service.delete(todo_id)
