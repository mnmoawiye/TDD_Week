from health import *

def test_take_damage():
    player = {"health": 100, "max_health": 100, "alive": True}
    result = take_damage(player, 30)
    assert result["health"] == 70

def test_heal_increases_health():
    player = {"health": 80, "max_health": 100, "alive": True}
    result = heal(player, 20)
    assert result["health"] == 80

def test_is_alive_returns_true_when_healthy():
    player = {"health": 100, "max_health": 100, "alive": True}
    assert is_alive(player) == True