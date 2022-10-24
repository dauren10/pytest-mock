import sys
import main


def test_patch(mocker):
    mocker.patch('main.get_age', return_value=3)
    assert main.get_age() == 3
    print("\nhello", file=sys.stderr)
    mocker.patch("builtins.print", return_value=3)
    assert print() == 3


def test_get_age():
    assert main.get_age() == 61


def test_patch_simple_side_effect(mocker):
    def patch_get_age():
        print("\nrequest", file=sys.stderr)
        return 3
    mocker.patch('main.get_age', side_effect=patch_get_age)
    assert main.get_age() == 3
