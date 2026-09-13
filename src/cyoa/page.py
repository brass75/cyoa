from collections.abc import Generator
from dataclasses import dataclass, field


class NoSelection(Exception):
    pass


class Sentinel:
    pass


GOBACK: Sentinel = Sentinel()


def prompt(
    options: dict[str, str], retries: int = 3, prev: str | None = None
) -> str | Sentinel | None:
    """
    Prompts the user for input and validates that it is a valid option.

    :param options: Dictionary containing the options.
    :param retries: Number of times to attempt to requery. Default: 3
    :param prev: The previously visited page.
    :return: The key for the selected option.
    :raise: NoSelection if no valid seclection is made while retries.
    """
    if not options:
        raise NoSelection
    if len(options) == 1 and (text := options.get("", "")):
        print(text)
        return None

    num_retries: int = max(retries, 0)
    enumerated: dict[str, dict[str, str]] = {
        str(idx): {"return": rc, "text": text}
        for idx, (rc, text) in enumerate(options.items(), start=1)
    }
    if prev:
        enumerated.update({"B": {"return": prev, "text": "Go back"}})
    while num_retries >= 0:
        num_retries -= 1
        print("Your options are:\n")
        for idx, option in enumerated.items():
            print(f"{idx}:  {option['text']}")
        print("\n")
        if (choice := input("What is your choice? ").upper()) not in enumerated:
            print(
                f"I'm sorry but {choice!r} is not a valid selection. {'Please try again' if retries else ''}"
            )
            continue
        if choice == "B":
            return GOBACK
        return enumerated[choice]["return"]
    raise NoSelection


@dataclass(kw_only=True, frozen=True)
class Page:
    title: str
    text: str
    options: dict[str, str] = field(default_factory=dict)

    def __iter__(self) -> Generator[str | Sentinel | None, str | None]:
        """
        Prompt user for the next option.

        :yields: The next page to load based on the options
        """
        prev: str | None = yield None
        while True:
            print(self.title)
            print("\n")
            print(self.text)
            print("\n")
            prev = yield prompt(self.options, prev=prev)
