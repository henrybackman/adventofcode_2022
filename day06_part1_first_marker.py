def main():

    with open('data/day06_signal.data') as f:
        data = next(f)
        counter = 0
        four_last = [None, None, None, None]
        for char in data:
            counter += 1
            index = counter % 4
            four_last[index] = char

            if counter < 4:
                continue

            unique_values = list(set(four_last))

            if len(unique_values) == 4:
                break

        first_marker = counter

    print(f"answer: {first_marker}")


if __name__ == "__main__":
    main()