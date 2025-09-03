import pandas as pd
from pathlib import Path
from typing import List, Dict, Any

def to_csv(rows: List[Dict[str, Any]], path: str | Path = "weather.csv"):
    df = pd.DataFrame(rows)
    df.to_csv(path, index=False, encoding="utf-8")
    return path
