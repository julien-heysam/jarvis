import logging

import click
from rich import print as rprint

from src.utils.tree_utils import DirectoryTreeBuilder

utils_cli = click.Group("utils", help="Commands related to utils")
logger = logging.getLogger(__name__)


@utils_cli.command()
@click.option("--src_dir", "-s", type=str)
def tree_dir(src_dir: str):
    tree_builder = DirectoryTreeBuilder(src_dir)
    tree = tree_builder.build()
    rprint(tree)
