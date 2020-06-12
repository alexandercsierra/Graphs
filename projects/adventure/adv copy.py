from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue





def get_neighbors(directions, dirs):
    dirs_dict = dirs[directions]
    neighbors = list(dirs_dict.values())
    return neighbors

def get_opp_direction(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'e':
        return 'w'
    elif direction == 'w':
        return 'e'
    else:
        return None


def get_final_path(rooms, dirs):
    final_list= []
    for i in range(len(rooms)-1):
        cardinals = list(dirs[rooms[i]].keys())
        room_names = list(dirs[rooms[i]].values())

        # print(rooms[i], 'to', rooms[i+1])
        if rooms[i+1] in room_names:
            index = room_names.index(rooms[i+1])
            card = cardinals[index]
            # print('direction', card)
            final_list.append(rooms[i])
        else:
            connection = find_path(rooms[i], rooms[i+1], dirs)
            final_list += connection
        i+=1
    return final_list

def find_path(starting_vertex, destination_vertex, dirs):
        
        start = starting_vertex
        q = Queue()
        q.enqueue([starting_vertex])

        while q.size() > 0:
            current_path = q.dequeue()
            if current_path[-1] == destination_vertex:
                return current_path

            for vert in get_neighbors(current_path[-1], dirs):
                if vert != "?":
                    new_path = [*current_path, vert]
                    q.enqueue(new_path)
    

def dft(starting_vertex, dirs):
    start = starting_vertex 
    s = []
    s.append(starting_vertex)

    visited = set()
    visited_list = []
    while len(s) > 0:

        current = s.pop()
        visited_list.append(current)
        if current not in visited:
            visited.add(current)

            neighbors = get_neighbors(current, dirs)
            for vert in neighbors:
                if vert != "?":
                    #dont append if already visited?
                    s.append(vert)

    # print('visited_list', visited_list)
    return visited_list

def get_directions(path, dirs):

    directions = []
    for i in range(len(path)-1):
        cardinals = list(dirs[path[i]].keys())
        room_names = list(dirs[path[i]].values())

        index = room_names.index(path[i+1])
        card = cardinals[index]
        directions.append(card)

    return directions



def traverse_maze(entrance, dirs):
    print('entrance', entrance)
    rooms = dft(entrance, dirs)
    room_set = set(rooms)
    print('length', len(room_set))
    path = get_final_path(rooms, dirs)
    keys = list(dirs.keys())
    print('keys', len(keys))
    count = set()
    path_no_dupes = []
    for i in range(len(path)-1):
        if path[i] != path[i+1]:
            path_no_dupes.append(path[i])
    for room in path_no_dupes:
        if room in keys:
            count.add(room)
    print('count', len(count))

    traversal_directions = get_directions(path_no_dupes, dirs)
    # print(traversal_directions)
    return traversal_directions



# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

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

start = list(room_graph.keys()).index(0)
paths = traverse_maze(list(room_graph.keys())[start], dirs)
if dirs[0]['n'] != '?':
    traversal_path = ['n','s',*paths]
else:
    traversal_path = paths

    
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
    print(f"{len(visited_rooms)} visited rooms")
    print(f"{len(traversal_path)} moves")
    names = []
    for room in visited_rooms:
        names.append(room.name)
    nums = []
    for name in names:
        for letter in name.split():
            if letter.isdigit():
                nums.append(int(letter))
    nums.sort()
    # print('nums', nums)
    for i in range(500):
        if i not in nums:
            print('missing', i)
   




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


