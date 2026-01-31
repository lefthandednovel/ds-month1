import pandas as pd
from pathlib import Path
from typing import Iterable

def read_csv_checked(path: str | Path, required_cols: Iterable[str]) -> pd.DataFrame:
    path=Path(path)
    
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path.absolute()}")
    
    df = pd.read_csv(path)
    available_cols = df.columns.tolist()
    missing = [col for col in required_cols if col not in available_cols]

    if len(missing)!=0:
        raise ValueError(f"Missing columns: {missing}, available columns: {available_cols}")
    
    return df



