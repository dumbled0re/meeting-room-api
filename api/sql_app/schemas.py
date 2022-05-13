import datetime
from pydantic import BaseModel, Field

# 会議室予約画面
class BookingCreate(BaseModel):
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime


class Booking(BookingCreate):
    booking_id: int

    # NOTE: 基本的にはディクショナリでデータが入ってくるが、sqlalchemyなどのormのデータ構造が入ってきてもデータを読めるようにする
    class Config:
        orm_mode = True


# ユーザー登録画面
class UserCreate(BaseModel):
    user_name: str = Field(max_length=12)


class User(UserCreate):
    user_id: int

    class Config:
        orm_mode = True


# 会議室登録画面
class RoomCreate(BaseModel):
    room_name: str = Field(max_length=12)
    capacity: int


class Room(RoomCreate):
    room_id: int

    class Config:
        orm_mode = True
