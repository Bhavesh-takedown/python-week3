from __future__ import annotations

from typing import Any

from etl.transform import OUTPUT_COLUMNS, transform_users


def test_transform_flattens_and_cleans_emails(
    sample_users: list[dict[str, Any]],
) -> None:
    frame = transform_users(sample_users)

    assert list(frame.columns) == OUTPUT_COLUMNS
    assert len(frame) == 2
    assert frame.loc[0, "email"] == "sincere@april.biz"
    assert frame.loc[0, "city"] == "Gwenborough"
    assert frame.loc[0, "company"] == "Romaguera-Crona"
    assert frame.loc[1, "user_id"] == 2


def test_transform_empty_input() -> None:
    frame = transform_users([])
    assert frame.empty
    assert list(frame.columns) == OUTPUT_COLUMNS


def test_transform_drops_rows_missing_required_fields() -> None:
    frame = transform_users(
        [{"id": 9, "name": "No Email", "email": None, "address": {}, "company": {}}]
    )
    assert frame.empty
