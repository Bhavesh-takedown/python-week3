from __future__ import annotations

from typing import Any

import pandas as pd

OUTPUT_COLUMNS = [
    "user_id",
    "name",
    "username",
    "email",
    "city",
    "zipcode",
    "company",
]


def _flatten_user(record: dict[str, Any]) -> dict[str, Any]:
    address = record.get("address") or {}
    company = record.get("company") or {}
    return {
        "user_id": record.get("id"),
        "name": record.get("name"),
        "username": record.get("username"),
        "email": (record.get("email") or "").strip().lower() or None,
        "city": address.get("city"),
        "zipcode": address.get("zipcode"),
        "company": company.get("name"),
    }


def transform_users(records: list[dict[str, Any]]) -> pd.DataFrame:
    """Flatten nested user JSON, clean emails, drop incomplete rows."""
    if not records:
        return pd.DataFrame(columns=OUTPUT_COLUMNS)

    frame = pd.DataFrame([_flatten_user(item) for item in records])
    frame = frame.dropna(subset=["user_id", "name", "email"])
    frame["user_id"] = frame["user_id"].astype(int)
    frame["name"] = frame["name"].astype(str).str.strip()
    return frame.loc[:, OUTPUT_COLUMNS].reset_index(drop=True)
