import re

CONTAINER_WIDTH = 4

def get_containers(row):
    containers = []
    for i in range(9):
        start_index = i * CONTAINER_WIDTH
        end_index = (i + 1) * CONTAINER_WIDTH - 1
        container = row[start_index:end_index]
        contents = container[1] if container[1] != ' ' else None
        containers.append(contents)
    return containers


def move_containers(stacks, moves, from_stack, to_stack):
    for _ in range(moves):
        container = stacks[from_stack - 1].pop()
        stacks[to_stack - 1].append(container)
    return stacks

def main():

    with open('data/day05_crane_operations.data') as f:
        stacks = [[] for _ in range(9)]

        # collect starting position
        for row in f:
            if row[1] == "1":
                break
            containers = get_containers(row)
            for i, container in enumerate(containers):
                stacks[i].append(container)

        # reorder stacks from bottom to top and remove empties
        for stack_index, stack in enumerate(stacks):
            stack.reverse()
            pruned_stack = [content for content in stack if content]
            stacks[stack_index] = pruned_stack

        # process operations, skip empty line and then continue through rows
        next(f)
        for row in f:
            moves = int(re.search('move (\d+) ', row).groups()[0])
            from_stack = int(re.search('from (\d+) ', row).groups()[0])
            to_stack = int(re.search('to (\d+)$', row).groups()[0])
            stacks = move_containers(stacks, moves, from_stack, to_stack)

        top_containers = ''
        for stack in stacks:
            top_containers += stack.pop()

    print(f"answer: {top_containers}")


if __name__ == "__main__":
    main()