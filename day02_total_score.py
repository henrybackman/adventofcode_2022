SELECTION_MAP = {
    "A": "ROCK",
    "X": "ROCK",
    "B": "PAPER",
    "Y": "PAPER",
    "C": "SCISSORS",
    "Z": "SCISSORS",
}


SELECTION_SCORES = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3
}

def get_score(opponent_choice, your_choice):
    score = SELECTION_SCORES[your_choice]

    if opponent_choice == your_choice:
        return score + 3

    is_win = False
    if your_choice == "ROCK" and opponent_choice == "SCISSORS":
        is_win = True
    elif your_choice == "PAPER" and opponent_choice == "ROCK":
        is_win = True
    elif your_choice == "SCISSORS" and opponent_choice == "PAPER":
        is_win = True

    if is_win:
        return score + 6

    return score

def main():

    with open('data/day02_rps_strategy.data') as f:
        total_score = 0
        for row in f:
            opponent_choice = SELECTION_MAP[row[0]]
            your_choice = SELECTION_MAP[row[2]]
            total_score += get_score(opponent_choice, your_choice)

    print(f"answer: {total_score}")

if __name__ == "__main__":
    main()