from collections.abc import Generator
from dataclasses import dataclass, field


class NoSelection(Exception):
    pass


def prompt(options: dict[str, str], retries: int = 3) -> str:
    """
    Prompts the user for input and validates that it is a valid option.

    :param options: Dictionary containing the options.
    :param retries: Number of times to attempt to requery. Default: 3
    :return: The key for the selected option.
    :raise: NoSelection if no valid seclection is made while retries.
    """
    if not options:
        raise NoSelection
    if not all(options):
        text: str = options.get("", "")
        print(text)
        return ""

    num_retries: int = max(retries, 0)
    enumerated: dict[str, dict[str, str]] = {
        str(idx): {"return": rc, "text": text}
        for idx, (rc, text) in enumerate(options.items(), start=1)
    }
    while num_retries >= 0:
        num_retries -= 1
        print("Your options are:\n")
        for idx, option in enumerated.items():
            print(f"{idx}:  {option['text']}")
        print("\n")
        if (choice := input("What is your choice? ")) not in enumerated:
            print(
                f"I'm sorry but {choice!r} is not a valid selection. {'Please try again' if retries else ''}"
            )
            continue
        return enumerated[choice]["return"]
    raise NoSelection


@dataclass(kw_only=True, frozen=True)
class Page:
    title: str
    text: str
    options: dict[str, str] = field(default_factory=dict)

    def __iter__(self) -> Generator[str]:
        """
        Prompt user for the next option.

        :yields: The next page to load based on the options
        """
        while True:
            print(self.title)
            print("\n")
            print(self.text)
            print("\n")
            yield prompt(self.options)
