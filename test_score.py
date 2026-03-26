import pytest
from score import add_points, apply_multiplier, reset_score, is_high_score


# add_points


def test_add_points_basic(game):
    result = add_points(game, 10)
    assert result["score"] == 10


def test_add_points_negative_raises_error(game):
    with pytest.raises(ValueError):
        add_points(game, -5)


# apply_multiplier


def test_apply_multiplier_basic(game):
    result = apply_multiplier(game, 3)
    assert result["multiplier"] == 3


def test_apply_multiplier_invalid_raises_error(game):
    with pytest.raises(ValueError):
        apply_multiplier(game, 0)


# reset_score


def test_reset_score_basic(game):
    add_points(game, 20)
    apply_multiplier(game, 4)
    result = reset_score(game)
    assert result["score"] == 0
    assert result["multiplier"] == 1


def test_reset_score_when_inactive(game):
    game["active"] = False
    add_points(game, 20)
    result = reset_score(game)
    assert result["score"] == 0
    assert result["multiplier"] == 1


# is_high_score


def test_is_high_score_true(game):
    add_points(game, 50)
    assert is_high_score(game, 10)


def test_is_high_score_invalid_threshold(game):
    with pytest.raises(ValueError):
        is_high_score(game, -1)
