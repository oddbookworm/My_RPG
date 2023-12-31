from __future__ import annotations
from typing import Dict, List
from abc import ABC, abstractmethod

from pygame.event import Event


class GameState(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def handle_events(self, events: Dict[int, List[Event]]) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass


class GameStateManager:
    __instance = None

    def __new__(cls) -> GameStateManager:
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        self.states: Dict[str, GameState] = {}
        self.state: GameState | None = None

    def add_state(self, state: GameState) -> None:
        self.states[state.name] = state

    def set_state(self, name: str) -> None:
        self.state = self.states[name]

    def update(self) -> None:
        if self.state is not None:
            self.state.update()

    def draw(self) -> None:
        if self.state is not None:
            self.state.draw()

    def handle_events(self, events: Dict[int, List[Event]]) -> None:
        if self.state is not None:
            self.state.handle_events(events)
