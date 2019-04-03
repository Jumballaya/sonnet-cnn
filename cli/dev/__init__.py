import click
from cli import cli
from cli.dev.actions import actions

help_txt = """
Usage: project dev [OPTIONS] SUBCOMMAND

Deployment options

Options:
  --help Show this message and exit.

Subcommands:
  frontend   Run frontend by itself
  services   Run the backend services by themselves
  run        Run the full development stack
"""

@cli.command()
@click.argument('subcommand')
def dev(subcommand):
    """
    Deployment options
    """
    sc = subcommand.lower()
    if sc in actions: actions[sc]()
    else: print(help_txt)
