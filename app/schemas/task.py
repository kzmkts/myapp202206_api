from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="今日の予定を入力")


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    created_at: datetime
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True
