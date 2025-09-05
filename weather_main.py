from utils.yaml_utils import load_yaml
from utils.api_client import get_current_weather
from utils.writers import to_csv_timestamped
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).parent / ".env")  # грузим .env из корня проекта

import os
print("API ok:", bool(os.getenv("OPENWEATHER_API_KEY")))

def main():
    settings = load_yaml("config/settings.yaml")
    cities = load_yaml("config/cities.yaml")

    base_url = settings["api"]["base_url"]
    units = settings["defaults"]["units"]
    lang = settings["defaults"]["lang"]

    rows = []
    for city in cities:
        data = get_current_weather(base_url, q=city, units=units, lang=lang)
        rows.append({
            "city": data["name"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "conditions": data["weather"][0]["description"],
        })

    out = to_csv_timestamped(rows, outdir="data")
    print(f"saved: {out}")

if __name__ == "__main__":
    main()
