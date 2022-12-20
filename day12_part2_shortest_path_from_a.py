import math
import sys
sys.setrecursionlimit(10**6)

TARGET = None
TERRAIN = None
MIN_PATH_LENGTH = math.inf

def get_candidates(coordinates):
    x = coordinates[0]
    y = coordinates[1]
    current_elevation = TERRAIN[y][x]
    possible_coordinates = []
    candidates = []
    try:
        candidates.append({
            "x": x + 1, "y": y,
            "elevation": TERRAIN[y][x + 1]
        })
    except:
        pass
    try:
        candidates.append({
            "x": x, "y": y + 1,
            "elevation": TERRAIN[y + 1][x]
        })
    except:
        pass
    try:
        assert(y - 1 >= 0)
        candidates.append({
            "x": x, "y": y - 1,
            "elevation": TERRAIN[y - 1][x]
        })
    except:
        pass
    try:
        assert(x - 1 >= 0)
        candidates.append({
            "x": x - 1, "y": y,
            "elevation": TERRAIN[y][x - 1]
        })
    except:
        pass
    for candidate in candidates:
        if current_elevation - candidate["elevation"] <= 1:
            possible_coordinates.append((candidate["x"], candidate["y"]))
    return possible_coordinates

def get_terrain():
    global TARGET
    global TERRAIN
    TERRAIN = []
    with open('data/day12_terrain.data') as f:
        y = -1
        for row in f:
            y += 1
            x = -1
            TERRAIN.append([])
            for char in row[:-1]:
                x += 1
                if char == "S":
                    elevation = 0
                elif char == "E":
                    TARGET = (x, y)
                    elevation = 25
                else:
                    elevation = ord(char) - 97
                TERRAIN[y].append(elevation)
    return TERRAIN

PATHS = {}

def find_shortest_path(path: list):
    global MIN_PATH_LENGTH
    if len(path) >= MIN_PATH_LENGTH:
        return
    candidates = get_candidates(path[-1])
    possible_paths_to_target = []
    for candidate in candidates:
        if candidate in path:
            continue
        path_candidate = path.copy()
        path_candidate.append(candidate)
        if candidate in PATHS:
            if len(path_candidate) >= PATHS[candidate]:
                continue # this path isn't shorter than already exists
        if TERRAIN[candidate[1]][candidate[0]] == 0:
            # found min elevation
            MIN_PATH_LENGTH = len(path_candidate)
            return path_candidate
        PATHS[candidate] = len(path_candidate)
        candidate_path_to_target = find_shortest_path(path_candidate)
        if candidate_path_to_target:
            possible_paths_to_target.append(candidate_path_to_target)
    shortest_path = None
    for possible_path in possible_paths_to_target:
        if not shortest_path:
            shortest_path = possible_path
        if len(possible_path) < len(shortest_path):
            shortest_path = possible_path

    return shortest_path

def main():
    get_terrain()
    shortest_path = find_shortest_path([TARGET])
    min_steps = len(shortest_path) - 1

    print(f"answer: {min_steps}")

# def test():
#     terrain = get_terrain()
#     possible = get_candidates(terrain=terrain, x=5, y=2)
#     print(possible)

if __name__ == "__main__":
    main()
    # test()