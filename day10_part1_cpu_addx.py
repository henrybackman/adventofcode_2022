CYCLE_TIMES = {
    "noop": 1,
    "addx": 2
}

class Instruction():
    def __init__(self, type) -> None:
        self.type = type
        self.add_value = 0
        self.cycles_left = CYCLE_TIMES[type]
        self.is_completed = False

    def run_cycle(self, X):
        self.cycles_left -= 1
        if self.cycles_left == 0:
            self.is_completed = True
            X = self.execute_instruction(X)
        return X
    
    def execute_instruction(self, X):
        if self.type == "addx":
            X += self.add_value
        return X

def main():
    instructions = []
    X = 1
    with open('data/day10_instructions.data') as f:
        for row in f:
            instruction_type = row[0:4]
            intrs = Instruction(type=instruction_type)
            if intrs.type == "addx":
                intrs.add_value = int(row[5:-1])
            instructions.append(intrs)

    signal_strengths = 0
    cycle_count = 0
    next_check_cycle = 20

    instruction = None
    while instructions or instruction:
        if not instruction:
            instruction = instructions.pop(0)
        cycle_count += 1
        if cycle_count == next_check_cycle:
            signal_strengths += X * cycle_count
            next_check_cycle += 40
        X = instruction.run_cycle(X)
        if instruction.is_completed:
            instruction = None

    print(f"answer: {signal_strengths}")

if __name__ == "__main__":
    main()
