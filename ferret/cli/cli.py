from pathlib import Path

import click

from ferret.data.loader import DataLoader


@click.group()
def cli():
    pass

@cli.command()
@click.option("--path", required=True)
def download(path: str):
    loader = DataLoader()
    loader.download(Path(path))

@cli.command()
def foo():
    print("foo")
