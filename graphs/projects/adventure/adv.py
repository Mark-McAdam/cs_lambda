from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# from collections import deque  # double ended queue will handle

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
# these are the rooms to explore in the "Maze"
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# we will create a long list of N S E W entries that correspond
# to the path we traverse to explore the maze
traversal_path = []


# TODO my code here
# graph to hold rooms I have visited.
# will contain explored exits
visited = {}

# pathfinder keeps track of where I am going
# in case I need to circle back and start again
# hold list of room ids
pathfinder = [world.starting_room.id]

# starting room goes into visited
# assume we visited the room we start in
visited[world.starting_room.id] = {}

# take note of the exits
# mark exits as "?" unknown
# if we mark every exit as unknown
# we can come back later and explore the unknown only
room_exits = world.starting_room.get_exits()
for exits in room_exits:
    visited[world.starting_room.id][exits] = "?"

# TODO -    Refactor this to use bfs to not need to pick random direction
#           Design it to pick the shortest path to a ?


# backtracking direction function
# takes direction as input and gives opposite direction
def backtrack_direction(direction):
    if direction == "n":
        direction = "s"
    elif direction == "s":
        direction = "n"
    elif direction == "e":
        direction = "w"
    elif direction == "w":
        direction = "e"

    return direction


# main loop to control movement and path

# so long as we have visited less rooms than total rooms to explore
while len(visited) < len(room_graph):
    room = pathfinder[-1]

    # case 1 room not in visited already
    if room not in visited:
        visited[player.current_room.id] = {}
        room_exits = player.current_room.get_exits()
        for exits in room_exits:
            visited[player.current_room.id][exits] = "?"

    # TODO !!! do I need the random_move inside the while loop or is global scope ok
    # Lets see if I need later
    # start going in random direction
    # take players current room exits and make random choice from available exits
    random_move = random.choice(player.current_room.get_exits())

    if visited[player.current_room.id][random_move] is "?":
        # save current room into room_visited
        room_travelled = player.current_room.id

        # move player in the random direction selected
        player.travel(random_move)

        # append direction travelled to my sweet maze dance moves list
        traversal_path.append(random_move)

        # get id of new room
        new_room = player.current_room.id

        # append the relationship of the previous
        # room and the new current room to visited graph
        # the relationship is important for when I come back
        visited[room_travelled][random_move] = new_room

        # what goes up must also go down etc
        backtrack = backtrack_direction(random_move)

        # now repeat the process with the new room I find myself in
        if player.current_room.id not in visited:
            visited[player.current_room.id] = {}
            room_exits = player.current_room.get_exits()
            for exits in room_exits:
                visited[player.current_room.id][exits] = "?"

        visited[new_room][backtrack] = room_travelled

        # append id to pathfinder so we can start the whole process over
        pathfinder.append(player.current_room.id)

    # case 2 ? not in visited
    if "?" not in visited[player.current_room.id].values():

        # if not a ? in visited we need to start the backtrack
        # if length of pathfinder is 1 we are back at starting room
        if len(pathfinder) > 1:
            for key, value in visited[player.current_room.id].items():
                if value == pathfinder[-2]:
                    cardinal_direction = key
            player.travel(cardinal_direction)
            traversal_path.append(cardinal_direction)
            # keep popping rooms off pathfinder until back to unexplored place
            pathfinder.pop()


# Test file function below for checking our work at end of sprint challenge
# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
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
