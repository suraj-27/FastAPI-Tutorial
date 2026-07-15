from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


posts:list[dict] = [
    {
        "id": 1,
        "author": "Suraj",
        "title": "My First Post",
        "content": "This is the content of my first blog post.",
        "date_posted": "2026-07-10"
    },
    {
        "id": 2,
        "author": "Ashwini",
        "title": "Learning FastAPI",
        "content": "In this post, I share my experience learning FastAPI for building APIs.",
        "date_posted": "2026-07-12"
    }
]

@app.get("/", include_in_schema=False) 
def home_page(request:Request):
    return templates.TemplateResponse(request, "home.html", {"posts":posts, "title":"By Corey"},)

@app.get("/api/posts")
def get_posts():
    return posts

