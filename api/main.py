import datetime
from fastapi import FastAPI
from pydantic import BaseModel, Field


# 会議室予約画面
class Booking(BaseModel):
    booking: int
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime


# ユーザー登録画面
class User(BaseModel):
    user_id: int
    user_name: str = Field(max_length=12)


# 会議室登録画面
class Room(BaseModel):
    room_id: int
    room_name: str = Field(max_length=12)
    capacity: int
