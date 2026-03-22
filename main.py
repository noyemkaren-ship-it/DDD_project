from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from api.routers.router import router
app = FastAPI(title="Giga Bank")
templates = Jinja2Templates(directory="templates")
app.include_router(router)
