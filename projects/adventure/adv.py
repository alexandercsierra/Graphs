from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# def dft(starting_vertex, directions):
#         #uses a stack
#         start = starting_vertex
#         s = []
#         s.append(starting_vertex)
#         print('directions', directions)
#         visited = set()
#         directions = {}
#         while len(s) > 0:

#             current = s.pop()
#             if current not in visited:
#                 # print('current', current)
#                 visited.add(current)
#                 #add all neighbors to q
#                 neighbors = get_neighbors(dirs[current])
#                 print('neighbors', neighbors)
#                 for direction in neighbors:
#                     if neighbors[direction] != '?':
#                         directions[current] = ([direction,neighbors[direction]])
#                         s.append(neighbors[direction])
#         return directions

def dft(starting_vertex, directions):
        #uses a stack
        start = starting_vertex
        s = []
        s.append([starting_vertex][])
        visited = set()
        directions = {}

        while len(s) > 0:

            current = s.pop()
            if current not in visited:
                # print('current', current)
                visited.add(current)
                #add all neighbors to q
                neighbors = get_neighbors(dirs[current])
                for neighbor in neighbors:
                    print('neighbors', neighbor)
                    avail_path = dirs[neighbor]
                    print('path', avail_path)



        # print('visited', visited)
        return visited


def get_neighbors(directions):
    result = []
    # print(directions)
    for letter in directions:
        result.append(directions[letter])
    # print('result', result)
    return result



# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)



#########################################################################
traversal_path = []

dirs = {}
for room in room_graph:
    direction_dict = room_graph[room][1]
    if 'n' not in direction_dict:
        direction_dict['n'] = '?'
    if 's' not in direction_dict:
        direction_dict['s'] = '?'
    if 'e' not in direction_dict:
        direction_dict['e'] = '?'
    if 'w' not in direction_dict:
        direction_dict['w'] = '?'
    dirs[room] = direction_dict

paths = dft(list(room_graph.keys())[0], dirs)
# print('dirs', dirs)
#########################################################################






# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)
  

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")




#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
