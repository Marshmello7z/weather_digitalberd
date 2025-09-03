from pathlib import Path
import yaml

def load_yaml(path: str | Path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)
