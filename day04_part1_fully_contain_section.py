import re
def main():

    with open('data/day04_sections.data') as f:
        fully_contained_count = 0
        for row in f:
            first_start = int(re.search('^\d+', row).group())
            first_end = int(re.search('-(\d+),', row).groups()[0])
            second_start = int(re.search(',(\d+)-', row).groups()[0])
            second_end = int(re.search('-(\d+)$', row).groups()[0])

            is_contained = False
            if first_start >= second_start and first_end <= second_end:
                is_contained = True
            if first_start <= second_start and first_end >= second_end:
                is_contained = True

            if is_contained:
                fully_contained_count += 1


    print(f"answer: {fully_contained_count}")

if __name__ == "__main__":
    main()