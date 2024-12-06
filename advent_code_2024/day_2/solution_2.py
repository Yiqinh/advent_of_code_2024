def check_mostly_trend(lst):    
    increasing = 0
    decreasing = 0
    
    # Count increasing and decreasing intervals
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            increasing += 1
        elif lst[i] < lst[i - 1]:
            decreasing += 1
        
    # Determine the trend
    if increasing > decreasing:
        return "increase"
    elif decreasing > increasing:
        return "decrease"

if __name__ == "__main__":
    levels = []
    with open('day_2_input.txt') as file:
        for line in file:
            reports = [int(num) for num in line.split()]
            levels.append(reports)
    #part 1
    unsafe_counter = 0
    for level in levels:
        if level[1] > level[0]:
            trend = 'increase'
            last_num = level[0] - 1
        else:
            trend = 'decrease'
            last_num = level[0] + 1
        
        for num in level:
            diff = num - last_num
            if trend == 'increase' and diff not in range(1, 4):
                unsafe_counter += 1
                break
            elif trend == 'decrease' and diff not in range(-3, 0):
                unsafe_counter += 1
                break
            last_num = num
    
    safe_counter = len(levels) - unsafe_counter
    print("Solution 1: ", safe_counter)

    # part 2
    def is_valid_trend(level):
        
        # Determine the trend
        trend = 'increase' if level[1] - level[0] > 0 else 'decrease'
        
        # Check the trend
        for i in range(1, len(level)):
            diff = level[i] - level[i - 1]
            if trend == 'increase' and diff not in range(1, 4):
                return False
            elif trend == 'decrease' and diff not in range(-3, 0):
                return False
        return True
    
    safe_counter = 0

    for level in levels:
        len_level = len(level)
        
        # Check if the original list is valid
        if is_valid_trend(level):
            safe_counter += 1
            continue
        
        # Check all possible one-element-removed lists
        for i in range(len_level):
            mod_level = level[:i] + level[i + 1:]
            if is_valid_trend(mod_level):
                safe_counter += 1
                break  # No need to check further modifications for this list
                
    
    print("Solution 2: ", safe_counter)

