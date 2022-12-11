def main():
    DATA = []
    with open('data/day08_tree_map.data') as f:
        COLS = None
        for row in f:
            trees = []
            for tree in row:
                try:
                    trees.append(int(tree))
                except:
                    # newline char will fail so can just continue
                    continue

            if not COLS:
                COLS = len(trees)
            DATA.append(trees)

    ROWS = len(DATA)
    coordinates_of_visible = set()
    # check rows
    for row in range(0, ROWS, 1):
        # check from left
        smallest_tree = -1
        for column in range(0, COLS, 1):
            tree = DATA[row][column]
            if tree > smallest_tree:
                smallest_tree = tree
                coordinates_of_visible.add((row, column))
        # check from right
        smallest_tree = -1
        for column in range(COLS - 1, -1, -1):
            tree = DATA[row][column]
            if tree > smallest_tree:
                smallest_tree = tree
                coordinates_of_visible.add((row, column))
    # check columns
    for column in range(0, COLS, 1):
        # check from up
        smallest_tree = -1
        for row in range(0, ROWS, 1):
            tree = DATA[row][column]
            if tree > smallest_tree:
                smallest_tree = tree
                coordinates_of_visible.add((row, column))
        # check from down
        smallest_tree = -1
        for row in range(ROWS - 1, -1, -1):
            tree = DATA[row][column]
            if tree > smallest_tree:
                smallest_tree = tree
                coordinates_of_visible.add((row, column))



    number_of_trees = len(coordinates_of_visible)
    print(f"answer: {number_of_trees}")

if __name__ == "__main__":
    main()

# 1265003 too low
# 1667443
# problem pwcvj
# pwcvj - 292769