def dfs(i, cur_total, operands, goal):
    if i == len(operands):
        return cur_total == goal
    
    res = (dfs(i + 1, cur_total + operands[i], operands, goal)
           or dfs(i + 1, cur_total * operands[i], operands, goal)
    )

    return res

def solution_1(totals, operands):
    n = len(totals)
    res = 0

    for i in range(n):
        goal = totals[i]
        cur_operands = operands[i]

        can_make = dfs(0, 0, cur_operands, goal)
        if can_make:
            res += goal
        
    return res

def dfs_2(i, cur_total, operands, goal, lst=[]):
    if i == len(operands):
        # print(lst)
        # print(cur_total)
        return cur_total == goal
    

    res = (dfs_2(i + 1, cur_total + operands[i], operands, goal)
           or dfs_2(i + 1, cur_total * operands[i], operands, goal)
           or dfs_2(i + 1, int(str(cur_total) + str(operands[i])), operands, goal)

        )

    return res

def solution_2(totals, operands):
    n = len(totals)
    res = 0

    for i in range(n):
        goal = totals[i]
        cur_operands = operands[i]

        can_make = dfs_2(0, 0, cur_operands, goal)
        if can_make:
            res += goal

    return res


if __name__ == "__main__":
    totals = []
    operands = []

    with open('day_7_input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            total, right = line.split(":")
            right = right.strip()
            right = list(map(int, right.split()))
            total = int(total)

            totals.append(total)
            operands.append(right)
    
    res_1 = solution_1(totals, operands)
    print("Solution 1: ", res_1)

    res_2 = solution_2(totals, operands)
    print("Soluton 2: ", res_2)