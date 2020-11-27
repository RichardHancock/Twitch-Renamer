import time
import os
import sys


def twitch_renamer(debug, path, skip_warn=False):
    if debug:
        print(path)
        print(epoch_to_format_datetime(1598014504))

    # Implement warning check here show an example file + file count
    files = os.listdir(path)
    total_files = len(files)

    if skip_warn or not query_yes_no("""Chosen path contains {0} files.\n
    One is named {1}.\n
    This script does not check if these files are valid to be renamed!\n
    Continue?""".format(
        total_files,
        files[0]),
        default=None
    ):
        print("Aborting!")
        exit(0)

    success_count = total_files

    # Start the actual renaming (or simulate if -d is passed)
    for count, filename in enumerate(files):

        if (debug):
            print(count)
            print("Origin - " + os.path.join(path, filename))
            print("Output - " + os.path.join(path, convert_filename(filename)))
            print(" ")
        else:
            try:
                raise os.rename(os.path.join(path, convert_filename(filename)))
            except OSError as e:
                print(
                    """ERROR: An error occurred while renaming {0}: {1}\n
                    """.format(
                        filename,
                        e.strerror
                    )
                )

                success_count = count
                break

    if success_count != total_files:
        print("Aborting after {0}/{1} files successfully renamed.".format(
            success_count,
            total_files
        ))
    else:
        print(total_files + " files successfully renamed.")


def convert_filename(filename):
    parts = filename.split(" - ", 1)
    date = epoch_to_format_datetime(parts[0])

    return date + " - " + parts[1]


def epoch_to_format_datetime(epoch):
    return time.strftime("%Y-%m-%d %H-%M", time.gmtime(int(epoch)))


def query_yes_no(question, default="yes"):
    """
    Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    From: https://stackoverflow.com/questions/3041986/
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
