from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field


# リクエストする時にどんなデータを送るのか定義
class ShopInfo(BaseModel):
    name: str
    location: str


class Item(BaseModel):
    # Fieldを使って制約をつけられる
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None


class Data(BaseModel):
    shop_info: Optional[ShopInfo] = None
    items: List[Item]


app = FastAPI()

# docsでリクエストに対して結果が確認できる
# レスポンスボディを定義(リクエストに対して返ってくる値)
@app.post("/item/")
async def create_item(item: Item):
    return {"message": f"{item.name}は、税込価格{int(item.price*item.tax)}円です"}


@app.post("/")
async def index(data: Data):
    return {"data": data}


"""
# 上から順番に確認される
@app.get("/countries/")
# asyncはなくても動くがasyncで非同期処理を可能にする
# Optionalで必須ではなくなる
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
    return {"country": country_name, "country_no": country_no}


# パスパラメータ
@app.get("/countries/{country_name}")
async def index(country_name: str):
    return {"country": country_name}


# クエリーパラメータ(?マーク以降のURL)
# https://fastapi.tiangolo.com/ja/tutorial/sql-databases/?h=db#alternative-db-session-with-middleware


@app.get("/countries/")
async def country2(country_name: str = "japan", country_no: int = 1):
    return {"country": country_name, "country_no": country_no}


# http://127.0.0.1:8000/countries/?country_name=America&country_no=3

# パスパラメータとクエリパラメータの組み合わせ
@app.get("/countries/{country_name}")
async def country_city(country_name: str = "japan", city_name: str = "tokyo"):
    return {"country": country_name, "city_name": city_name}


# http://127.0.0.1:8000/countries/japan?city_name=tokyo
"""
