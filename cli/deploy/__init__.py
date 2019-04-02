import click
from cli import cli

help_txt = """
Usage: project deploy [OPTIONS] SUBCOMMAND

Deployment options

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

    if sc == 'frontend':
        click.secho("Deploy frontend", fg="green")

    elif sc == 'models':
        click.secho("Deploy models", fg="green")

    elif sc == 'services':
        click.secho("Deploy services", fg="green")

    elif sc == 'database':
        click.secho("Deploy DB changes", fg="green")

    else: print(help_txt)
