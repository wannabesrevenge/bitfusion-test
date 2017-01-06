import click
from click.testing import CliRunner
import docker

import dockercli

runner = CliRunner()

def _log_output(output):
  print('\n--------------\nCommand Output: \n%s\n--------------\n' % output)

def test_run():
  print('Test run command')

  result = runner.invoke(dockercli.run, ['test'])
  try:
    assert result.exit_code == 0
    assert 'Server is listening' in result.output
  except Exception as e:
    print('Test run command failed')
    _log_output(result.output)
    return

  print('Test run command success')

def test_logs():
  print('Test logs command')

  result = runner.invoke(dockercli.logs, ['test'])
  try:
    assert result.exit_code == 0
    assert 'Running on http://0.0.0.0' in result.output
  except Exception as e:
    print('Test logs command failed')
    _log_output(result.output)
    return

  print('Test logs command success')

def test_stop():
  print('Test stop command')

  result = runner.invoke(dockercli.stop, ['test'])
  try:
    assert result.exit_code == 0
    assert 'Container destroyed' in result.output
  except Exception as e:
    print('Test stop command failed')
    _log_output(result.output)
    return

  print('Test logs command success')

test_run()
test_logs()
test_stop()
