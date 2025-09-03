import os
import requests
from typing import Any, Dict

def get_current_weather(base_url: str, q: str, units: str, lang: str) -> Dict[str, Any]:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key or "ВСТАВ" in api_key:
        raise RuntimeError("OPENWEATHER_API_KEY не найден или плейсхолдер. Добавь реальный ключ в .env")

    params = {
        "q": q,
        "appid": api_key,
        "units": units,
        "lang": lang,
    }
    r = requests.get(base_url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    if str(data.get("cod")) != "200":
        raise RuntimeError(f"API error: {data.get('cod')} - {data.get('message')}")
    return data
