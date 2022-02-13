from config import *


def test_load(mocker):
    mocked_config_data = mocker.mock_open(
        read_data='{"configVersion": 999999,"debug_mode": false}'
    )
    mocker.patch("config.open", mocked_config_data)
    assert load() == {"configVersion": 999999, "debug_mode": False}

    mocker.patch("config.open", mocked_config_data)
    assert load() != {"configVersion": 999999, "debug_mode": True}
