"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """A 3rd party CLI for interacting with Dark and Darker."""


if __name__ == "__main__":
    main(prog_name="dark-and-darker")  # pragma: no cover
