class Rope_Piece():
    def __init__(self, place, next_rope_piece=False) -> None:
        self.x = 0
        self.y = 0
        self.place = place
        self.next_rope_piece = next_rope_piece


def move_head(head, direction):
    if direction == "R":
        head.x += 1
    if direction == "L":
        head.x -= 1
    if direction == "U":
        head.y += 1
    if direction == "D":
        head.y -= 1
    return head


def move_towards(current, target):
    # if x coordinates don't match, move towards target
    if target.x > current.x:
        current.x += 1
    elif target.x < current.x:
        current.x -= 1

    # if y coordinates don't match, move towards target
    if target.y > current.y:
        current.y += 1
    elif target.y < current.y:
        current.y -= 1
    
    return current

def get_tail_coordinates(head: Rope_Piece):
    current = head

    while True:
        previous = current
        current = previous.next_rope_piece
        # if previous is not within one space, move
        if abs(current.x - previous.x) > 1 \
            or abs(current.y - previous.y) > 1:
            current = move_towards(current=current, target=previous)

        if not current.next_rope_piece:
            # we are at tail piece
            break

    return (current.x, current.y)


def main():
    # create rope starting from tail
    current_place = 9
    tail = Rope_Piece(place=current_place)
    next_piece = tail
    for _ in range(9):
        current_place -= 1
        rope_piece = Rope_Piece(place=current_place, next_rope_piece=next_piece)
        next_piece = rope_piece
    head = rope_piece
    
    visited_spaces = 0
    movements = []
    with open('data/day09_movements.data') as f:
        for row in f:
            movements.append((row[0], int(row[2:-1])))


    tail_visited = set()
    for movement_info in movements:
        direction = movement_info[0]
        steps = movement_info[1]
        for _ in range(steps):
            head = move_head(head, direction)
            tail_coordinates = get_tail_coordinates(head)
            tail_visited.add(tail_coordinates)

    visited_spaces = len(tail_visited)


    print(f"answer: {visited_spaces}")

if __name__ == "__main__":
    main()
