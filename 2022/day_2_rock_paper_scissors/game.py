def play_game(file_path):
    strategy = _get_strategy(file_path)
    score = _follow_strategy(strategy)
    return score


def play_game_with_new_rules(file_path):
    strategy = _get_strategy(file_path)
    score = _follow_strategy_with_new_rules(strategy)
    return score


def _get_strategy(file_path):
    strategy = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            strategy.append(tuple(line.split(' ')))

    return strategy


def _follow_strategy(strategy):
    absolute_points = {'X': 1,
                       'Y': 2,
                       'Z': 3}

    relative_points = {'X': {'C': 6,
                             'A': 3,
                             'B': 0},
                       'Y': {'A': 6,
                             'B': 3,
                             'C': 0},
                       'Z': {'B': 6,
                             'C': 3,
                             'A': 0}}
    score = 0

    for turn in strategy:
        opponent_choice, player_choice = turn
        score += absolute_points[player_choice]
        score += relative_points[player_choice][opponent_choice]

    return score


def _follow_strategy_with_new_rules(strategy):
    absolute_points = {'X': 0,
                       'Y': 3,
                       'Z': 6}

    relative_points = {'A': {'X': 3,
                             'Y': 1,
                             'Z': 2},
                       'B': {'X': 1,
                             'Y': 2,
                             'Z': 3},
                       'C': {'X': 2,
                             'Y': 3,
                             'Z': 1}}

    score = 0

    for turn in strategy:
        opponent_choice, required_outcome = turn
        score += absolute_points[required_outcome]
        score += relative_points[opponent_choice][required_outcome]

    return score
