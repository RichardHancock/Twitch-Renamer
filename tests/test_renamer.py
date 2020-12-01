import pytest
import os

from twitch_renamer.twitch_renamer import epoch_to_format_datetime, \
    twitch_renamer

file_names = [
    ("1606406279 - SomeNameBlah.tst", "2020-11-26 15-57 - SomeNameBlah.tst"),
    ("1577836800 - multi - dash.tst", "2020-01-01 00-00 - multi - dash.tst"),
    ("1577836800 - multi - dash.tst2", "2020-01-01 00-00 - multi - dash.tst2"),
    ("1577836800 - multi ext.gif.tst", "2020-01-01 00-00 - multi ext.gif.tst"),
    ("2208988799 - break-it.tst", "2039-12-31 23-59 - break-it.tst"),
    ("833587200 - ---dash--it.tst", "1996-06-01 00-00 - ---dash--it.tst"),
]

path = ".testfiles"


@pytest.fixture
def create_test_files(scope="function"):
    try:
        os.mkdir(path)
    except OSError as e:
        print("Test path creation failed: " + e.strerror)
        assert False

    print("'testfiles' Directory Created")
    print("Creating Test Files")
    for filename, expected in file_names:
        try:
            with open(os.path.join(path, filename), mode="a") as f:
                f.write("Test Content")
        except OSError as e:
            print("Test file creation failed: " + e.strerror)
            assert False

    yield

    print("Cleaning Up Test Files")


def compare_test_files():
    # Check test path exists (If this fails it's probably a test setup issue)
    assert os.path.exists(path), "Test Path: {0} doesn't exist".format(path)

    files = os.listdir(path)
    # Fetches only the second element of the filename tuples
    expected_files = [orig_files[1] for orig_files in file_names]

    for filename in files:
        assert filename in expected_files


def test_rename_files_normal(create_test_files):
    twitch_renamer(False, path, True)

    compare_test_files()


@pytest.mark.parametrize("input,expected", [
    (1606406279, "2020-11-26 15-57"),
    ("1606406279", "2020-11-26 15-57"),
    (1577836800, "2020-01-01 00-00"),
    (2208988799, "2039-12-31 23-59"),
    (833587200, "1996-06-01 00-00"),
])
def test_epoch_converter(input, expected):
    assert epoch_to_format_datetime(input) == expected
