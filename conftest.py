import pytest
# Default scope — runs before every test (safe for mutable objects like dicts)

@pytest.fixture
def player():
    return {"health": 100, "max_health": 100, "alive": True}


@pytest.fixture(scope="module")
def game_config():
    return {"max_level": 50, "starting_health": 100}   # read-only config
