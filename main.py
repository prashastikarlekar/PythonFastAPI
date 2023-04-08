from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def root():
    return {"message": "Welcome to my API!!!!"}


@app.get("/posts")
def get_posts():
    return {"data": "These are your posts"}


@app.post("/createposts")
# def create_posts(payLoad: dict = Body(...)):
def create_posts(new_post: Post):
    print(new_post.rating)
    # return {"new_post": f"title {payLoad['title']} content:{payLoad['content']}"}
    return {"data": "new_post"}
# what data is needed from client: title str, content str
