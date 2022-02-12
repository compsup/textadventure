import platform

from main import clear


def test_os_type():
    assert clear() == platform.system()
