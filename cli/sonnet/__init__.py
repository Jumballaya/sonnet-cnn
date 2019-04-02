import click
from cli.sonnet.actions import build, generate

@click.group()
def sonnet():
  """
  Sonnet data and model actions
  """
  pass

@sonnet.command()
def build():
  """
  Build the sonnet ML model file for future use
  """
  build()


@sonnet.command()
def generate():
  """
  Generate a random Sonnet
  """
  generate()

# @cli.command()
# @click.argument('subcommand')
# def sonnet(subcommand):
    # if subcommand.lower() == 'build':
        # build()
    # elif subcommand.lower() == 'generate':
        # generate()
