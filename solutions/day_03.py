with open("test_inputs/day_03.txt", "r") as file:

    input_data = [line.strip("\n") for line in file.readlines()]
    
print(input_data)

# part 1

current_sum = 0
idx = 0
# # ------------------------------------------
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
    counter = 0
    indices = []
    idx = 0
    found_idx = main_string.find(substring, idx)
    
    while found_idx != -1 and counter < 100:
        
        indices.append(found_idx)
        idx = found_idx + len(substring)
        found_idx = main_string.find(substring, idx)
        
        if idx >= len(main_string):
            break
        
        counter += 1
    
    return indices

input_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
print(find_string_in_string("mul", input_str))