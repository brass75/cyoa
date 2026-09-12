# CYOA

CYOA is a Choose Your Own Adventure story engine, written in Python. 

## License

CYOA is distributed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 license.
See [LICENSE.md] for more details.

## Installation

1. Clone the repo:

```sh
$ git clone git@github.com:brass75/cyoa.git
```

or with the GitHub command line app:

```sh
$ gh repo clone brass75/cyoa
```

2. Install:

`uv`:

```sh
$ uv pip install .
```

pip:

```sh
$ pip install .
```

## Usage

Once you have installed you can play a story by running:

```sh
$ cyoa <story.json>
```

The repo includes an example story `[story.json]`

### The story file

A story file is a JSON file that defines a group of pages and which is the first page of the book. 
An example might look like:

```json
{
  "first_page": "page 1",
  "pages": {
    "page 1": {
      "title": "Page 1",
      "text": "This is the text",
      "options": {
        "page 2": "Go to page 2",
        "": "Exit the story"
      }
    },
    "page 2": {
      "title": "Page 2",
      "text": "Some more text",
      "options": {
      "": "Thanks for reading!"
    }
    }
  }
}
```

## Roadmap

At the moment, all I have done is write the engine. I plan on adding:

- A TUI viewer
- A method to export the story to HTML so it can be served as a webpage
- A CLI for editing a story
- A TUI for editing a story

## Contributing

At the moment this is something I plan on doing by myself so contributions are not welcome. If that changes, I will
update this with some actual instructions on how you can contribute.

[story.json]: story.json 
[LICENSE.md]: LICENSE.md
