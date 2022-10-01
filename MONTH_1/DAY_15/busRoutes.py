from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        if target == source: return 0
        stops = {}
        adj = [[] for x in range(len(routes))]
        visited, target_busses = set(), set()
        for bus_id, bus in enumerate(routes):
            if source in bus:
                visited.add(bus_id)

            if target in bus:
                target_busses.add(bus_id)

            if target in bus and source in bus:
                return 1

            for stop in bus:
                stops[stop] = stops.get(stop, [])
                for bus_stopping in stops[stop]:
                    if bus_id not in adj[bus_stopping]:
                        adj[bus_stopping].append(bus_id)
                    if bus_stopping not in adj[bus_id]:
                        adj[bus_id].append(bus_stopping)


                stops[stop].append(bus_id)
        
        Q = deque((bus, 1) for bus in visited)

        while Q:
            (bus, distance) = Q.popleft()
            visited.add(bus)
            if bus in target_busses: return distance
            for neighbor in adj[bus]:
                if neighbor not in visited:
                    Q.append((neighbor, distance+1))
        
        return -1            


sol = Solution()
routes = [[1,9,12,20,23,24,35,38],[10,21,24,31,32,34,37,38,43],[10,19,28,37],[8],[14,19],[11,17,23,31,41,43,44],[21,26,29,33],[5,11,33,41],[4,5,8,9,24,44]]
source = 37
target = 28
print(sol.numBusesToDestination(routes, source, target))










# DOESNT WORK BUT INTERESTING IDEAS USED
# class Solution:
#     def numBusesToDestination(self, routes, source: int, target: int) -> int:
#         if target == source: return 0
#         N_BUSES = len(routes)
#         routes = list(map(set, routes))
#         adj = defaultdict(set)
        
#         visited, finishing = set(), set()
#         for bus_id, bus_stops in enumerate(routes):
#             if source in bus_stops: visited.add(bus_id)
#             if target in bus_stops: finishing.add(bus_id)

#             for bus2_id in range(bus_id+1, N_BUSES):
#                 bus2_stops = routes[bus2_id]
#                 if any(stop in bus2_stops for stop in bus_stops):
#                     adj[bus_id].add(bus2_id)
#                     adj[bus2_id].add(bus_id)
        
#         Q = deque([(bus, 1) for bus in visited])
        
#         while Q:
#             (bus, distance) = Q.popleft()
#             if bus in finishing:
#                 return distance
#             for neighbor in adj[bus]:
#                 if neighbor not in visited:
#                     Q.append((neighbor, distance+1))
        
#         return -1

# OLD SOLUTION
# class Solution:
#     def numBusesToDestination(self, routes, source: int, target: int) -> int:
#         if target == source: return 0
#         stops = {}
#         adj = [[] for x in range(len(routes))]
#         vis = [-1 for x in range(len(routes))]
#         first_bus = None
#         target_busses = {}
#         for bus_id, bus in enumerate(routes):
#             if source in bus and first_bus is None:
#                 first_bus = bus_id
#             effective_bus = first_bus if source in bus else bus_id

#             if target in bus:
#                 target_busses[bus_id] = 1
            
#             if target in bus and source in bus:
#                 return 1

#             for stop in bus:
#                 stops[stop] = stops.get(stop, [])
#                 for bus_stopping in stops[stop]:
#                     if effective_bus not in adj[bus_stopping]:
#                         adj[bus_stopping].append(effective_bus)
#                     if bus_stopping not in adj[effective_bus]:
#                         adj[effective_bus].append(bus_stopping)


#                 stops[stop].append(bus_id)
        
#         Q = deque()
#         Q.append((first_bus, 1))

#         while Q:
#             (bus, distance) = Q.popleft()
#             vis[bus] = distance
#             if bus in target_busses:
#                 return vis[bus]
#             for neighbor in adj[bus]:
#                 if vis[neighbor] == -1:
#                     Q.append((neighbor, distance+1))
        
#         return -1

