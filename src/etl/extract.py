from __future__ import annotations

from typing import Any

import requests

DEFAULT_URL = "https://jsonplaceholder.typicode.com/users"
DEFAULT_TIMEOUT = 10


class ExtractError(RuntimeError):
    """Raised when the source API cannot be fetched."""


def fetch_users(
    url: str = DEFAULT_URL,
    *,
    timeout: int = DEFAULT_TIMEOUT,
    session: requests.Session | None = None,
) -> list[dict[str, Any]]:
    """GET JSON records from a REST API.

    `session` is injectable so tests can mock HTTP without hitting the network.
    """
    client = session or requests
    try:
        response = client.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise ExtractError(f"Failed to fetch {url}: {exc}") from exc

    payload = response.json()
    if not isinstance(payload, list):
        raise ExtractError("Expected a JSON array of user records")
    return payload
