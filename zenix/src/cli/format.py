from rich.box import MINIMAL
from rich.console import Console, Group
from rich.live import Live
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table


class Format:

    def __init__(self):
        self.language = "python"
        self.display = ""
        self.code = ""

        self.live = Live(auto_refresh=False, console=Console())
        self.live.start()
