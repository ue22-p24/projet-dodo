from contextlib import asynccontextmanager
from databases import Database
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Static files are handled by a specific sub-router 
static = StaticFiles(directory="static")

# We instanciate a template engine for jinja2
templates = Jinja2Templates(directory="templates")

# The database connection
database = Database('sqlite+aiosqlite:///data.db')

# Connect/disconnect the database when the app starts/stops
@asynccontextmanager
async def lifespan(_app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

# We mount the static files handler under /static
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, filter: str = "all"):
    todos = []
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "todos": todos,
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.bind_host, port=config.port)