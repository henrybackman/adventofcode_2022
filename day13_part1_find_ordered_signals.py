import json
def get_data():
    data = []
    with open('data/day13_signal.data') as f:
        first = None
        for row in f:
            if len(row) == 1:
                first = None
                continue
            parsed = json.loads(row[:-1])
            if first is None:
                first = parsed
            else:
                data.append((first, parsed))
    return data


def is_correct_order(left, right):
    if right is None and left is not None:
        return False
    if right is not None and left is None:
        return True

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if left > right:
            return False
        if left == right:
            return True
    
    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]
    
    left_item = None
    right_item = None
    try:
        left_item = left.pop(0)
    except IndexError:
        left_item = None
    try:
        right_item = right.pop(0)
    except IndexError:
        right_item = None
    
    if left_item is None:
        return True
    
    if left_item == right_item:
        return is_correct_order(left, right)

    return is_correct_order(left_item, right_item)
        

def main():
    pairs = get_data()
    sum_of_indexes = 0
    for index, pair in enumerate(pairs):
        if not is_correct_order(pair[0], pair[1]):
            continue
        sum_of_indexes += index + 1

    print(f"answer: {sum_of_indexes}")

if __name__ == "__main__":
    main()
    # test()