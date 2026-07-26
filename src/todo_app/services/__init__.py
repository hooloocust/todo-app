from todo_app.models import Todo


class TodoService:
    """Service layer — business logic for Todo CRUD."""

    @staticmethod
    def create(title: str, description: str | None = None) -> Todo:
        return Todo.create(title=title, description=description)

    @staticmethod
    def get_all() -> list[Todo]:
        return list(Todo.select().order_by(Todo.created_at.desc()))

    @staticmethod
    def get_by_id(todo_id: int) -> Todo | None:
        try:
            return Todo.get_by_id(todo_id)
        except Todo.DoesNotExist:
            return None

    @staticmethod
    def toggle_complete(todo_id: int) -> Todo | None:
        todo = TodoService.get_by_id(todo_id)
        if todo:
            todo.is_completed = not todo.is_completed
            todo.save()
        return todo

    @staticmethod
    def update(todo_id: int, **fields) -> Todo | None:
        todo = TodoService.get_by_id(todo_id)
        if todo:
            for key, value in fields.items():
                setattr(todo, key, value)
            todo.save()
        return todo

    @staticmethod
    def delete(todo_id: int) -> bool:
        todo = TodoService.get_by_id(todo_id)
        if todo:
            todo.delete_instance()
            return True
        return False
