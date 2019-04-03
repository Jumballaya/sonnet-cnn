import click
from cli import cli
from cli.dev.actions import actions

help_txt = """
Usage: project dev [OPTIONS] SUBCOMMAND

Options:
  --help Show this message and exit.

Subcommands:
  frontend   Run frontend by itself
  services   Run the backend services by themselves
  start      Run the full development stack
  build      Build the docker-compose.yml file
"""

@cli.command()
@click.argument('subcommand')
def dev(subcommand):
    """
    Development options
    """
    sc = subcommand.lower()
    if sc in actions: actions[sc]()
    else: print(help_txt)
