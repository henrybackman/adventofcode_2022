from functools import cmp_to_key
import json
def get_data():
    data = []
    with open('data/day13_signal.data') as f:
        for row in f:
            if len(row) == 1:
                continue
            parsed = json.loads(row[:-1])
            data.append(parsed)
    return data


def compare_items(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        return 0
    
    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]
    
    return compare_lists(left, right)

def compare_lists(left, right):
    if not left:
        return -1
    
    for index, left_item in enumerate(left):
        right_item = None
        try:
            right_item = right[index]
        except IndexError:
            return 1
        comparison = compare_items(left_item, right_item)
        if not comparison:
            continue
        return comparison
    if len(right) > len(left):
        return -1        
    return 0
 

def main():
    signals = get_data()
    KEY1 = [[2]]
    KEY2 = [[6]]
    signals.extend([KEY1, KEY2])
    sorted_signals = sorted(signals, key=cmp_to_key(compare_lists))
    key1_index = None
    key2_index = None
    for index, signal in enumerate(sorted_signals):
        if signal == KEY1:
            key1_index = index + 1
        if signal == KEY2:
            key2_index = index + 1
    product_of_key_index = key1_index * key2_index

    print(f"answer: {product_of_key_index}")

    # with open('data/day13_output.data', 'w') as f:
    #     for signal in sorted_signals:
    #         f.write(str(signal) + '\n')

if __name__ == "__main__":
    main()
