import json
from pathlib import Path
from typing import Protocol

from .models import Player


class PlayerSource(Protocol):
    def get_players(self) -> list[Player]:
        ...


class MockPlayerSource:

    def __init__(self) -> None:
        self._path = Path(__file__).parent / "data" / "mock_players.json"
    
    def get_players(self) -> list[Player]:
        raw = json.loads(self._path.read_text())
        return [Player(**entry) for entry in raw]