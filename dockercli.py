import sys
import time

import click
import docker

DOCKER_TAG = 'wannabesrevenge/bf-python-server:0.0.1'
DOCKER_PATH = '.'
DOCKER_PORT = 8888

dc = docker.from_env()

def open_url(ctx, param, value):
    if value is not None:
        ctx.params['fp'] = urllib.urlopen(value)
        return value


@click.group()
def cli():
  pass


@cli.command()
def build():
  """Locally builds server image from Dockerfile"""
  click.echo('Building docker image...')
  dc.images.build(path=DOCKER_PATH, tag=DOCKER_TAG, rm=True, stream=True)
  click.echo('Finished building docker image!')


@cli.command()
@click.argument('container_name')
def run(container_name):
  """Runs the bf-python-server docker image"""

  click.echo('Starting docker container...')

  try:
    dc.containers.get(container_name)
    click.echo('Docker container already exists. Run "dockercli stop" and try again.')
    sys.exit(1)
  except:
    pass

  dc.containers.run(DOCKER_TAG, name=container_name, ports={'8888/tcp': DOCKER_PORT}, detach=True)
  click.echo('Container started! Checking health...')

  time.sleep(5)
  container = dc.containers.get(container_name)
  health = container.attrs['State']['Health']['Status']

  while health == 'starting':
    time.sleep(1)
    container = dc.containers.get(container_name)
    health = container.attrs['State']['Health']['Status']

  if health != 'healthy':
    click.echo('Container is not healthy. Health status is %s. Check logs and try restarting.' % health)
    sys.exit(1)

  click.echo('Container is healthy!')
  click.echo('Server is listening on http://localhost:%s' % DOCKER_PORT)


@cli.command()
@click.argument('container_name')
def stop(container_name):
  """Stops and removes the named docker container"""
  click.echo('Stopping and removing docker container...')

  container = dc.containers.get(container_name)
  container.remove(force=True)

  click.echo('Container destroyed!')


@cli.command()
@click.argument('container_name')
def logs(container_name):
  """Prints logs for the name docker container"""
  container = dc.containers.get(container_name)
  click.echo(container.logs())
