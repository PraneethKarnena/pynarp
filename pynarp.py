from rich.console import Console
from rich.markdown import Markdown


def print_intro():
    file = 'README.md'
    with open(file) as readme:
        markdown = Markdown(readme.read())

    console = Console()
    console.print(markdown)


if __name__ == '__main__':
    print_intro()
