# please check analysis.md for understanding of the solution and the algorithm and for space and time complexity analysis.
# for math part please check problem1.jpg

def escape_maze(maze: list[list[str]]) -> list[tuple[int, int]]:
    escape_path = list() # here we are going to store our path
    movement_vectors = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1)] # ways we can move
    s = find_s(maze) #function checks all elements and returns tuple (x,y) for the first occurence of S
    x = s[0]
    y = s[1] # better not to use tuples further in traverse() as they are immutable
    state = {
        "found" : False,
        "usage_of_diagonal_vectors" : 0,
        "concecutive_diagonals" : False
    }
    escape_path.append(s) # do it so that we do not go somewhere and then go through our starting point again without poping
    traverse(x, y, movement_vectors, state, escape_path, maze)
    return escape_path if len(escape_path) != 1 else [] # if len = 1 then each recursive calls popped their path leaving only the beginning.

def find_s(maze):
    i = 0
    j = 0
    for row in maze:
        for column in row:
            if column == 'S':
                return j, i
            j+=1
        j = 0
        i+=1


def traverse(x, y, movement_vectors, state, escape_path, maze):
    if maze[y][x] == 'E': # base case, if in any call we get to E then we are done found[0] = True means we are not going to iterate no more movement_vectors and we are not going to pop anything and just return None in each recursive call in our stack
        state["found"] = True
        return

    for vector in movement_vectors:
        if not state["found"]:
            ok = False # if our movement is okay to perform if not then we will check the next movement
            next_x_pos = x + vector[0] # create new variables since changing x and y is not convenient and leads to issues
            next_y_pos = y + vector[1]
            # we will not have issues with Outofindex error as python does not check other statements when one of those before them gets False
            if (0 <= next_x_pos < len(maze[0])) and (0 <= next_y_pos < len(maze)) and (maze[next_y_pos][next_x_pos] != '#') and ((next_x_pos, next_y_pos) not in escape_path):
                ok = True # our conditions are: x between 0 and the length of rows (considering that all rows have the same length), y between 0 and the heighth of our maze, the next point is not a wall, the next point has not been visited during the current path traverse

            if ok:
                prev_count = state["usage_of_diagonal_vectors"] # here we will save our previous state so that this recursive calls do not mess up with the previous state and we can restore it in case if we return from the stack
                prev_concecutive = state["concecutive_diagonals"]

                try:
                    movement_vectors.index(vector, 4, 8)  # if not one of diagonal movements will throw ValueError
                                                        # else will check if the count of used diagonal vectors is 3 or the previous recursive call used diagonal -> will skip the diagonal movement
                    if (state["usage_of_diagonal_vectors"] == 3) or (state["concecutive_diagonals"]):
                        continue
                    state["usage_of_diagonal_vectors"] += 1
                    state["concecutive_diagonals"] = True
                except ValueError:
                    state["concecutive_diagonals"] = False
                    pass

                escape_path.append((next_x_pos, next_y_pos))
                traverse(next_x_pos, next_y_pos, movement_vectors, state, escape_path, maze)
                if not state["found"]:
                    escape_path.pop()
                    state["usage_of_diagonal_vectors"] = prev_count # here we get back to previous call's state
                    state["concecutive_diagonals"] = prev_concecutive

maze_sample = [
    ['#', '#', '#', '.', '#'],
    ['#', 'S', '.', '.', '#'],
    ['#', '#', '.', '#', '.'],
    ['#', '.', '.', '.', 'E'],
    ['#', '#', '#', '#', '#']
]

print(escape_maze(maze_sample))