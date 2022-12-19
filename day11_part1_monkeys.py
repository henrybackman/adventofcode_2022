

def test_function(n):
    def f(old):
        return not old % n
    return f

def operation_function(operation: str):
    if operation == "old * old":
        return lambda x: x * x
    addition_splits = operation.split(' + ')
    if len(addition_splits) == 2:
        return lambda x: x + int(addition_splits[1])
    multiply_splits = operation.split(' * ')
    return lambda x: x * int(multiply_splits[1])

class Monkey():
    def __init__(self, number:int , items, operation: str, test_value: int, true_monkey: int, false_monkey: int) -> None:
        self.number = number
        self.inspections = 0
        self.items = items
        self.operation = operation_function(operation)
        self.test = test_function(test_value)
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

MONKEYS = {}

def execute_round(monkey: Monkey):
    for item in monkey.items:
        monkey.inspections += 1
        worry_level = int(monkey.operation(item) / 3)
        target_monkey = None
        if monkey.test(worry_level):
            target_monkey = MONKEYS[monkey.true_monkey]
        else:
            target_monkey = MONKEYS[monkey.false_monkey]
        target_monkey.items.append(worry_level)
    monkey.items = []


def main():
    with open('data/day11_monkeys.data') as f:
        while True:
            number_line = next(f)[:-1]
            number = int(number_line[-2:-1])
            items_line = next(f)[:-1]
            items = [int(item) for item in items_line[18:].split(', ')]
            operation_line = next(f)[:-1]
            operation = operation_line.split(' = ')[1]
            test_line = next(f)[:-1]
            test_value = int(test_line.split(' ')[-1])
            true_monkey_line = next(f)[:-1]
            true_monkey = int(true_monkey_line[-1])
            false_monkey_line = next(f)[:-1]
            false_monkey = int(false_monkey_line[-1])
            monkey = Monkey(number, items, operation, test_value, true_monkey, false_monkey)
            MONKEYS[number] = monkey
            try:
                # try if still having an empty row
                _ = next(f)
            except:
                break
    monkey_business = 0

    for _ in range(1, 21):
        for monkey in MONKEYS.values():
            execute_round(monkey)

    inspection_counts = []
    for monkey in MONKEYS.values():
        inspection_counts.append(monkey.inspections)

    inspection_counts.sort(reverse=True)
    monkey_business = inspection_counts[0] * inspection_counts[1]
    print(f"answer: {monkey_business}")

if __name__ == "__main__":
    main()
