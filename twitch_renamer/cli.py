import argparse
from twitch_renamer.version import __version__


def handle_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path",
        help="Path to directory of files to rename"
    )
    parser.add_argument(
        "-d",
        "--dry",
        help="""Perform the renames as a dry run, meaning the original files
         are left unchanged and the results are outputted to the console.""",
        action="store_true"
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version='Twitch-Renamer V{version}'.format(
            version=__version__
        )
    )
    parser.add_argument(
        "-s",
        "--skip-warn",
        help="Skips all warnings, mostly for the CI builds",
        action="store_true"
    )
    args = parser.parse_args()

    return args.debug, args.path, args.skip_warn
