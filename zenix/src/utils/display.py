from rich import print as rprint
from rich.markdown import Markdown
from rich.rule import Rule


def display(message):
    for line in message.split("\n"):
        line = line.strip()
        if line == "":
            print("")
        elif line == "---":
            rprint(Rule(style="white"))
        else:
            rprint(Markdown(line))

    if message.startswith(">") and "\n" not in message:
        print("")


def truncate(string, length=2500):
    message = f'Showing the last {length} characters\n\n'

    if string.startswith(message):
        string = string[len(message):]
        needs_truncation = True

    if len(string) > length or needs_truncation:
        string = message + string[-length:]

    return string
