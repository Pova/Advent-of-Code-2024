import itertools

debug_mode = False

with open('real_inputs/day_09.txt') as file:
    
    input = file.read().strip()

input = [int(char) for char in input]

# --------------------------------------
odd_input = input[::2]
even_input = input[1::2]

print(odd_input)
print(even_input)

# print('input:')       
# print(input)
# print('\nSum of file blocks')
# print(sum(odd_input))
# print('\nSum of free space blocks')
# print(sum(even_input))
# --------------------------------------

# --------------------------------------
key_str_list = []

for i, id in enumerate(odd_input):
    for _ in range(id):
        key_str_list.append(str(i))

reversed_key_str_list = key_str_list[::-1]

# print(key_str)
# print(key_str[::-1])
# --------------------------------------


# --------------------------------------
individual_blocks = []
j = 0
for i, id in enumerate(odd_input):
    for _ in range(id):
        individual_blocks.append(str(i))
    if i < len(even_input):
        for _ in range(even_input[i]):
            individual_blocks.append(reversed_key_str_list[j])
            j += 1
            
# print(''.join(individual_blocks))

individual_blocks = individual_blocks[:sum(odd_input)]
individual_blocks = [int(num) for num in individual_blocks]
# print(individual_blocks)

def checksum(number_list):
    
    checksum = 0
    
    for i, num in enumerate(number_list):
        
        checksum += i * num
        
    return checksum
        
print(checksum(individual_blocks))

# Part 2

def check_spaces(individual_blocks):
    
    i = 0
    output_list = []
    
    while i < len(individual_blocks):
        
        if individual_blocks[i] == []:
            i += 1
            continue
        
        if set(individual_blocks[i]) != {'.'}:
            output_list.append(individual_blocks[i])
            i += 1
            
        else:
            total_lengths = len(individual_blocks[i])
            j = i+1
            
            while j < len(individual_blocks) and set(individual_blocks[j]) == {'.'}:
                total_lengths += len(individual_blocks[j])
                j += 1
                
            output_list.append(['.']*total_lengths)
            i = j
            
    return output_list

blocks_to_move = [] # holds the movable blocks
individual_blocks = []
j = 0
for i, id in enumerate(odd_input):
    individual_blocks.append([str(i),]*id)
    blocks_to_move.append([str(i),]*id)
    if i < len(even_input):
        individual_blocks.append(['.']*even_input[i])
            
print(individual_blocks)

# for idx, list in enumerate(individual_blocks[::2][::-1]):
#     print(list)

blocks_to_move = blocks_to_move[::-1]
print(blocks_to_move)

print()

for i, block_to_move in enumerate(blocks_to_move):
    
    block_to_move_len = len(block_to_move)
    
    individual_blocks[individual_blocks.index(block_to_move)] = ['.']*block_to_move_len
    
    for j, block in enumerate(individual_blocks):
        
        
        if block == []:
            continue
        
        if debug_mode:
            print(f'trying to move: {block_to_move} to {block}')
        
        if set(block) == {'.'}:
            if debug_mode:
                print('found space')
            
            if len(block) < block_to_move_len:
                if debug_mode:
                    print('not enough space to move')
                continue
            else:
                if debug_mode:
                    print('enough space to move')
                    
                # individual_blocks.remove(block_to_move)
                # individual_blocks[individual_blocks.index(block_to_move)] = ['.']*block_to_move_len
                
                individual_blocks[j] = block_to_move
                individual_blocks.insert(j+1, ['.']*(len(block)-block_to_move_len))
                
                if debug_mode:
                    print(individual_blocks)
                break
        else:
            if debug_mode:
                print('not space')
            continue
        
    individual_blocks = check_spaces(individual_blocks)
    # print(individual_blocks)

individual_blocks = [block for block in individual_blocks if block != []]

# print('FINAL RESULT')
# print('-'*20)
# print("".join(list(itertools.chain(*individual_blocks))))
# print('-'*20)

def checksum_part2(number_list):
    
    checksum = 0
    
    for i, num in enumerate(number_list):
        
        if num == '.':
            continue
        
        checksum += i * int(num)
        
    return checksum

print(checksum_part2(list(itertools.chain(*individual_blocks))))