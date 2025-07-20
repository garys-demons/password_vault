import os
from pyfiglet import Figlet
from rich import print

from rich.console import Console

class Utils:
    def heading(self):
        f = Figlet(font="slant")
        console = Console()
        console.print(f.renderText("password vault"), style="bold cyan")
        print("\n")

    def choices(self):
        print(f"[bold cyan]====================================[/bold cyan]")
        print(f"[bold cyan] What would you like to do ?[/bold cyan]")
        print("1. Add a new password")
        print("2. View an existing password")
        print("3. View all saved sites")
        print("4. Exit")

    def printTitle(self, text: str):
        print(f"[bold cyan]{text}[/bold cyan]")

    def printText(self, text: str):
        print(f"{text}")

    def logError(self, text: str):
        print(f"[bold red]{text}[/bold red]")

    def clear_terminal(self):
        os.system("clear")
