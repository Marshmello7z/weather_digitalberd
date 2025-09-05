from pathlib import Path
import pandas as pd
from datetime import datetime

def to_csv_timestamped(rows, outdir="data"):
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    path = outdir / f"{ts}.csv"

    df = pd.DataFrame(rows)
    df.to_csv(path, index=False, encoding="utf-8")
    return path
