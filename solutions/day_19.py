debug_mode = False
testing = False

if testing:
    
    with open("test_inputs/day_19.txt", "r") as file:

        input_data = [line.strip("\n") for line in file.readlines()]
        break_idx = input_data.index("")

        patterns = input_data[:break_idx]
        designs = input_data[break_idx+1:]

else:
    
    with open("real_inputs/day_19.txt", "r") as file:

        input_data = [line.strip("\n") for line in file.readlines()]
        break_idx = input_data.index("")

        patterns = input_data[:break_idx]
        designs = input_data[break_idx+1:]

patterns = [pattern.strip() for pattern in patterns[0].split(',')]
  
# print(patterns)
# print(designs)

# from day 3

def find_string_in_string(substring, main_string):
    indices = []
    idx = 0
    found_idx = main_string.find(substring, idx)
    
    while found_idx != -1:
        
        indices.append(found_idx)
        idx = found_idx + len(substring)
        found_idx = main_string.find(substring, idx)
        
        if idx >= len(main_string):
            break
    
    return indices

# part 1
possible_count = 0

for design in designs:
    
    idx_list = []
    
    for pattern in patterns:
        
        indices_to_check = find_string_in_string(pattern, design)
        if debug_mode:
            print(f"{pattern} in {design}... indices to check: {indices_to_check}")
        
        for idx in indices_to_check:
            idx_list.extend([idx+i for i in range(len(pattern))])
    
    if debug_mode:
        print(idx_list)
    unique_idx_list = set(idx_list)
    
    if len(unique_idx_list) != len(design):
        if debug_mode:
            print(f'design: {design} is impossible!')
            print(unique_idx_list)
    else:
        possible_count += 1

print(possible_count)