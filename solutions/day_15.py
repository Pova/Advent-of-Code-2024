testing = True
debug_mode = False

if testing:
    
    with open("test_inputs/day_15_b.txt", "r") as file:

        input_data = [line.strip("\n") for line in file.readlines()]
        break_idx = input_data.index("")

        warehouse_lines = input_data[:break_idx]
        lines_of_movements = input_data[break_idx+1:]
        movements = []
        for line in lines_of_movements:
            movements.extend(line)
else:
    
    with open("real_inputs/day_15.txt", "r") as file:

        input_data = [line.strip("\n") for line in file.readlines()]
        break_idx = input_data.index("")

        warehouse_lines = input_data[:break_idx]
        lines_of_movements = input_data[break_idx+1:]
        movements = []
        for line in lines_of_movements:
            movements.extend(line)

height = len(warehouse_lines)
width = len(warehouse_lines[0])

warehouse = {}

for j, line in enumerate(warehouse_lines):
    for i, char in enumerate(line):
        warehouse[(i,j)] = char
        if char == '@':
            initial_position = (i,j)
            
original_warehouse = warehouse.copy() # we will change warehouse so need to save this for part 2

def find_new_position(current_position, direction):
    
    '''
    direction options: < > ^ v
    '''
    
    if direction == '<':
        return (current_position[0]-1,current_position[1])
    elif direction == '>':
        return (current_position[0]+1,current_position[1])
    if direction == '^':
        return (current_position[0],current_position[1]-1)
    elif direction == 'v':
        return (current_position[0],current_position[1]+1)
    else:
        print('unrecognized direction')
        return None
    
def print_warehouse(warehouse):
    
    print_width = max([key[0] for key, value in warehouse.items()])+1
    print_height = max([key[1] for key, value in warehouse.items()])+1
    
    display_str = '\n'
    
    for j in range(print_height):
        new_line = ''
        for i in range(print_width):
            new_line += str(warehouse[(i,j)])
        new_line += '\n'
        display_str += new_line

    print(display_str)
 
def check_for_space(position, direction, warehouse, print_out=False):
    
    # position: location of box that must be moved.
    
    if direction == '^':
        positions = [(position[0],position[1]-i) for i in range(position[1]+1)]
        char_list = [warehouse[position] for position in positions if position in warehouse]
        char_set = set(char_list)
        if '.' in char_set:
            if char_list.index('.') < char_list.index('#'):
                end_idx = char_list.index('.')
                positions_to_update = positions[:end_idx+1]
            else:
                positions_to_update = None
        else:
            positions_to_update = None
    elif direction == 'v':
        positions = [(position[0],position[1]+i) for i in range(height-position[1])]
        char_list = [warehouse[position] for position in positions if position in warehouse]
        char_set = set(char_list)
        if '.' in char_set:
            if char_list.index('.') < char_list.index('#'):
                end_idx = char_list.index('.')
                positions_to_update = positions[:end_idx+1]
            else:
                positions_to_update = None
        else:
            positions_to_update = None
    if direction == '<':
        positions = [(position[0]-i,position[1]) for i in range(position[0]+1)]
        char_list = [warehouse[position] for position in positions if position in warehouse]
        char_set = set(char_list)
        if '.' in char_set:
            if char_list.index('.') < char_list.index('#'):
                end_idx = char_list.index('.')
                positions_to_update = positions[:end_idx+1]
            else:
                positions_to_update = None
        else:
            positions_to_update = None
    elif direction == '>':
        positions = [(position[0]+i,position[1]) for i in range(width-position[0])]
        char_list = [warehouse[position] for position in positions if position in warehouse]
        char_set = set(char_list)
        if '.' in char_set:
            if char_list.index('.') < char_list.index('#'):
                end_idx = char_list.index('.')
                positions_to_update = positions[:end_idx+1]
            else:
                positions_to_update = None
        else:
            positions_to_update = None
    
    if print_out:
        print(f'positions to update: {positions_to_update}')
        
    return positions_to_update
    
    
