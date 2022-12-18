def move_head(coordinates, direction):
    if direction == "R":
        return (coordinates[0] + 1, coordinates[1])
    if direction == "L":
        return (coordinates[0] - 1, coordinates[1])
    if direction == "U":
        return (coordinates[0], coordinates[1] + 1)
    if direction == "D":
        return (coordinates[0], coordinates[1] - 1)

def get_tail_coordinates(tail_coordinates, head_coordinates):
    tail_x = tail_coordinates[0]
    tail_y = tail_coordinates[1]
    head_x = head_coordinates[0]
    head_y = head_coordinates[1]

    # if head is within one space, no need to move
    if abs(tail_x - head_x) < 2 \
        and abs(tail_y - head_y) < 2:
        return tail_coordinates

    # if x coordinates don't match, move towards head
    if head_x > tail_x:
        tail_x += 1
    elif head_x < tail_x:
        tail_x -= 1

    # if y coordinates don't match, move towards head
    if head_y > tail_y:
        tail_y += 1
    elif head_y < tail_y:
        tail_y -= 1

    return (tail_x, tail_y)


def main():
    visited_spaces = 0
    movements = []
    with open('data/day09_movements.data') as f:
        for row in f:
            movements.append((row[0], int(row[2:-1])))

    head_coordinates = (0,0)
    tail_coordinates = (0,0)
    tail_visited = set()
    for movement_info in movements:
        direction = movement_info[0]
        steps = movement_info[1]
        for _ in range(steps):
            head_coordinates = move_head(head_coordinates, direction)
            tail_coordinates = get_tail_coordinates(tail_coordinates, head_coordinates)
            tail_visited.add(tail_coordinates)

    visited_spaces = len(tail_visited)


    print(f"answer: {visited_spaces}")

if __name__ == "__main__":
    main()
