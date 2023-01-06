import re
import math
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


def main():
    global MIN_X
    global MAX_X
    Y_TO_CHECK = 10
    Y_TO_CHECK = 2000000
    print('getting data')
    data = get_data()

    print('creating sensors')
    sensors = []
    for sensor_xy, beacon_xy in data:
        sensor = Sensor(sensor_xy, beacon_xy)
        sensors.append(sensor)

    # update limits
    for sensor in sensors:
        MIN_X = min(MIN_X, sensor.x - sensor.beacon_distance)
        MAX_X = max(MAX_X, sensor.x + sensor.beacon_distance)
    
    print('finding impossible locations')
    y = Y_TO_CHECK      
    impossible_locations = 0
    for x in range(MIN_X, MAX_X + 1):
        location_possible = True
        for sensor in sensors:
            if (x, y) == sensor.beacon_xy:
                location_possible = True
                break
            if get_distance((x, y), sensor.xy) <= sensor.beacon_distance:
                # print(x, y)
                location_possible = False
                break
        
        if not location_possible:
            impossible_locations += 1
    print(f'answer: {impossible_locations}')

if __name__ == "__main__":
    main()

# 4389717 too low
# 5500272 too low