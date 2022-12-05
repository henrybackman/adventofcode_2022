priorities = {}

counter = 1
for i in range(ord("a"), ord("z") + 1):
    priorities[chr(i)] = counter
    counter += 1
for j in range(ord("A"), ord("Z") + 1):
    priorities[chr(j)] = counter
    counter += 1

def main():

    with open('data/day03_rucksacks.data') as f:
        total_score = 0
        for row in f:
            # remove newline
            row = row[0:-1]
            index_of_second_half_start = int(len(row) / 2)
            first_half = row[0:index_of_second_half_start]
            second_half = row[index_of_second_half_start:]
            common_item = set(first_half).intersection(set(second_half)).pop()
            total_score += priorities[common_item]

    print(f"answer: {total_score}")

if __name__ == "__main__":
    main()