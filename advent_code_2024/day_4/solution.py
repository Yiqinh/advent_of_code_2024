def solution_1(grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    m = len(grid)
    n = len(grid[0])
    target = 'XMAS'

    res = 0

    for i in range(m):
        for j in range(n):
            for d_i, d_j in directions:
                cur_coord = [i, j]
                for k in range(4):
                    if cur_coord[0] not in range(0, m) or cur_coord[1] not in range(0, n):
                        break
                    if grid[cur_coord[0]][cur_coord[1]] != target[k]:
                        break
                    if k == 3:
                        res += 1

                    cur_coord = [cur_coord[0] + d_i, cur_coord[1] + d_j]
    
    return res

def solution_2(grid):
    direction_1 = [(1, 1), (0, 0), (-1, -1)]
    direction_2 = [(-1, -1), (0, 0), (1, 1)]
    
    direction_3 = [(1, -1), (0, 0), (-1, 1)]
    direction_4 = [(-1, 1), (0, 0), (1, -1)]

    cross_1 = [direction_1, direction_2]
    cross_2 = [direction_3, direction_4]

    m = len(grid)
    n = len(grid[0])

    target = 'MAS'
    res = 0

    for i in range(m):
        for j in range(n):
            passes = False
            for x in range(2):
                for y in range(2):
                    path_1 = cross_1[x]
                    path_2 = cross_2[y]
                    cur_check = True
                    for path in [path_1, path_2]:
                        for k, (d_i, d_j) in enumerate(path):
                            cur_coord = [i + d_i, j + d_j]
                            if cur_coord[0] not in range(0, m) or cur_coord[1] not in range(0, n):
                                cur_check = False
                                break
                            if grid[cur_coord[0]][cur_coord[1]] != target[k]:
                                cur_check = False
                                break
                    passes = passes or cur_check
            if passes == True:
                res += 1
        
    return res


if __name__ == "__main__":

    with open('input.txt', 'r') as file:
        grid = [list(line.strip()) for line in file]


    res = solution_1(grid)
    print("Solution 1: ", res)

    res = solution_2(grid)
    print("Solution 2: ", res)

