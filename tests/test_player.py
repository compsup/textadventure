from player import Player
from room import Room
from items import Item

torch = Item(name="Torch", description="Sturdy Torch", value=1, lightsource=True)
items = [torch]

room = Room(
    name="testroom",
    introtext="test",
    items=items,
)
newroom = Room(
    name="testnewroom",
    introtext="test",
    items=items,
)

player = Player("testsubject", room)


def test_get_room():
    """
    Asserts that the passed in room for the player is assessable from the player class
    """

    returnedRoom = player.room

    assert player.room == returnedRoom
    assert returnedRoom.name == "testroom"
    assert returnedRoom.introtext == "test"


def test_reduce_health():
    """
    Asserts that reducing the players health not all the way too 0 will result in it returning the current health
    Asserts that if the players health gets reduced to 0 or below that it will return false
    """
    player.health = 100

    response = player.reduce_health(99)

    assert response == 1

    response = player.reduce_health(1)

    assert response == 0
    assert player.is_alive() is False


def test_change_room():
    """
    Asserts that changing the players room correctly works
    """
    player.change_room(newroom)

    assert player.room.name == "testnewroom"


def test_do_action():
    """
    Asserts that valid commands return True and invalid return False
    """
    player.room = room
    newroom.last_room = room
    room.next_room = newroom

    assert player.do_action("forward") is True
    assert player.do_action("backward") is True
    assert player.do_action("RandomInvalidAction") is False


def test_search_room():
    assert player.do_action("search") is True


def test_pickup_item():
    assert player.do_action("take torc") is False
    assert player.do_action("take") is False
    assert player.do_action("take torch") is True
    assert player.room.items == []
