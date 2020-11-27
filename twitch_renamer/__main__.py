import twitch_renamer.cli as cli
import twitch_renamer.twitch_renamer as tr

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    (
        path,
        debug,
        skip_warn
    ) = cli.handle_cli()

    tr.twitch_renamer(
        path,
        debug,
        skip_warn
    )
