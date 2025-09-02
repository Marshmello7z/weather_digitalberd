import requests
import yaml
import pandas as pd
from pathlib import Path

API_KEY = "853fd1860e37d240bf5fbe5fc0738735"

# загружаем конфиги
with open("config/settings.yaml", encoding="utf-8") as f:
    settings = yaml.safe_load(f)

with open("config/cities.yaml", encoding="utf-8") as f:
    cities = yaml.safe_load(f)

base_url = settings["api"]["base_url"]
units = settings["defaults"]["units"]
lang = settings["defaults"]["lang"]

rows = []

for city in cities:
    params = {"q": city, "appid": API_KEY, "units": units, "lang": lang}
    r = requests.get(base_url, params=params)
    data = r.json()

    if r.status_code == 200 and data.get("main"):
        rows.append({
            "city": data["name"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "conditions": data["weather"][0]["description"]
        })
    else:
        print("Ошибка для", city, data)

# сохраняем в CSV
df = pd.DataFrame(rows)
df.to_csv("weather.csv", index=False, encoding="utf-8")
print("Файл сохранён: weather.csv")
