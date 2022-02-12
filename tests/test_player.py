from player import Player
from room import Room


def test_get_room():
    """
    Asserts that the passed in room for the player is assessable from the player class
    """
    room = Room(
        actions=["backward", "forward"],
        name="testroom",
        introtext="test",
        is_victory=True,
    )
    player = Player("testsubject", room)

    returnedRoom = player.room

    assert player.room == returnedRoom
    assert returnedRoom.name == "testroom"
    assert returnedRoom.introtext == "test"
    assert returnedRoom.is_victory is True
    assert returnedRoom.actions == ["backward", "forward"]


def test_reduce_health():
    """
    Asserts that reducing the players health not all the way too 0 will result in it returning the current health
    Asserts that if the players health gets reduced to 0 or below that it will return false
    """
    room = Room(
        actions=["backward", "forward"],
        name="testroom",
        introtext="test",
        is_victory=True,
    )
    player = Player("testsubject", room)
    player.health = 100

    response = player.reduce_health(99)

    assert response == 1

    response = player.reduce_health(1)

    assert response is False
    assert player.is_alive() is False


def test_change_room():
    """
    Asserts that changing the players room correctly works
    """
    room = Room(
        actions=["backward", "forward"],
        name="testroom",
        introtext="test",
        is_victory=True,
    )
    newroom = Room(
        actions=["backward", "forward"],
        name="testnewroom",
        introtext="test",
        is_victory=False,
    )

    player = Player("testsubject", room)
    player.change_room(newroom)

    assert player.room.name == "testnewroom"
    assert player.room.is_victory is False


def test_do_action():
    """
    Asserts that valid commands return True and invalid return False
    """
    newroom = Room(
        actions=["backward", "forward"],
        name="testnewroom",
        introtext="test",
        is_victory=False,
    )
    room = Room(
        actions=["backward", "forward"],
        name="testroom",
        introtext="test",
        is_victory=False,
    )

    newroom.last_room = room
    room.next_room = newroom
    player = Player("testsubject", room)

    assert player.do_action("forward") is True
    assert player.do_action("backward") is True
    assert player.do_action("RandomInvalidAction") is False
