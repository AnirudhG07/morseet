import argparse
import os
import subprocess

from entry import entry


def main():
    ## Handle input flags
    parser = argparse.ArgumentParser(
        description="Morseet Morseet Morseeeeeeet!!!",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    # Add the flags
    parser.add_argument(
        "-v", "--version",
        action="version",
        version="Morseet - version 1.0.0",
        help="Show the version of the program and exit.",
    )
    parser.add_argument(
        "-c", "--config", action="store_true", help="Open the Configuration file in $EDITOR"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Check if the config flag was used
    if args.config:
        # Get the default editor from the environment variable
        editor = os.getenv("EDITOR", "nano")  # Default to nano if EDITOR is not set
        # Open the config.toml file in the editor
        subprocess.run([editor, "config.toml"])
    else:
        # Call the entry function if the -c flag is not used
        exit_code = entry()

if __name__ == "__main__":
    main()
