from __future__ import annotations

from pathlib import Path

import pandas as pd


def save_csv(frame: pd.DataFrame, path: str | Path) -> Path:
    """Write the transformed table to CSV, creating parent folders as needed."""
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output, index=False)
    return output
