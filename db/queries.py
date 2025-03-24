from typing import List 
from databases import Database

from db.models import Todo

async def get_todos(db: Database, filter: str) -> List[Todo]:
    """
    Récupère tous les todos
    """
    query = "SELECT * FROM todos "
    if filter == "active":
        query += " WHERE is_done = FALSE"
    elif filter == "completed":
        query += " WHERE is_done = TRUE"
    query += " ORDER BY created_at DESC"
    rows = await db.fetch_all(query)
    return (Todo(**row) for row in rows)

async def update_todo(db: Database, todo_id: int, is_done: bool) -> Todo:
    """
    Met à jour le statut d'un todo
    """
    query = """
    UPDATE todos SET is_done = :is_done WHERE id = :todo_id
    RETURNING *
    """
    await db.execute(query, {"is_done": is_done, "todo_id": todo_id})

async def create_todo(db: Database, content: str) -> Todo:
    """
    Crée un nouveau todo
    """
    query = "INSERT INTO todos (content) VALUES (:content)"
    return await db.execute(query, {"content": content})

async def delete_todo(db: Database, todo_id: int) -> Todo:
    """ 
    Supprime un todo
    """
    query = "DELETE FROM todos WHERE id = :todo_id"
    return await db.execute(query, {"todo_id": todo_id})