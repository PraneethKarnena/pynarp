import sys

import click
from rich.console import Console
from rich.markdown import Markdown

from src.run import start
from src.modules.permissions import has_root_permission


def print_intro():
    file = 'README.md'
    with open(file) as readme:
        markdown = Markdown(readme.read())

    console = Console()
    console.print(markdown)
    console.print('Run [bold cyan]sudo ./pynarp --help[/bold cyan] for mode details.')
    console.print('\n')


if __name__ == '__main__':
    # Check sudo access
    if not has_root_permission():
        sys.exit("Pynarp can only be run with root permissions!")

    # Print project info
    print_intro()

    # Start the installer
    start()
