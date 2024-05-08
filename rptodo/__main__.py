"""RP To-Do entry point script."""
# rptodo/__main__.py

from rptodo import cli, __app_name__

def main() -> None:
    """RP To-Do entry point."""
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()