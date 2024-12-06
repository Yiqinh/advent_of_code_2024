import re

def parse_and_multiply(corrupted_memory):
    pattern = r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'
    
    matches = re.findall(pattern, corrupted_memory)
    
    total = 0
    for match in matches:
        x, y = map(int, match)
        total += x * y
    
    return total

def parse_and_multiply_with_rules(corrupted_memory):

    mul_pattern = r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'
    instructions = re.findall(r'mul\(\s*\d{1,3}\s*,\s*\d{1,3}\s*\)|do\(\)|don\'t\(\)', corrupted_memory)
    
    is_enabled = True 
    total = 0
    
    for instruction in instructions:
        if instruction == "do()":
            is_enabled = True
        elif instruction == "don't()":
            is_enabled = False
        else:
            match = re.match(mul_pattern, instruction)
            if match and is_enabled:
                x, y = map(int, match.groups())
                total += x * y
    
    return total

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        corrupted_memory = file.read()

    # part 1
    res = parse_and_multiply(corrupted_memory)
    print(res)

    res = parse_and_multiply_with_rules(corrupted_memory)
    print(res)
    # part 2