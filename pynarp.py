import os
import sys

from rich.console import Console
from rich.markdown import Markdown


def resource_path(relative_path):
    """ Get absolute path to resource for PyInstaller """

    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
        
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def print_intro():
    file = 'README.md'
    path = resource_path(file)
    with open(path) as readme:
        markdown = Markdown(readme.read())

    console = Console()
    console.print(markdown)


if __name__ == '__main__':
    print_intro()
