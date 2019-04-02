import click
from cli import cli
from cli.dev.actions import run

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

    if sc == 'frontend':
        click.secho("Dev frontend", fg="green")

    elif sc == 'services':
        click.secho("Dev services", fg="green")

    elif sc == 'run':
        click.secho("Starting development services.....", fg="green")
        run()


    else: print(help_txt)
