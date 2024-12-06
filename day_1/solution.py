import numpy as np
from collections import Counter

if __name__ == "__main__":

    group_1 = []
    group_2 = []

    with open('location_id.txt') as file:
        for line in file:
            one, two = map(int, line.split())
            group_1.append(one)
            group_2.append(two)

    # part 1
    group_1.sort()
    group_2.sort()
    n = len(group_1)

    diffs = []
    for i in range(n):
        abs_diff = abs(group_1[i] - group_2[i])
        diffs.append(abs_diff)
    
    res_1 = sum(diffs)

    # part 2
    right_counter = Counter(group_2)
    right_counter = dict(right_counter)

    sim_score = []
    for i in range(n):
        left_num = group_1[i]
        score = left_num * right_counter.get(left_num, 0)
        sim_score.append(score)
    
    res_2 = sum(sim_score)
    
    with open('solution.txt', 'w') as file:
        file.write('part_1: \n')
        file.write(str(res_1))
        file.write('\n')
        file.write('part_2: \n')
        file.write(str(res_2))
