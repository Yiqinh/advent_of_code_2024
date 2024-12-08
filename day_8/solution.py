from collections import defaultdict

def solution_1(grid):
    m = len(grid)
    n = len(grid[0])
    res = set()

    freqs = defaultdict(set)
    for i in range(m):
        for j in range(n):
            symbol = grid[i][j]
            if symbol != ".":
                freqs[symbol].add((i, j))
    
    
    for symbol, coords in freqs.items():
        for coord_1 in coords:
            for coord_2 in coords:
                if coord_1 == coord_2:
                    continue
                    
                slope = (coord_2[0] - coord_1[0], coord_2[1] - coord_1[1])
                oppo = (coord_1[0] - slope[0], coord_1[1] - slope[1])
                other = (coord_2[0] + slope[0], coord_2[1] + slope[1])

                for anti in oppo, other:
                    if anti[0] in range(m) and anti[1] in range(n):
                        res.add(anti)
    
    return len(res)

def solution_2(grid):
    m = len(grid)
    n = len(grid[0])
    res = set()

    freqs = defaultdict(set)
    for i in range(m):
        for j in range(n):
            symbol = grid[i][j]
            if symbol != ".":
                freqs[symbol].add((i, j))
    
    
    for symbol, coords in freqs.items():
        for coord_1 in coords:
            for coord_2 in coords:
                if coord_1 == coord_2:
                    continue
                    
                slope = (coord_2[0] - coord_1[0], coord_2[1] - coord_1[1])

                index = 0
                while True:
                    oppo = (coord_1[0] - slope[0] * index, coord_1[1] - slope[1] * index)
                    if oppo[0] in range(m) and oppo[1] in range(n):
                        res.add(oppo)
                        index += 1
                    else:
                        break

                index = 0
                while True:
                    other = (coord_2[0] + slope[0] * index, coord_2[1] + slope[1] * index)
                    if other[0] in range(m) and other[1] in range(n):
                        res.add(other)
                        index += 1
                    else:
                        break
    
    return len(res)

if __name__ == "__main__":
    grid = []
    with open('day_8_input.txt', 'r') as file:
        for line in file:
            line = list(line.strip())
            grid.append(line)
    
    res_1 = solution_1(grid)
    print("Solution 1: ", res_1)

    res_2 = solution_2(grid)
    print("Solution 2: ", res_2)