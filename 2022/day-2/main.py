# PART 1

score = 0

scenarios = {
    'A X': 4, 'A Y': 8, 'A Z': 3,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 7, 'C Y': 2, 'C Z': 6
}

with open('input.txt') as file:
    rounds = file.read().split('\n')

    for round in rounds:
        score += scenarios[round]

    print(score)


# PART 2

score = 0

scenarios_points = {
    'A A': 4, 'A B': 8, 'A C': 3,
    'B A': 1, 'B B': 5, 'B C': 9,
    'C A': 7, 'C B': 2, 'C C': 6
}

desired_scenarios = {
    'A X': 'A C', 'A Y': 'A A', 'A Z': 'A B',
    'B X': 'B A', 'B Y': 'B B', 'B Z': 'B C',
    'C X': 'C B', 'C Y': 'C C', 'C Z': 'C A'
}

with open('input.txt') as file:
    rounds = file.read().split('\n')

    for round in rounds:
        new_round = desired_scenarios[round]
        score += scenarios_points[new_round]

    print(score)
