from __future__ import annotations

from typing import Any

import pytest


@pytest.fixture
def sample_users() -> list[dict[str, Any]]:
    return [
        {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": " Sincere@april.biz ",
            "address": {"city": "Gwenborough", "zipcode": "92998-3874"},
            "company": {"name": "Romaguera-Crona"},
        },
        {
            "id": 2,
            "name": "Ervin Howell",
            "username": "Antonette",
            "email": "Shanna@melissa.tv",
            "address": {"city": "Wisokyburgh", "zipcode": "90566-7771"},
            "company": {"name": "Deckow-Crist"},
        },
        {
            "id": 3,
            "name": None,
            "username": "incomplete",
            "email": None,
            "address": {},
            "company": {},
        },
    ]
