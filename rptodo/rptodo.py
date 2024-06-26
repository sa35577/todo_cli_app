"""This module provides the RP To-Do model-controller."""
# rptodo/rptodo.py

from pathlib import Path
from typing import Any, Dict, List, NamedTuple

from rptodo import DB_READ_ERROR, ID_ERROR
from rptodo.database import DatabaseHandler

class CurrentTodo(NamedTuple):
    todo: Dict[str, Any]
    error: int

class Todoer:
    def __init__(self, db_path: Path) -> None:
        self._db_handler = DatabaseHandler(db_path)

    def add(self, description: List[str], priority: int = 2) -> CurrentTodo:
        """Add a new to-do to the database."""
        description_text = " ".join(description)
        if not description_text.endswith("."):
            description_text += "."
        todo = {
            "Description": description_text,
            "Priority": priority,
            "Done": False,
        }
        read = self._db_handler.read_todos()
        if read.error == DB_READ_ERROR:
            return CurrentTodo(todo, read.error)
        read.todo_list.append(todo)
        write = self._db_handler.write_todos(read.todo_list)
        return CurrentTodo(todo, write.error)

    def get_todo_list(self) -> List[Dict[str, Any]]:
        """List all to-dos from the database."""
        return self._db_handler.read_todos().todo_list
    
    def set_done(self, todo_id: int) -> CurrentTodo:
        """Set the to-do as done."""
        read = self._db_handler.read_todos()
        if read.error:
            return CurrentTodo({}, read.error)
        try:
            read.todo_list[todo_id - 1]["Done"] = True
        except IndexError:
            return CurrentTodo({}, ID_ERROR)
        write = self._db_handler.write_todos(read.todo_list)
        return CurrentTodo(read.todo_list[todo_id - 1], write.error)
    
    def remove(self, todo_id: int) -> CurrentTodo:
        """Delete a to-do from the database."""
        read = self._db_handler.read_todos()
        if read.error:
            return CurrentTodo({}, read.error)
        try:
            todo = read.todo_list.pop(todo_id - 1)
        except IndexError:
            return CurrentTodo({}, ID_ERROR)
        write = self._db_handler.write_todos(read.todo_list)
        return CurrentTodo(todo, write.error)
    
    def remove_all(self) -> CurrentTodo:
        """Remove all to-dos from the database."""
        write = self._db_handler.write_todos([])
        return CurrentTodo({}, write.error)