def move_boxes(current_position, positions_to_update, warehouse):
    
    # current_position: location of robot
    # positions_to_update: locations of boxes in the way (ending with empty space)
    
    warehouse[current_position] = '.'
    warehouse[positions_to_update[0]] = '@'
    for position in positions_to_update[1:]:
        warehouse[position] = 'O'
        
    return warehouse
    

print('ORIGINAL')
    
print_warehouse(warehouse)

current_position = initial_position

for move in movements:
    
    new_position = find_new_position(current_position, move)
    
    if debug_mode:
        print(f'with the move: {move} robot wants to move from {current_position} to {new_position}')
    
    # case 1 - nothing in the way
    
    if warehouse[new_position] == '.':
        if debug_mode:
            print(f'nothing in the way, robot moving: {current_position} --> {new_position}')
        
        # update warehouse
        
        warehouse[current_position] = '.'
        warehouse[new_position] = '@'
        
        if debug_mode:
            print_warehouse(warehouse)
        
        # update position
        current_position = new_position
            
    elif warehouse[new_position] == '#':
        if debug_mode:
            print(f'hit a wall, robot stays at {current_position}')
                        
    elif warehouse[new_position] == 'O':
        if debug_mode:
            print(f'hit a box, robot to move boxes moving: {current_position} --> {new_position}')
        
        positions_to_update = check_for_space(new_position, move, warehouse, print_out=False)
        
        if positions_to_update is None:    
            # case : no space to move boxes
            if debug_mode:
                print('case: no space to move boxes!')
            
        else:
            # case: space to move boxes
            if debug_mode:
                print('case: space to move boxes')
            
            warehouse = move_boxes(current_position, positions_to_update, warehouse)
            
            if debug_mode:
                print('after update')
                print_warehouse(warehouse)
            
            # update position
            current_position = new_position
        
    else:
        print(f'unexpected input: {warehouse[new_position]}')
        break
    
    if debug_mode:
        print()

print('FINAL')
print_warehouse(warehouse)

total_gps = 0

for key,value in warehouse.items():
    if value == 'O':
        total_gps += key[0]+key[1]*100

# print(f'Final robot position: {current_position}')
print(f'Sum of GPS coordinates: {total_gps}')

# Part 2

print('='*10)

"""

step 1 - create a new widened warehouse map
step 2 - adjust logic for moving boxes:
    moving is different now when moving boxes up/down
    identification of boxes is different now as well

"""

new_warehouse = {}

for key, value in original_warehouse.items():
    
    if value == '#':
        new_warehouse[(2*key[0],key[1])] = '#'
        new_warehouse[(2*key[0]+1,key[1])] = '#'
    elif value == 'O':
        new_warehouse[(2*key[0],key[1])] = '['
        new_warehouse[(2*key[0]+1,key[1])] = ']'
    elif value == '.':
        new_warehouse[(2*key[0],key[1])] = '.'
        new_warehouse[(2*key[0]+1,key[1])] = '.'
    elif value == '@':
        new_warehouse[(2*key[0],key[1])] = '@'
        new_warehouse[(2*key[0]+1,key[1])] = '.'
    else:
        print('unknown symbol!')
        break

print('PART 2 ORIGINAL')
print_warehouse(new_warehouse)

# # ----------------------------------------------------
# total_gps = 0

# for key,value in warehouse.items():
#     if value == 'O':
#         total_gps += key[0]+key[1]*100

# # print(f'Final robot position: {current_position}')
# print(f'Sum of GPS coordinates: {total_gps}')
# # ----------------------------------------------------

