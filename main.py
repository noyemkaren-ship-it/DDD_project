from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates
from api.routers.router import router
app = FastAPI(title="Giga Bank")
templates = Jinja2Templates(directory="templates")
app.include_router(router)

@app.get("/profile/{username}")
async def profile(username: str, request: Request):
    user = request.cookies.get("username")
    if user:
        return templates.TemplateResponse("profile.html", {"request": request, "username": username})
    else:
        return templates.TemplateResponse("error.html", {"request": request, "username": username})

@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register")
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/profile/{username}/transfers")
async def transfers(request: Request, username: str):
    user = request.cookies.get("username")
    if user:
        return templates.TemplateResponse("transfers.html", {"request": request, "username": username})
    else:
        return templates.TemplateResponse("error.html", {"request": request, "username": username})

