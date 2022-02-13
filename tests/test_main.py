from main import *
import pytest


def test_setup_rooms():
    rooms = setup_rooms()
    assert rooms[0].next_room == rooms[1]
    assert rooms[1].last_room == rooms[0]


def test_choice(mocker):
    mocker.patch("main.input", return_value="yEs")
    assert choice() == "yes"
    assert choice("test") == "yes"


def test_clear(mocker):
    mocker.patch("main.get_os_type", return_value="Linux")
    assert clear() == "clear"
    mocker.patch("main.get_os_type", return_value="Windows")
    assert clear() == "cls"
    mocker.patch("main.get_os_type", return_value="notaos")
    assert clear() is False


def test_get_os_type():
    assert get_os_type() == platform.system()


def test_prompt(mocker):
    mocker.patch("main.choice", return_value=1)
    assert prompt("test", ["option1", "option2"]) == 1
