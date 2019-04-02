import click

@click.group()
def deploy():
  """
  Deployment actions
  """
  pass

@deploy.command()
def models():
  """
  Deploy models out to S3
  """
  pass
