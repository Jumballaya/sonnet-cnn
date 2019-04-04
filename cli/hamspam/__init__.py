import click
from cli import cli
from cli.hamspam.actions import actions

help_txt = """
Usage: project hamspam [OPTIONS] SUBCOMMAND

Options:
  --help  Show this message and exit.
  --text  Provide a sample text to be tested

Subcommands:
  build      Build the imagenet model
  test       Test an image against the model
"""

@cli.command()
@click.argument('subcommand')
@click.option('-t', '--text', 'text')
def hamspam(subcommand, text):
    """
    Build/Generate the Ham/Spam Model
    """
    sc = subcommand.lower()
    if sc in actions: actions[sc](text)
    else: print(help_txt)
