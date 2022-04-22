import requests
import json


def main():
    url = "http://127.0.0.1:8000/item/"
    body = {"name": "T-shirt", "description": "string", "price": 5980, "tax": 1.1}
    # bodyをjsonの形に変換して送る(ディクショナリを送るとエラーが発生する)
    res = requests.post(url, json.dumps(body))
    print(f"レスポンス番号: {res} レスポンスボディ: {res.json()}")


if __name__ == "__main__":
    main()
