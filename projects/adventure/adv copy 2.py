from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue





def get_questions(directions, dirs):
    dirs_dict = dirs[directions]
    neighbors = list(dirs_dict.values())
    return neighbors



def dft(starting_vertex, dirs, master):
    start = starting_vertex 
    s = []
    s.append(starting_vertex)

    visited = set()
    visited_list = []
    dirs2 = dirs.copy()
    
    while len(s) > 0:
        print('stack', s)
        current = s.pop()
        print('current', current)
        visited_list.append(current)
        print('dirs', dirs2)

        if current not in visited:
            neighbors = get_questions(current, dirs2)
            # print('directions', neighbors)
            if neighbors[0] != '?' and neighbors[1] != '?' and neighbors[2] != '?' and neighbors[3] != '?':
                visited.add(current)

            old_dirs = dirs2[current]
            for direction in dirs2[current]:
                print('current is', current)
                if dirs2[current][direction] == '?':
                    print('old_dirs before', old_dirs)
                    if direction in master[current]:
                        if master[current][direction] not in visited:
                            s.append(master[current][direction])
                            old_dirs[direction] = master[current][direction]
                            dirs2[current] = old_dirs
                    else:
                        old_dirs[direction] = None
                        print('old_dirs', old_dirs)
                        dirs2[current] = old_dirs
        


    # print('visited_list', visited_list)
    return visited_list




def traverse_maze(entrance, dirs, master):
    rooms = dft(entrance, dirs, master)
    print('rooms', rooms)



# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
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
master_list = {}
question_list = {'n':'?', 's':'?', 'e':'?', 'w':'?'}
for room in room_graph:
    master_list[room] = room_graph[room][1]
    dirs[room] = question_list



paths = traverse_maze(list(room_graph.keys())[0], dirs, master_list)
# traversal_path = paths
# print('returning', paths)
# print('dirs', dirs)
#########################################################################






# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    # print('move', move)
    player.travel(move)
    # print('current_room', player.current_room)
    visited_rooms.add(player.current_room)
  

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
    print(f"{len(room_graph)} total rooms")
    print(f"{len(traversal_path)} moves")




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



'''
Pick a neighbor
create a stack for that neighbor
create a master directions list
traverse until all directions are ? except already visited nodes, adding each direction to the master list
at this point should have a stack of nodes and directions [[None, 0],[n,1],[n,2]]
pop off stack adding opposite direction to a list of directions
when the stack is empty, we have reached the starting node, mark the opposite of the last direction in the master list as ?. Ex: None 0, n,1 , n,2, s,1, s,0  - mark the north direction of 0 as complete by changing it to a ?
when only question marks remain on the starting node, we have explored every room.


'''


