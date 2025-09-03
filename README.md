# 🌦️ Weather Digitalberd

Мини-проект для получения текущей погоды по списку городов с помощью **OpenWeather API**.  
Результаты сохраняются в **CSV** для последующей обработки или анализа.

---

## 📂 Структура проекта

```
weather_digitalberd/
├── config/             # Конфигурационные файлы (.yaml)
│   ├── cities.yaml     # Города для запроса
│   └── settings.yaml   # Базовые настройки (units, lang, url)
├── utils/              # Утилиты
│   ├── api_client.py   # Работа с API (запросы к OpenWeather)
│   ├── writers.py      # Запись данных в CSV
│   └── yaml_utils.py   # Чтение/запись YAML
├── .env                # API ключ (НЕ хранится в Git)
├── requirements.txt    # Зависимости проекта
├── weather_main.py     # Точка входа
└── weather.csv         # Результаты (игнорируется в Git)
```

---

## ⚙️ Установка и запуск

1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/Marshmello7z/weather_digitalberd.git
   cd weather_digitalberd
   ```

2. Создать и активировать виртуальное окружение:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux / Mac
   .venv\Scripts\activate      # Windows
   ```

3. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Добавить API-ключ в файл `.env`:
   ```env
   OPENWEATHER_API_KEY=ваш_ключ
   ```

5. Запустить проект:
   ```bash
   python weather_main.py
   ```

---

## 🗝️ Конфигурация

**config/settings.yaml**
```yaml
api:
  base_url: "https://api.openweathermap.org/data/2.5/weather"
defaults:
  units: "metric"
  lang: "ru"
```

**config/cities.yaml**
```yaml
- Moscow,ru
- London,gb
- New York,us
```

---

## 📊 Результат

После запуска создаётся файл `weather.csv`, где хранится актуальная погода по каждому городу:

```
city,temp,feels_like,humidity,conditions
Moscow,14,13,77,пасмурно
London,18,17,65,ясно
New York,22,21,60,переменная облачность
```

---

## 📌 Заметки

- 🔑 API-ключ хранится в `.env` и не попадает в Git (см. `.gitignore`).  
- 📁 Все локальные данные (`*.csv`, `.env`, `.venv`) игнорируются.  
- ⚠️ Новые города можно добавить в `cities.yaml`.  

---

## 🛠️ Технологии

- Python 3.10+  
- [Requests](https://docs.python-requests.org/) — HTTP-запросы  
- [PyYAML](https://pyyaml.org/) — работа с YAML  
- Pandas — обработка данных  

---

## 📄 Лицензия

MIT License. Используй проект свободно 🚀
