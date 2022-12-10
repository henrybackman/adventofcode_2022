def main():

    with open('data/day06_signal.data') as f:
        data = next(f)
        counter = 0
        MARKER_LENGTH = 14
        four_last = [None] * MARKER_LENGTH
        for char in data:
            counter += 1
            index = counter % MARKER_LENGTH
            four_last[index] = char

            if counter < MARKER_LENGTH:
                continue

            unique_values = list(set(four_last))

            if len(unique_values) == MARKER_LENGTH:
                break

        first_message = counter

    print(f"answer: {first_message}")


if __name__ == "__main__":
    main()