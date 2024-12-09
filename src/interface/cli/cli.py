import click

from src.interface.cli.sub_commands.utils import utils_cli

@click.group(help="Command Line Interface for various tasks.")
def cli(): ...


cli.add_command(utils_cli)


if __name__ == "__main__":
    cli()
