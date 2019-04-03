import click
from cli import cli
from cli.deploy.actions import actions

help_txt = """
Usage: project deploy [OPTIONS] SUBCOMMAND

Options:
  --help Show this message and exit.

Subcommands:
  frontend   Build and deploy frontend assets
  models     Deploy built models
  services   Deploy backend services
  database   Deploy database migrations and changes
"""

@cli.command()
@click.argument('subcommand')
def deploy(subcommand):
    """
    Deployment options
    """
    sc = subcommand.lower()

    if sc in actions: actions[sc]()
    else: print(help_txt)
