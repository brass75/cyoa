from collections.abc import Generator
from dataclasses import dataclass

from .page import NoSelection, Page, Sentinel


@dataclass(frozen=True, kw_only=True)
class Engine:
    states: dict[str, Page]
    first_state: str

    def run(self):
        """
        Run the Engine
        """
        state: str = self.first_state
        states: dict[str, Generator[str | Sentinel | None, str | None]] = {}
        breadcrumbs: list[str] = [""]
        while True:
            if state not in states:
                states[state] = iter(self.states[state])
                next(states[state])  # pyright: ignore[reportUnusedCallResult]
            try:
                next_state: str | object | None = states[state].send(breadcrumbs[~0])
                match next_state:
                    case Sentinel():
                        state = breadcrumbs.pop()
                        continue
                    case str() | None:
                        if not next_state:
                            raise StopIteration
                        breadcrumbs.append(state)
                        state = next_state
            except StopIteration:
                break
            except KeyboardInterrupt:
                print("\n\nThanks for reading!")
                break
            except NoSelection:
                print("\n\nThanks for reading!")
                break
