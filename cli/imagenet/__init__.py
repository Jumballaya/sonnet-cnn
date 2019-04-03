import click
from cli import cli
from cli.imagenet.actions import actions

help_txt = """
Usage: project imagenet [OPTIONS] SUBCOMMAND

Options:
  --help  Show this message and exit.
  --image Provide an image to be tested

Subcommands:
  build      Build the imagenet model
  test       Test an image against the model
"""

@cli.command()
@click.argument('subcommand')
@click.option('-i', '--image', 'image')
def imagenet(subcommand, image):
    """
    Build/Generate the Imagenet Model
    """
    sc = subcommand.lower()
    if sc in actions: actions[sc](image)
    else: print(help_txt)
