import click
import subprocess
import shlex

@click.command()
@click.argument("hostname")
@click.option('--username',
			  default=None,
			  type=click.STRING,
			  help='Username for host.')
@click.option('--no_tmux', is_flag=True, help='Do not invoke tmux on connection.')
def cli(hostname, username, no_tmux):
	tmux = '-- tmux new -A -s main'
	if username:
		hostname = username + "@" + hostname
	cmd = [
		'mosh',
		hostname,
	]
	if not no_tmux:
		cmd = cmd + shlex.split(tmux)
		
	click.echo(f"Connecting to {hostname} with {shlex.join(cmd)}…")
	subprocess.run(cmd)
if __name__ == '__main__':
	cli()