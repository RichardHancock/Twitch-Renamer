import pytest
import os

from twitch_renamer.twitch_renamer import epoch_to_format_datetime

files_names = [
    ("1606406279 - SomeNameBlah.tst", "2020-11-26 15-57 - SomeNameBlah.tst"),
    ("1577836800 - multi - dash.tst", "2020-01-01 00-00 - multi - dash.tst"),
    ("2208988799 - break-it.tst", "2039-12-31 23-59 - break-it.tst"),
    ("833587200 ---- dash--it.tst", "1996-06-01 00-00 ----dash--it.tst"),
]


@pytest.fixture
def create_test_files(scope="function"):
    # try:
    # os.mkdir("testfiles")
    # except OSError as e:
    # print("Test path creation failed: " + e.strerror)
    # assert False

    print("testfiles directory created")

    for filename, expected in files_names:
        print("TODO")


@pytest.mark.parametrize("input,expected", [
    (1606406279, "2020-11-26 15-57"),
    ("1606406279", "2020-11-26 15-57"),
    (1577836800, "2020-01-01 00-00"),
    (2208988799, "2039-12-31 23-59"),
    (833587200, "1996-06-01 00-00"),
])
def test_epoch_converter(input, expected):
    assert epoch_to_format_datetime(input) == expected
