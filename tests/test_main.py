import platform

from main import clear
from main import setup_rooms


def test_os_type():
    assert clear() == platform.system()


def test_setup_rooms():
    rooms = setup_rooms()
    assert rooms[0].next_room == rooms[1]
    assert rooms[1].last_room == rooms[0]
