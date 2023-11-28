import re
import math
from collections import deque
from icecream import ic

def get_data():
    data = []
    with open('data/day16_valves.data') as f:
        for row in f:
            valve_name = re.search(r'(?<=Valve )..', row).group()
            flow_rate = re.search(r'(?<=has flow rate=)\d+', row).group()
            s = re.search(r'(?<=tunnels lead to valves ).*', row)
            connected_valves = None
            if s:
                connected_valves = s.group().split(', ')
            data.append((valve_name, flow_rate, connected_valves))
    return data

def shortest_path(graph, start, end):
    ic(graph)
    dist = {start: [start]}
    q = deque([start])
    while len(q):
        ic(q)
        at = q.popleft()
        ic(at)
        if not graph[at]:
            continue
        for next in graph[at]:
            ic(next)
            if next not in dist:
                dist[next] = dist[at] + [next]
                ic(dist[next])
                q.append(next)
    return dist.get(end)

def create_graph(d):
    graph = {}
    for valve, _, valves in d:
        graph[valve] = valves
    return graph

def get_closed_valves(d):
    valves = []
    for valve, flow_rate in d:
        if flow_rate:
            valves.append(valve)
    return valves

def main():
    ic('getting data')
    data = get_data()
    ic(data)
    graph = create_graph(data)
    ic(graph)
    valves_to_open = get_closed_valves(data)
    ic(valves_to_open)
    ic(shortest_path(graph, 'AA', 'CC'))
    ic(shortest_path(graph, 'CC', 'AA'))


# at each node can either open the valve or not
# nodes can be revisited both before and after their valves have been opened
# only reason to turn back is if a valve has been opened, this makes the backtrack paths available again
# each time a valve is opened, paths already done are available again
# instead of going minute by minute, could be faster to check in which order to open the valves
# need to find the shortest path to all other valves (not opened yet)

if __name__ == "__main__":
    main()
