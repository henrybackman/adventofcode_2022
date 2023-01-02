import math
min_x = math.inf
max_x = 0
max_y = 0

def get_data():
    global min_x
    global max_x
    global max_y
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

    # @staticmethod
    # def get_direction(start, end):
    #     if start[0] < end[0]:
    #         return 'RIGHT'
    #     if start[0] > end[0]:
    #         return 'LEFT'
    #     if start[1] < end[1]:
    #         return 'DOWN'
    #     return 'UP'

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

    def get_next_free(self, y, x):
        if self.map[y + 1][x] == '.':
            return (y + 1, x)
        if self.map[y + 1][x - 1] == '.':
            return (y + 1, x - 1)
        if self.map[y + 1][x + 1] == '.':
            return (y + 1, x + 1)
        return None
    

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
            try:
                down_symbol = self.map[next_y][down_x]
            except IndexError:
                down_symbol = ''
            try:
                left_symbol = self.map[next_y][left_x]
            except IndexError:
                left_symbol = ''
            try:
                right_symbol = self.map[next_y][right_x]
            except IndexError:
                right_symbol = ''
            
            if down_symbol == '':
                return False
            elif down_symbol == '.':
                y = next_y
                x = down_x
            elif left_symbol == '':
                return False
            elif left_symbol == '.':
                y = next_y
                x = left_x
            elif right_symbol == '':
                return False
            elif right_symbol == '.':
                y = next_y
                x = right_x
            else:
                self.map[y][x] = 'o'
                return True
        

def main():
    data = get_data()
    dungeon = Dungeon(max_y, max_x, 500 - min_x)
    for wall_coordinates in data:
        dungeon.add_wall(wall_coordinates)
    sand_count = 0
    while True:
        success = dungeon.drop_sand()
        if not success:
            break
        sand_count += 1
    dungeon.print_map()
    print(f'answer: {sand_count}')

if __name__ == "__main__":
    main()
