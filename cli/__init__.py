import click
from cli.sonnet import sonnet
from cli.deploy import deploy

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


cli.add_command(sonnet)
cli.add_command(deploy)
