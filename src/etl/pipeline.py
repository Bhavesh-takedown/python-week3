from __future__ import annotations

from pathlib import Path

import requests

from etl.extract import DEFAULT_URL, fetch_users
from etl.load import save_csv
from etl.transform import transform_users

DEFAULT_OUTPUT = Path("data") / "users.csv"


def run_pipeline(
    *,
    url: str = DEFAULT_URL,
    output_path: str | Path = DEFAULT_OUTPUT,
    session: requests.Session | None = None,
) -> Path:
    """Extract users from the API, transform with pandas, load to CSV."""
    records = fetch_users(url, session=session)
    frame = transform_users(records)
    return save_csv(frame, output_path)
