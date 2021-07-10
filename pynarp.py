import click
from rich.console import Console
from rich.markdown import Markdown

from src.run import start


def print_intro():
    file = 'README.md'
    with open(file) as readme:
        markdown = Markdown(readme.read())

    console = Console()
    console.print(markdown)
    console.print('Type [bold cyan]./pynarp --help[/bold cyan] for mode details.')
    console.print('\n')


if __name__ == '__main__':
    # Print project info
    print_intro()

    # Start the installer
    start()