def check_for_space_part_2(position, direction, warehouse, print_out=False):
    
    # position: location of box that must be moved.
    
    if direction == '^':
        positions = [(position[0],position[1]-i) for i in range(position[1]+1)]
        char_list = [warehouse[position] for position in positions if position in warehouse]
        char_set = set(char_list)
        if '.' in char_set:
            if char_list.index('.') < char_list.index('#'):
                end_idx = char_list.index('.')
                positions_to_update = positions[:end_idx+1]
            else:
                positions_to_update = None
        else:
            positions_to_update = None
    elif direction == 'v':
        positions = [(position[0],position[1]+i) for i in range(height-position[1])]
        char_list = [warehouse[position] for position in positions if position in warehouse]
        char_set = set(char_list)
        if '.' in char_set:
            if char_list.index('.') < char_list.index('#'):
                end_idx = char_list.index('.')
                positions_to_update = positions[:end_idx+1]
            else:
                positions_to_update = None
        else:
            positions_to_update = None
    if direction == '<':
        positions = [(position[0]-i,position[1]) for i in range(position[0]+1)]
        char_list = [warehouse[position] for position in positions if position in warehouse]
        char_set = set(char_list)
        if '.' in char_set:
            if char_list.index('.') < char_list.index('#'):
                end_idx = char_list.index('.')
                positions_to_update = positions[:end_idx+1]
            else:
                positions_to_update = None
        else:
            positions_to_update = None
    elif direction == '>':
        positions = [(position[0]+i,position[1]) for i in range(width-position[0])]
        char_list = [warehouse[position] for position in positions if position in warehouse]
        char_set = set(char_list)
        if '.' in char_set:
            if char_list.index('.') < char_list.index('#'):
                end_idx = char_list.index('.')
                positions_to_update = positions[:end_idx+1]
            else:
                positions_to_update = None
        else:
            positions_to_update = None
    
    if print_out:
        print(f'positions to update: {positions_to_update}')
        
    return positions_to_update
    
    
def move_boxes_part_2(current_position, positions_to_update, warehouse):
    
    # current_position: location of robot
    # positions_to_update: locations of boxes in the way (ending with empty space)
    
    warehouse[current_position] = '.'
    warehouse[positions_to_update[0]] = '@'
    for position in positions_to_update[1:]:
        warehouse[position] = 'O'
        
    return warehouse

current_position = (initial_position[0]*2, initial_position[1])
print(new_warehouse[current_position])

for move in movements:
    
    pass
    
    # new_position = find_new_position(current_position, move)
    
    # if debug_mode:
    #     print(f'with the move: {move} robot wants to move from {current_position} to {new_position}')
    
    # # case 1 - nothing in the way
    
    # if warehouse[new_position] == '.':
    #     if debug_mode:
    #         print(f'nothing in the way, robot moving: {current_position} --> {new_position}')
        
    #     # update warehouse
        
    #     warehouse[current_position] = '.'
    #     warehouse[new_position] = '@'
        
    #     if debug_mode:
    #         print_warehouse(warehouse)
        
    #     # update position
    #     current_position = new_position
            
    # elif warehouse[new_position] == '#':
    #     if debug_mode:
    #         print(f'hit a wall, robot stays at {current_position}')
                        
    # elif warehouse[new_position] == 'O':
    #     if debug_mode:
    #         print(f'hit a box, robot to move boxes moving: {current_position} --> {new_position}')
        
    #     positions_to_update = check_for_space(new_position, move, warehouse, print_out=False)
        
    #     if positions_to_update is None:    
    #         # case : no space to move boxes
    #         if debug_mode:
    #             print('case: no space to move boxes!')
            
    #     else:
    #         # case: space to move boxes
    #         if debug_mode:
    #             print('case: space to move boxes')
            
    #         warehouse = move_boxes(current_position, positions_to_update, warehouse)
            
    #         if debug_mode:
    #             print('after update')
    #             print_warehouse(warehouse)
            
    #         # update position
    #         current_position = new_position
        
    # else:
    #     print(f'unexpected input: {warehouse[new_position]}')
    #     break
    
    # if debug_mode:
    #     print()