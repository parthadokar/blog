from typing import Annotated
from datetime import datetime
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy.sql import func

app = FastAPI()


class PostBase(SQLModel):
    title: str = Field(index=True)
    description: str | None = Field(default=None, index=True)


class Post(PostBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@app.on_event("startup")
def on_startup() -> None:
    create_db_and_tables()


@app.post("/post/", response_model=PostRead)
def create_post(post: PostCreate, session: SessionDep) -> Post:
    db_post = Post.model_validate(post)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post
