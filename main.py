import sys
from cli import run_cli, interactive_mode

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_cli()
    else:
        interactive_mode()
