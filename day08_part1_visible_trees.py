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
    max_scenic_score = 0
    for row in range(ROWS):
        for column in range(COLS):
            if row == 3 and column == 2:
                pass
            tree = DATA[row][column]
            up_visibility = 0
            for vision_row in range(row - 1, -1, -1):
                up_visibility += 1
                visible_tree = DATA[vision_row][column]
                if visible_tree >= tree:
                    break
            down_visibility = 0
            for vision_row in range(row + 1, ROWS, 1):
                down_visibility += 1
                visible_tree = DATA[vision_row][column]
                if visible_tree >= tree:
                    break
            left_visibility = 0
            for vision_column in range(column - 1, -1, -1):
                left_visibility += 1
                visible_tree = DATA[row][vision_column]
                if visible_tree >= tree:
                    break
            right_visibility = 0
            for vision_column in range(column + 1, COLS, 1):
                right_visibility += 1
                visible_tree = DATA[row][vision_column]
                if visible_tree >= tree:
                    break
            scenic_score = up_visibility * down_visibility * left_visibility * right_visibility
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score



    print(f"answer: {max_scenic_score}")

if __name__ == "__main__":
    main()

# 1265003 too low
# 1667443
# problem pwcvj
# pwcvj - 292769