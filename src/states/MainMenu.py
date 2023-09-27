from typing import Dict, List, Tuple
from pygame.event import Event

import pygame

from .GameState import GameState


class MainMenu(GameState):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.color: str | Tuple[int, int, int] = "blue"

        self.need_to_change_color = False

    def handle_events(self, events: Dict[int, List[Event]]) -> None:
        if events[pygame.QUIT]:
            raise SystemExit

        for event in events[pygame.KEYDOWN]:
            if event.key == pygame.K_SPACE:
                self.need_to_change_color = True

    def update(self) -> None:
        if self.need_to_change_color:
            self._change_color()
        self.need_to_change_color = False

    def draw(self) -> None:
        screen = pygame.display.get_surface()

        screen.fill(self.color)
        pygame.display.flip()

    def _change_color(self) -> None:
        from random import randint

        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
