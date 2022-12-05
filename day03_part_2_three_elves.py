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
        while True:
            group = []
            try:
                group.append(next(f)[0:-1])
                group.append(next(f)[0:-1])
                group.append(next(f)[0:-1])
            except StopIteration:
                break
            common_item = set(group[0])\
                .intersection(group[1])\
                .intersection(group[2])\
                .pop()
            total_score += priorities[common_item]

    print(f"answer: {total_score}")

if __name__ == "__main__":
    main()