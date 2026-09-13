import json
from dataclasses import dataclass
from pathlib import Path
from typing import Annotated

import dykes

from .engine import Engine
from .page import Page


@dataclass(frozen=True)
class Args:
    filename: Annotated[Path, "The path to the file with the story."]


def main():
    args: Args = dykes.parse_args(Args)  # pyright: ignore[reportUnknownMemberType]
    story: dict = json.loads(args.filename.read_text())  # pyright: ignore[reportMissingTypeArgument, reportAny]
    pages: dict[str, Page] = {
        name: Page(**values)  # pyright: ignore[reportUnknownArgumentType]
        for name, values in story["pages"].items()  # pyright: ignore[reportUnknownMemberType, reportUnknownVariableType]
    }
    engine: Engine = Engine(states=pages, first_state=story["first_page"])  # pyright: ignore[reportUnknownArgumentType]
    engine.run()
