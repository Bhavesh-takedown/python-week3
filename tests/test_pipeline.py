from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import MagicMock

import pandas as pd

from etl.pipeline import run_pipeline


def test_run_pipeline_extract_transform_load(
    tmp_path: Path, sample_users: list[dict[str, Any]]
) -> None:
    response = MagicMock()
    response.json.return_value = sample_users
    response.raise_for_status.return_value = None
    session = MagicMock()
    session.get.return_value = response

    dest = tmp_path / "users.csv"
    path = run_pipeline(session=session, output_path=dest)

    assert path == dest
    loaded = pd.read_csv(dest)
    assert len(loaded) == 2
    assert "sincere@april.biz" in set(loaded["email"])
    session.get.assert_called_once()
