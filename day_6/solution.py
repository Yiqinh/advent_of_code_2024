def path_find(grid):
    visited = set()
    start = None
    direction = None

    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == ">":
                direction = (0, 1) # right
                start = (i, j)
            if grid[i][j] == "v":
                direction = (1, 0) # down
                start = (i, j)
            if grid[i][j] == '^':
                direction = (-1, 0) # up
                start = (i, j)
            if grid[i][j] == "<":
                direction = (0, -1) # left
                start = (i, j)

    while True:
        visited.add(start)

        next_i, next_j = start[0] + direction[0], start[1] + direction[1]
        if next_i not in range(m) or next_j not in range(n):
            break

        if grid[next_i][next_j] != "#":
            start = (next_i, next_j)
        else:
            if direction == (0, 1): # currently going right
                direction = (1, 0)
            elif direction == (1, 0): # currently going down
                direction = (0, -1)
            elif direction == (0, -1): # currently going left
                direction = (-1, 0)
            elif direction == (-1, 0): # currently going up
                direction = (0, 1)
            
    return len(visited)

def is_loop(grid):
    visited = set()
    start = None
    direction = None

    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == ">":
                direction = (0, 1) # right
                start = (i, j)
            if grid[i][j] == "v":
                direction = (1, 0) # down
                start = (i, j)
            if grid[i][j] == '^':
                direction = (-1, 0) # up
                start = (i, j)
            if grid[i][j] == "<":
                direction = (0, -1) # left
                start = (i, j)

    while True:
        if ((start), (direction)) in visited:
            return True
        else:
            visited.add(((start), (direction)))

        next_i, next_j = start[0] + direction[0], start[1] + direction[1]
        if next_i not in range(m) or next_j not in range(n):
            break

        if grid[next_i][next_j] != "#":
            start = (next_i, next_j)
        else:
            if direction == (0, 1): # currently going right
                direction = (1, 0)
            elif direction == (1, 0): # currently going down
                direction = (0, -1)
            elif direction == (0, -1): # currently going left
                direction = (-1, 0)
            elif direction == (-1, 0): # currently going up
                direction = (0, 1)
            
    return False

def part_2(grid):
    counter = 0
    m = len(grid)
    n = len(grid[0])

    starts = [">", "<", "^", "v"]
    for i in range(m):
        for j in range(n):
            if grid[i][j] != "#" and grid[i][j] not in starts:
                before = grid[i][j]
                grid[i][j] = "#"
                if is_loop(grid):
                    counter += 1
                grid[i][j] = before
    
    return counter

if __name__ == "__main__":
    
    grid = []
    with open('day_6_input.txt', 'r') as file:
        for line in file:
            line = list(line.strip())
            grid.append(line)

    res_1 = path_find(grid)
    print('Solution 1: ', res_1)
    res_2 = part_2(grid)
    print('Solution 2: ', res_2)
