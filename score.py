# score.py

def add_points(game, amount):
    if amount <= 0 or not isinstance(amount, int):
        raise ValueError("Amount must be a positive integer")
    if not game["active"]:
        return game
    game["score"] += amount * game["multiplier"]
    return game


def apply_multiplier(game, multiplier):
    pass  


def reset_score(game):
    pass  


def is_high_score(game, threshold):
    pass  