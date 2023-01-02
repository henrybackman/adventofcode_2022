import math
min_x = math.inf
max_x = 0
max_y = 0
floor_y = 0

def get_data():
    global min_x
    global max_x
    global max_y
    global floor_y
    data = []
    with open('data/day14_dungeon.data') as f:
        for row in f:
            line = row[:-1]
            wall_coordinates = []
            for coordinate_str in line.split(' -> '):
                x = int(coordinate_str.split(',')[0])
                y = int(coordinate_str.split(',')[1])
                wall_coordinates.append((y, x))
                min_x = min(min_x, x)
            data.append(wall_coordinates)
    # return data

    adjusted_data = []
    for wall_coordinates in data:
        adjusted_wall_coordinates = []
        for wall_part in wall_coordinates:
            x = wall_part[1] - min_x
            y = wall_part[0]
            adjusted_wall_coordinates.append((y, x))
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        adjusted_data.append(adjusted_wall_coordinates)
    floor_y = max_y + 2
    return adjusted_data

class Dungeon():
    def __init__(self, y_size, x_size, sand_x) -> None:
        self.sand_x = sand_x
        map = []
        for _ in range(y_size + 1):
            row = []
            for _ in range(x_size + 1):
                row.append('.')
            map.append(row)
        self.map = map

    def is_occupied(self, y, x):
        return not self.map[y][x] == '.'

    def print_map(self):
        for row in self.map:
            row_str = ''
            for symbol in row:
                row_str += symbol
            print(row_str)

    def add_wall_part(self, start, end):
        min_x 
        xs = list(range(min(start[1], end[1]), max(start[1], end[1]) + 1))
        ys = list(range(min(start[0], end[0]), max(start[0], end[0]) + 1))
        for y in ys:
            for x in xs:
                self.map[y][x] = '#'
        

    def add_wall(self, wall_coordinates):
        start = None
        for coordinates in wall_coordinates:
            if not start:
                start = coordinates
                continue

            self.add_wall_part(start, coordinates)
            start = coordinates
    
    
    def expand_map_to_left(self):
        new_map = []
        for row in self.map:
            new_row = ['.'] + row
            new_map.append(new_row)
        self.map = new_map
    
    
    def expand_map_to_right(self):
        new_map = []
        for row in self.map:
            new_row = row + ['.']
            new_map.append(new_row)
        self.map = new_map


    def drop_sand(self):
        y = 0
        x = self.sand_x
        while True:
            next_y = y + 1
            down_x = x
            left_x = x - 1
            right_x = x + 1
            down_symbol = None
            left_symbol = None
            right_symbol = None

            down_symbol = self.map[next_y][down_x]
            if left_x == -1:
                self.expand_map_to_left()
                x += 1
                left_x += 1
                down_x += 1
                right_x += 1
                self.sand_x += 1

            left_symbol = self.map[next_y][left_x]
            try:
                right_symbol = self.map[next_y][right_x]
            except IndexError:
                self.expand_map_to_right()
                right_symbol = '.'
            
            if y == 0 and \
                down_symbol == 'o' and \
                left_symbol == 'o' and \
                right_symbol == 'o':
                return False
            elif next_y == floor_y:
                self.map[y][x] = 'o'
                return True
            elif down_symbol == '.':
                y = next_y
                x = down_x
            elif left_symbol == '.':
                y = next_y
                x = left_x
            elif right_symbol == '.':
                y = next_y
                x = right_x
            else:
                self.map[y][x] = 'o'
                return True
        

def main():
    data = get_data()
    dungeon = Dungeon(floor_y, max_x, 500 - min_x)
    for wall_coordinates in data:
        dungeon.add_wall(wall_coordinates)
    sand_count = 1
    while True:
        success = dungeon.drop_sand()
        if not success:
            break
        sand_count += 1
    dungeon.print_map()
    print(f'answer: {sand_count}')

if __name__ == "__main__":
    main()
