with open("real_inputs/day_03.txt", "r") as file:

    input_data = [line.strip("\n") for line in file.readlines()]
    
# print(f"input_data: {input_data}")
print(f"lines of input data: {len(input_data)}")
print('-'*30)

total_input_data = ''.join(input_data)

# part 1

# # ------------------------------------------
# current_sum = 0
# idx = 0
# check if current char is 'm' 
    # if not: increment idx (by 1)
    # if so:
        # check if the next 3 chars are 'mul'
            # if not: increment idx (by 1)
            # if so: 
                # check for (
                    # if so 
                    # xxx,xxx)
# # ------------------------------------------

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


total_sum = 0
indices_to_check = find_string_in_string("mul", total_input_data)

print_rejection = False
print_acceptance = False

for idx in indices_to_check:
    
    # print(f'checking idx: {idx}')
    
    current_idx = idx + 3
    
    if total_input_data[current_idx] != '(':
        if print_rejection:
            print(f'rejecting: {total_input_data[idx:current_idx+1]}')
        continue
    
    current_idx += 1
    # ----------------------------------------
    first_num_len, first_num_left_idx = 0, current_idx
    while total_input_data[current_idx].isnumeric():
        current_idx += 1
        first_num_len += 1
        
    if first_num_len > 3 or first_num_len == 0:
        if print_rejection:
            print(f'rejecting: {total_input_data[idx:current_idx+1]}')
        continue
    else:
        first_num = int(total_input_data[first_num_left_idx:current_idx])
    # ----------------------------------------
    
    if total_input_data[current_idx] != ',':
        if print_rejection:
            print(f'rejecting: {total_input_data[idx:current_idx+1]}')
        continue
    
    current_idx += 1
    
    second_num_len, second_num_left_idx = 0, current_idx
    while total_input_data[current_idx].isnumeric():
        current_idx += 1
        second_num_len += 1
    
    if second_num_len > 3 or second_num_len == 0:
        if print_rejection:
            print(f'rejecting: {total_input_data[idx:current_idx+1]}')
        continue
    else:
        second_num = int(total_input_data[second_num_left_idx:current_idx])
        
    if total_input_data[current_idx] != ')':
        if print_rejection:
            print(f'rejecting: {total_input_data[idx:current_idx+1]}')
        continue
    
    if print_acceptance:
        print(f'got a valid command starting at: {idx}: {total_input_data[idx:current_idx+1]}')
    total_sum += first_num*second_num
        
print(f'total = {total_sum}')

# 23465714 (incorrect - too low)
# 145501706 (incorrect - too low)
# 23465714 (counter while limit bug)
# 178794710

# Part 2 

do_breakpoints = [0] + find_string_in_string("do()", total_input_data)
dont_breakpoints = find_string_in_string("don't()", total_input_data)

do_breakpoints = [idx+4 for idx in do_breakpoints]
dont_breakpoints = [idx+7 for idx in dont_breakpoints]

# print(total_input_data)
# print(do_breakpoints)
# print(dont_breakpoints)

def check_mul_is_active(idx):
    
    best_do_idx = None
    best_dont_idx = None
    
    for do_idx in do_breakpoints:
        if do_idx <= idx:
            best_do_idx = do_idx
        else:
            break
        
    for dont_idx in dont_breakpoints:
        if dont_idx <= idx:
            best_dont_idx = dont_idx
        else:
            break
    
    if best_dont_idx is None:
        return True
    elif best_do_idx > best_dont_idx:
        return True
    else:
        return False

indices_to_check = find_string_in_string("mul", total_input_data) # wasteful dont need to run this again

total_sum = 0

print_rejection = False
print_acceptance = False

for idx in indices_to_check:
    
    # print(f'checking idx: {idx}')
    
    current_idx = idx + 3
    
    if total_input_data[current_idx] != '(':
        if print_rejection:
            print(f'rejecting: {total_input_data[idx:current_idx+1]}')
        continue
    
    current_idx += 1
    # ----------------------------------------
    first_num_len, first_num_left_idx = 0, current_idx
    while total_input_data[current_idx].isnumeric():
        current_idx += 1
        first_num_len += 1
        
    if first_num_len > 3 or first_num_len == 0:
        if print_rejection:
            print(f'rejecting: {total_input_data[idx:current_idx+1]}')
        continue
    else:
        first_num = int(total_input_data[first_num_left_idx:current_idx])
    # ----------------------------------------
    
    if total_input_data[current_idx] != ',':
        if print_rejection:
            print(f'rejecting: {total_input_data[idx:current_idx+1]}')
        continue
    
    current_idx += 1
    
    second_num_len, second_num_left_idx = 0, current_idx
    while total_input_data[current_idx].isnumeric():
        current_idx += 1
        second_num_len += 1
    
    if second_num_len > 3 or second_num_len == 0:
        if print_rejection:
            print(f'rejecting: {total_input_data[idx:current_idx+1]}')
        continue
    else:
        second_num = int(total_input_data[second_num_left_idx:current_idx])
        
    if total_input_data[current_idx] != ')':
        if print_rejection:
            print(f'rejecting: {total_input_data[idx:current_idx+1]}')
        continue
    
    if print_acceptance:
        print(f'got a valid command starting at: {idx}: {total_input_data[idx:current_idx+1]}')
    
    mul_is_active = check_mul_is_active(idx)
    if mul_is_active:
        total_sum += first_num*second_num
        
print(f'total = {total_sum}')