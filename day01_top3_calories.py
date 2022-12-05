
def main():

    with open('data/day01_elf_calories.data') as f:
        top3_calories = [0, 0, 0]
        current_calories = 0

        for row in f:
            try:
                current_calories += int(row)
                continue
            except ValueError:
                top3_calories[0] = max(current_calories, top3_calories[0])
                top3_calories.sort() # leaves the smallest as the first item
                current_calories = 0
    print(f"answer: {sum(top3_calories)}")

if __name__ == "__main__":
    main()