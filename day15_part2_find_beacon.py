import re
import math
import time
MIN_Y = math.inf
MAX_Y = -math.inf
MIN_X = math.inf
MAX_X = -math.inf

def get_data():
    global MIN_Y
    global MAX_Y
    global MIN_X
    global MAX_X
    data = []
    with open('data/day15_sensors.data') as f:
        for row in f:
            matches = re.findall("(?:x=|y=)(-?\d+)", row)
            sensor_x, sensor_y, beacon_x, beacon_y = matches
            sensor_x = int(sensor_x)
            sensor_y = int(sensor_y)  
            beacon_x = int(beacon_x)
            beacon_y = int(beacon_y)
            MAX_Y = max(sensor_y, beacon_y, MAX_Y)
            MIN_Y = min(sensor_y, beacon_y, MIN_Y) 
            MAX_X = max(sensor_x, beacon_x, MAX_X)
            MIN_X = min(sensor_x, beacon_x, MIN_X) 

            sensor_xy = (sensor_x, sensor_y)
            beacon_xy = (beacon_x, beacon_y)
            data.append((sensor_xy, beacon_xy))
    return data

def get_distance(a_xy, b_xy):
    # manhattan distance between two coordinates
    ax, ay = a_xy
    bx, by = b_xy
    dist_x = abs(ax - bx)
    dist_y = abs(ay - by)
    return dist_x + dist_y

class Sensor():
    def __init__(self, sensor_xy, closest_beacon_xy) -> None:
        x, y = sensor_xy
        self.x = x
        self.y = y
        self.xy = sensor_xy
        beacon_x, beacon_y = closest_beacon_xy
        self.beacon_x = beacon_x
        self.beacon_y = beacon_y
        self.beacon_xy = closest_beacon_xy
        self.beacon_distance = get_distance(self.xy, self.beacon_xy)


def get_cells_at_distance(x, y, distance):
    cells = []
    x_offset = 0
    y_offset = distance - x_offset
    cell_xy = (x + x_offset, y + y_offset)
    cells.append(cell_xy)
    for _ in range(distance):
        x_offset += 1
        y_offset -= 1
        cell_xy = (x + x_offset, y + y_offset)
        cells.append(cell_xy)
    for _ in range(distance):
        x_offset -= 1
        y_offset -= 1
        cell_xy = (x + x_offset, y + y_offset)
        cells.append(cell_xy)
    for _ in range(distance):
        x_offset -= 1
        y_offset += 1
        cell_xy = (x + x_offset, y + y_offset)
        cells.append(cell_xy)
    for _ in range(distance):
        x_offset += 1
        y_offset += 1
        cell_xy = (x + x_offset, y + y_offset)
        cells.append(cell_xy)
    return cells


def main():
    start = time.time()
    print('getting data')
    data = get_data()

    print('creating sensors')
    sensors = []
    for sensor_xy, beacon_xy in data:
        sensor = Sensor(sensor_xy, beacon_xy)
        sensors.append(sensor)

    SEARCH_MIN = 0
    SEARCH_MAX = 4000000
    # SEARCH_MAX = 20
    for sensor in sensors:
        print(f'getting cells for sensor {sensor.xy} distance {sensor.beacon_distance}')
        cells = get_cells_at_distance(sensor.x, sensor.y, sensor.beacon_distance + 1)
        print(f'check cells around the sensor search area: {len(cells)}')
        is_valid_cell = False
        for cell_xy in cells:
            if cell_xy[0] < SEARCH_MIN or \
                cell_xy[0] > SEARCH_MAX or \
                cell_xy[1] < SEARCH_MIN or \
                cell_xy[1] > SEARCH_MAX:
                continue
            is_valid_cell = True
            for search_sensor in sensors:
                if search_sensor == sensor:
                    continue
                if get_distance(cell_xy, search_sensor.xy) <= search_sensor.beacon_distance:
                    is_valid_cell = False
            if is_valid_cell:
                print(f'found valid cell: {cell_xy}')
                break
        if is_valid_cell:
            break
    if not is_valid_cell:
        raise Exception('NO CELL FOUND')
    tuning_frequency = cell_xy[0] * 4000000 + cell_xy[1]
    print(f'answer: {tuning_frequency}')
    end = time.time()
    print(f'execution time: {end - start}')

if __name__ == "__main__":
    main()
