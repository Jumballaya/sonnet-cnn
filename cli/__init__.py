import click

APP_VERSION = '0.0.1'
CLI_VERSION = '0.0.1'

@click.group()
def cli():
  """
  CLI for generating models, running the server, migrating DBs, deploying to production, and any other tasks
  """
  pass

@cli.command()
def version():
  """
  Print CLI and Project version
  """
  print("Application Version: {}".format(APP_VERSION))
  print("CLI Version: {}".format(CLI_VERSION))

from cli.sonnet import sonnet
from cli.deploy import deploy
from cli.dev import dev
