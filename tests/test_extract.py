from __future__ import annotations

from unittest.mock import MagicMock

import pytest
import requests

from etl.extract import ExtractError, fetch_users


def test_fetch_users_returns_json_list() -> None:
    response = MagicMock()
    response.json.return_value = [{"id": 1}]
    response.raise_for_status.return_value = None

    session = MagicMock()
    session.get.return_value = response

    records = fetch_users("https://example.test/users", session=session)

    assert records == [{"id": 1}]
    session.get.assert_called_once_with("https://example.test/users", timeout=10)


def test_fetch_users_raises_on_http_error() -> None:
    response = MagicMock()
    response.raise_for_status.side_effect = requests.HTTPError("500")

    session = MagicMock()
    session.get.return_value = response

    with pytest.raises(ExtractError, match="Failed to fetch"):
        fetch_users(session=session)


def test_fetch_users_rejects_non_list_payload() -> None:
    response = MagicMock()
    response.json.return_value = {"users": []}
    response.raise_for_status.return_value = None

    session = MagicMock()
    session.get.return_value = response

    with pytest.raises(ExtractError, match="JSON array"):
        fetch_users(session=session)
