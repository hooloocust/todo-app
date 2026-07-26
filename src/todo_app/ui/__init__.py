import tkinter as tk
from tkinter import messagebox, ttk

from todo_app.controllers import TodoController


class TodoApp:
    """UI layer — Tkinter frontend."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("📝 Todo App")
        self.root.geometry("650x500")
        self.root.resizable(False, False)

        self.controller = TodoController()
        self.selected_todo_id = None

        self._build_ui()
        self._refresh_list()

    # ── UI Construction ──────────────────────────────────────────────

    def _build_ui(self):
        # ── Input Frame ──
        input_frame = tk.LabelFrame(self.root, text="New Todo", padx=10, pady=10)
        input_frame.pack(fill="x", padx=10, pady=(10, 5))

        tk.Label(input_frame, text="Title:").grid(row=0, column=0, sticky="w")
        self.title_entry = tk.Entry(input_frame, width=50)
        self.title_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Description:").grid(row=1, column=0, sticky="w", pady=5)
        self.desc_entry = tk.Entry(input_frame, width=50)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5)

        btn_frame = tk.Frame(input_frame)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=5)

        tk.Button(btn_frame, text="➕ Add", width=12, command=self._add_todo).pack(side="left", padx=5)
        tk.Button(btn_frame, text="✏️ Edit", width=12, command=self._edit_todo).pack(side="left", padx=5)
        tk.Button(btn_frame, text="🗑️ Delete", width=12, command=self._delete_todo).pack(side="left", padx=5)
        tk.Button(btn_frame, text="✅ Toggle", width=12, command=self._toggle_todo).pack(side="left", padx=5)

        # ── List Frame ──
        list_frame = tk.LabelFrame(self.root, text="Todos", padx=10, pady=10)
        list_frame.pack(fill="both", expand=True, padx=10, pady=(5, 10))

        columns = ("id", "title", "status", "created")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=12)
        self.tree.heading("id", text="ID")
        self.tree.heading("title", text="Title")
        self.tree.heading("status", text="Status")
        self.tree.heading("created", text="Created At")
        self.tree.column("id", width=40, anchor="center")
        self.tree.column("title", width=280)
        self.tree.column("status", width=80, anchor="center")
        self.tree.column("created", width=160, anchor="center")

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.tree.bind("<<TreeviewSelect>>", self._on_select)

    # ── Data Operations ──────────────────────────────────────────────

    def _refresh_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for todo in self.controller.list_todos():
            status = "✅ Done" if todo.is_completed else "⏳ Pending"
            created = todo.created_at.strftime("%Y-%m-%d %H:%M")
            self.tree.insert("", "end", iid=str(todo.id), values=(todo.id, todo.title, status, created))

        self._clear_fields()

    def _on_select(self, event):
        selected = self.tree.selection()
        if selected:
            todo_id = int(selected[0])
            self.selected_todo_id = todo_id
            todo = self.controller.service.get_by_id(todo_id)
            if todo:
                self.title_entry.delete(0, tk.END)
                self.title_entry.insert(0, todo.title)
                self.desc_entry.delete(0, tk.END)
                if todo.description:
                    self.desc_entry.insert(0, todo.description)

    def _clear_fields(self):
        self.title_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.selected_todo_id = None

    # ── Actions ──────────────────────────────────────────────────────

    def _add_todo(self):
        title = self.title_entry.get().strip()
        if not title:
            messagebox.showwarning("Warning", "Title is required!")
            return
        description = self.desc_entry.get().strip() or None
        self.controller.add_todo(title, description)
        self._refresh_list()

    def _edit_todo(self):
        if not self.selected_todo_id:
            messagebox.showwarning("Warning", "Select a todo first!")
            return
        title = self.title_entry.get().strip()
        if not title:
            messagebox.showwarning("Warning", "Title is required!")
            return
        description = self.desc_entry.get().strip() or None
        self.controller.edit_todo(self.selected_todo_id, title, description)
        self._refresh_list()

    def _delete_todo(self):
        if not self.selected_todo_id:
            messagebox.showwarning("Warning", "Select a todo first!")
            return
        if messagebox.askyesno("Confirm", "Delete this todo?"):
            self.controller.remove_todo(self.selected_todo_id)
            self._refresh_list()

    def _toggle_todo(self):
        if not self.selected_todo_id:
            messagebox.showwarning("Warning", "Select a todo first!")
            return
        self.controller.toggle_complete(self.selected_todo_id)
        self._refresh_list()
