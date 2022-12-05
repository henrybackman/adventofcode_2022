
def main():

    with open('data/day01_elf_calories.data') as f:
        max_calories = 0
        current_calories = 0

        for row in f:
            try:
                current_calories += int(row)
                continue
            except ValueError:
                max_calories = max(current_calories, max_calories)
                current_calories = 0
    print(f"answer: {max_calories}")

if __name__ == "__main__":
    main()