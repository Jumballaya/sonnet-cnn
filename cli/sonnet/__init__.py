import click
from cli import cli
from cli.sonnet.actions import actions

help_txt = """
Usage: project sonnet [OPTIONS] SUBCOMMAND

Deployment options

Options:
  --help Show this message and exit.

Subcommands:
  build      Build the sonnet model
  generate   Generate a sample sonnet
"""

@cli.command()
@click.argument('subcommand')
def sonnet(subcommand):
    """
    Build/Generate the Sonnet Model
    """
    sc = subcommand.lower()
    if sc in actions: actions[sc]()
    else: print(help_txt)
