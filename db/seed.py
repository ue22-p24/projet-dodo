from pathlib import Path
local_dir = Path(__file__).parent.absolute()
root_dir = Path(__file__).parent.parent.absolute()

# We hack the path to be able to import the config
import sys
sys.path.append(f"{root_dir}/")
from config import Config

# And at last, we can do the work 😅
import asyncio
from databases import Database

config = Config()

async def seed(database_url: str):
    database = Database(database_url)
    await database.connect()

    await database.execute(
r"""
CREATE TABLE IF NOT EXISTS Todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    is_done BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
    for content in ["Faire les courses", "Rendre le TP", "Faire une promenade"]:
        await database.execute(
            "INSERT INTO todos (content) VALUES (:content)",
            {"content": content}
        )

    await database.disconnect()

if __name__ == "__main__":
    asyncio.run(seed(config.database_url))
    asyncio.run(seed(config.test_database_url))