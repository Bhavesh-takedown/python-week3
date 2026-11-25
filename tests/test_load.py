from __future__ import annotations

from pathlib import Path

import pandas as pd

from etl.load import save_csv
from etl.transform import OUTPUT_COLUMNS


def test_save_csv_writes_file_and_creates_dirs(tmp_path: Path) -> None:
    dest = tmp_path / "nested" / "out.csv"
    frame = pd.DataFrame(
        [
            {
                "user_id": 1,
                "name": "Ada",
                "username": "ada",
                "email": "ada@example.com",
                "city": "London",
                "zipcode": "SW1",
                "company": "Analytical",
            }
        ],
        columns=OUTPUT_COLUMNS,
    )

    written = save_csv(frame, dest)

    assert written == dest
    loaded = pd.read_csv(dest)
    assert list(loaded.columns) == OUTPUT_COLUMNS
    assert loaded.loc[0, "name"] == "Ada"
