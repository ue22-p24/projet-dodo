import datetime
from typing import List 
from databases import Database

from db.models import Todo

async def get_todos(db: Database, filter: str) -> List[Todo]:
    """
    Récupère tous les todos
    """
    return [
        Todo(
            id = 1,
            content = "Faire les courses",
            is_done = False,
            created_at = datetime.datetime.now()
        )
    ]

async def update_todo(db: Database, todo_id: int, is_done: bool) -> Todo:
    """
    Met à jour le statut d'un todo
    """

async def create_todo(db: Database, content: str) -> Todo:
    """
    Crée un nouveau todo
    """

async def delete_todo(db: Database, todo_id: int) -> Todo:
    """ 
    Supprime un todo
    """