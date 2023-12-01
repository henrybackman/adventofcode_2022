import re
import math
from collections import deque
from icecream import ic
from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class Room():
    id: str
    flow_rate: int
    has_flow_rate: bool
    connected_rooms: List[str] = field(default_factory=list)
    paths: dict = field(default_factory=dict)

def get_data():
    rooms = {}
    with open('data/day16_valves.data') as f:
        for row in f:
            id = re.search(r'(?<=Valve )..', row).group()
            flow_rate = int(re.search(r'(?<=has flow rate=)\d+', row).group())
            s = re.search(r'(?<=tunnels lead to valves ).*', row)
            connected_rooms = None
            if s:
                connected_rooms = s.group().split(', ')

            room = Room(
                id=id, 
                flow_rate=flow_rate, 
                has_flow_rate=flow_rate > 0,
                connected_rooms=connected_rooms
            )

            rooms[id] = room
            
    return rooms

def shortest_path(rooms, start, end):
    paths = {start: [start]}
    q = deque([start])
    while len(q): # nodes left to check
        ic(q)
        current_node = q.popleft()
        ic(current_node)
        if not rooms[current_node]:
            continue
        for child_node in rooms[current_node]: # loop through all child nodes
            ic(child_node)
            if child_node not in paths: # if node seen first time, this is the shortest path to it
                paths[child_node] = paths[current_node] + [child_node]
                ic(paths[child_node])
                q.append(child_node)
    return paths.get(end)

def populate_paths(rooms: List[Room]):
    for room in rooms:
        paths = {room.id: [room.id]}
        q = deque([room])
        while len(q): # rooms left to check
            current_room = q.popleft()
            if not room.connected_rooms:
                continue
            for connected_room_id in current_room.connected_rooms: # loop through all connected rooms
                connected_room = rooms[connected_room_id]
                if connected_room_id not in paths: # if room seen first time, this is the shortest path to it
                    paths[connected_room_id] = paths[current_room.id] + [connected_room_id]
                    q.append(connected_room)
        room.paths = paths

def main():
    ic('getting data')
    rooms = get_data()
    # populate all shortest paths
    for room in rooms.values():
        room.paths = all_shortest_paths(rooms, room)
    ic(rooms)


# at each node can either open the valve or not
# nodes can be revisited both before and after their valves have been opened
# only reason to turn back is if a valve has been opened, this makes the backtrack paths available again
# each time a valve is opened, paths already done are available again
# instead of going minute by minute, could be faster to check in which order to open the valves
# need to find the shortest path to all other valves (not opened yet)

if __name__ == "__main__":
    main()
