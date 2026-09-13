### Intuition

What I initially thought for solving this problem is that we can do recursive calls to traverse 
the maze, trying every possible direction from each cell as we work with stack it would be possible to just remove the last action go back and try something else with the previous action (recursive call). At each step,
we attempt all 8 movement vectors and recurse into valid ones. If the last recursive call cannot go anywhere then it stops and the previous recursive call
pops the last position from escape_path and restores
the diagonal state to what it was before that move. In this way we will  check every possible direction through every possible path
until we either find the path and give 'found' state True or we do not find anything and all recursive calls just pop all paths and kill themselves.

### Algorithm work
1. **Finding the start**: `find_s()` scans the maze returns (x, y) coordinates of 'S'.

2. **State tracking**: A `state` dictionary is passed through every recursive
   call, holding three things:
   - `found`: whether we've reached 'E', when it gets True, calls cannot modify 
   `escape_path` anymore because of the condition before it and cannot check no more moves because of the condition right in the beginning of the loop for moves
   - `usage_of_diagonal_vectors`: how many diagonal moves have been used so far on
     this path (max 3 allowed)
   - `consecutive_diagonals`: whether the previous move was diagonal (two in a row
     are not allowd)

3. **At each cell**, we iterate over all 8 movement vectors and for each we check:
   - The next position is within bounds
   - It is not a wall ('#')
   - It has not already been visited in the current path (through `not in escape_path`)
   - If the move is diagonal: the diagonal count is below 3 AND the last move was not diagonal

4. **Diagonal check** is done with `movement_vectors.index(vector, 4, 8)` the
   diagonal vectors are in indices 4-7 in our list, so if the vector is found there
   it is diagonal, otherwise `index()` raises `ValueError` which we catch.

5. **Going back through a stack**: if a recursive call returns without setting `found = True`, we:
   - `pop()` the last position from `escape_path`
   - restore `usage_of_diagonal_vectors` and `consecutive_diagonals` to their values
     before that move was made (saved in `prev_count` and `prev_consecutive`)

6. **No path found**: if `escape_path`
   ends up with only the starting cell then if
   `len(escape_path) == 1` return `[]`.


### Time Complexity

So we must think of the worst case scenario.

Take `n` as the number of cells in our grid. So find_s takes `O(n)` to find S.

After this we create `n` possible recursive calls each iterating over 8 possible movements. In total `n` cells so `O(8^n)` in case if we traverse through each cell by each possible movement.

And everytime in each cell we make a call to `escape_path` which takes `O(n)`. So traverse takes `O(n8^n)` (`O(n8^n + n)` with find_s but we can omit find_s as it is too small).

Overall time complexity is `O(n8^n)`

### Space Complexity

In worst case we store `n` recursive calls in our stack and our `escape_path` stores up to `n` coordinates. So overall `O(n)` space complexity.