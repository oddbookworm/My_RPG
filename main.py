import pygame

from typing import Dict, List
from collections import defaultdict

from src.states.MainMenu import MainMenu
from src.states.GameState import GameStateManager


def main() -> None:
    pygame.init()

    pygame.display.set_mode((500, 500))

    manager = GameStateManager()
    manager.add_state(MainMenu("Main Menu"))
    manager.set_state("Main Menu")

    while True:
        events: Dict[int, List[pygame.Event]] = defaultdict(list)
        for event in pygame.event.get():
            events[event.type].append(event)

        manager.handle_events(events)
        manager.update()
        manager.draw()


if __name__ == "__main__":
    main()
