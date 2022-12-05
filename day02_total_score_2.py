SELECTION_MAP = {
    "A": "ROCK",
    "X": "LOSE",
    "B": "PAPER",
    "Y": "DRAW",
    "C": "SCISSORS",
    "Z": "WIN",
}


SELECTION_SCORES = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3
}

def get_score(opponent_choice, result):
    your_choice = None
    score = 0
    if result == "DRAW":
        score += 3
        your_choice = opponent_choice
    elif result == "LOSE":
        if opponent_choice == "ROCK":
            your_choice = "SCISSORS"
        elif opponent_choice == "PAPER":
            your_choice = "ROCK"
        elif opponent_choice == "SCISSORS":
            your_choice = "PAPER"
    elif result == "WIN":
        score += 6
        if opponent_choice == "ROCK":
            your_choice = "PAPER"
        elif opponent_choice == "PAPER":
            your_choice = "SCISSORS"
        elif opponent_choice == "SCISSORS":
            your_choice = "ROCK"

    score += SELECTION_SCORES[your_choice]

    return score

def main():

    with open('data/day02_rps_strategy.data') as f:
        total_score = 0
        for row in f:
            opponent_choice = SELECTION_MAP[row[0]]
            result = SELECTION_MAP[row[2]]
            total_score += get_score(opponent_choice, result)

    print(f"answer: {total_score}")

if __name__ == "__main__":
    main()