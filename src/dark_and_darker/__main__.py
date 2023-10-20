"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Dark and Darker."""


if __name__ == "__main__":
    main(prog_name="dark-and-darker")  # pragma: no cover
