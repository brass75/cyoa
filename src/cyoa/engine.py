from collections.abc import Generator
from dataclasses import dataclass

from .page import NoSelection


@dataclass(frozen=True, kw_only=True)
class Engine:
    states: dict[str, Generator[str]]
    first_state: str

    def run(self):
        """
        Run the Engine
        """
        state: str = self.first_state
        states: dict[str, Generator[str]] = {}
        while True:
            if state not in states:
                states[state] = iter(self.states[state])
            try:
                state = states[state].send(None)
                if not state:
                    raise StopIteration
            except StopIteration:
                break
            except KeyboardInterrupt, NoSelection:
                print("\n\nThanks for reading!")
                break
