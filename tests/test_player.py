from player import Player
from room import Room
from items import Item

torch = Item(name="Torch", description="Sturdy Torch", value=1, lightsource=True)


def room1():
    items = [torch]
    return Room(
        name="testroom",
        introtext="test",
        items=items,
    )


def room2():
    return Room(name="testnewroom", introtext="test", is_victory=True)


def player():
    return Player("testsubject", room1())


def test_get_room():
    """
    Asserts that the passed in room for the player is assessable from the player class
    """
    room = room1()
    newroom = room2()
    player1 = player()

    returnedRoom = player1.room

    assert player1.room == returnedRoom
    assert returnedRoom.name == "testroom"
    assert returnedRoom.introtext == "test"


def test_reduce_health():
    """
    Asserts that reducing the players health not all the way too 0 will result in it returning the current health
    Asserts that if the players health gets reduced to 0 or below that it will return false
    """
    player1 = player()
    player1.health = 100

    response = player1.reduce_health(99)

    assert response == 1

    response = player1.reduce_health(1)

    assert response == 0
    assert player1.is_alive() is False


def test_change_room():
    """
    Asserts that changing the players room correctly works
    """
    player1 = player()
    newroom = room2()
    player1.change_room(newroom)

    assert player1.room.name == "testnewroom"
    assert player1.victory is True


def test_do_action_move():
    """
    Asserts that valid commands return True and invalid return False
    """
    room = room1()
    newroom = room2()
    player1 = player()

    player1.room = room
    newroom.last_room = room
    room.next_room = newroom
    player1.health = 100

    assert player1.do_action("RandomInvalidAction") is False

    assert player1.do_action("backward") is False
    assert player1.do_action("forward") is True
    assert player1.do_action("forward") is False
    assert player1.do_action("backward") is True

    assert player1.health == 98


def test_do_action_search_room():
    player1 = player()

    assert player1.do_action("search") is True
    player1.room.items = []
    assert player1.search() is False


def test_do_action_take_item():
    player1 = player()
    assert player1.do_action("take torc") is False
    assert player1.do_action("take") is False
    player1.room.searched = True
    assert player1.do_action("take torch") is True
    assert player1.room.items == []
    assert player1.take_item("torch") is False


def test_do_action_drop_item():
    room = room1()
    newroom = room2()
    player1 = player()
    player1.room.items = []
    player1.inv = [torch]

    assert player1.do_action("drop") is False
    assert player1.do_action("drop abc") is False
    assert player1.do_action("drop torch") is True
    assert player1.inv == []
    assert player1.room.items == [torch]

    assert player1.do_action("take torch") is False
    player1.room.searched = True
    assert player1.do_action("take torch") is True
    assert player1.inv == [torch]
    player1.change_room(newroom)
    assert player1.do_action("drop torch") is True
    assert player1.room.items == [torch]
    assert player1.inv == []

    player1.change_room(room)
    player1.change_room(newroom)
    assert player1.room.items == [torch]
