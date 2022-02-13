from items import Item

item = Item("testitem", "test", 10)


def test_item_return_values():
    assert item.name == "testitem"
    assert item.description == "test"
    assert item.value == 10
