"""
FastAPI with Corey Schefer

This module demonstrates:
- Basic FastAPI app setup
- A list of sample posts as in-memory data
- A JSON API endpoint to list all posts: /api/posts
- A hidden HTML endpoint to show posts in the browser: /posts
- How to exclude endpoints from the OpenAPI docs using include_in_schema=False

The home page (/) is also hidden from the API docs for a cleaner documentation view.
"""


from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

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

@app.get("/", include_in_schema=False) #include_in_schema=False to avoid add into docs
def home_page():
    return {"Message" : "Welcome to Homepage"}

@app.get("/api/posts")
def get_posts():
    return posts

@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def show_posts():
    return f"<h1>{posts[0]['title']}</h1>"