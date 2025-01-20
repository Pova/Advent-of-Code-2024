debug_mode = False

with open('real_inputs/day_10.txt') as file:
    
    lines = [line.strip('\n') for line in file.readlines()]
    
print(lines)

starting_indices = []
map = {}

for j, line in enumerate(lines):
    for i, char in enumerate(line):
        
        if char == '0':
            starting_indices.append((i,j))
            
        map[(i,j)] = int(char)
    
def check_trailhead_part_1(position, current_height, debug_mode = False):
        
    if debug_mode:
        print(f"called with: {position, current_height}")
    
    up_position = (position[0], position[1]-1) if (position[0], position[1]-1) in map.keys() else None
    right_position = (position[0]+1, position[1]) if (position[0]+1, position[1]) in map.keys() else None
    down_position = (position[0], position[1]+1) if (position[0], position[1]+1) in map.keys() else None
    left_position = (position[0]-1, position[1]) if (position[0]-1, position[1]) in map.keys() else None
        
    if current_height < 9:
        if debug_mode:
            print('not yet at end of path')
            
        if debug_mode:
            print('checking up')
        if (up_position and map[up_position] == current_height + 1):
            up_count = check_trailhead_part_1(up_position, current_height + 1)
        else:
            up_count = None
        
        if debug_mode:
            print('checking right')
        if (right_position and map[right_position] == current_height + 1):
            right_count = check_trailhead_part_1(right_position, current_height + 1)
        else:
            right_count = None
        
        if debug_mode:
            print('checking down')
        if (down_position and map[down_position] == current_height + 1):
            down_count = check_trailhead_part_1(down_position, current_height + 1)
        else:
            down_count = None
        
        if debug_mode:
            print('checking left')
        if (left_position and map[left_position] == current_height + 1):
            left_count = check_trailhead_part_1(left_position, current_height + 1)
        else:
            left_count = None
        
        new_sum = []
        if debug_mode:
            print('summing up')
        
        if up_count:
            new_sum += up_count
        if right_count:
            new_sum += right_count
        if down_count:
            new_sum += down_count
        if left_count:
            new_sum += left_count
        
        if debug_mode:
            print('-'*30)
        
        if debug_mode:
            print(f'[{position, current_height}] call (partial) - returning {new_sum} from {up_count, right_count, down_count, left_count}')
        return new_sum
        
    else:
        if debug_mode:
            print(f'[{position, current_height}] call (final) - returning 1')
        
        return [position]

total_count_part_1 = 0        
    
for position in starting_indices:
    
    total_count_part_1 += len(set(check_trailhead_part_1(position, current_height = 0)))
    
print(total_count_part_1)

# part 2

def check_trailhead_part_2(position, current_height, debug_mode = False):
        
    if debug_mode:
        print(f"called with: {position, current_height}")
    
    up_position = (position[0], position[1]-1) if (position[0], position[1]-1) in map.keys() else None
    right_position = (position[0]+1, position[1]) if (position[0]+1, position[1]) in map.keys() else None
    down_position = (position[0], position[1]+1) if (position[0], position[1]+1) in map.keys() else None
    left_position = (position[0]-1, position[1]) if (position[0]-1, position[1]) in map.keys() else None
        
    if current_height < 9:
        if debug_mode:
            print('not yet at end of path')
            
        if debug_mode:
            print('checking up')
        if (up_position and map[up_position] == current_height + 1):
            up_count = check_trailhead_part_2(up_position, current_height + 1)
        else:
            up_count = None
        
        if debug_mode:
            print('checking right')
        if (right_position and map[right_position] == current_height + 1):
            right_count = check_trailhead_part_2(right_position, current_height + 1)
        else:
            right_count = None
        
        if debug_mode:
            print('checking down')
        if (down_position and map[down_position] == current_height + 1):
            down_count = check_trailhead_part_2(down_position, current_height + 1)
        else:
            down_count = None
        
        if debug_mode:
            print('checking left')
        if (left_position and map[left_position] == current_height + 1):
            left_count = check_trailhead_part_2(left_position, current_height + 1)
        else:
            left_count = None
        
        new_sum = 0
        if debug_mode:
            print('summing up')
        
        if up_count:
            new_sum += up_count
        if right_count:
            new_sum += right_count
        if down_count:
            new_sum += down_count
        if left_count:
            new_sum += left_count
        
        if debug_mode:
            print('-'*30)
        
        if debug_mode:
            print(f'[{position, current_height}] call (partial) - returning {new_sum} from {up_count, right_count, down_count, left_count}')
        return new_sum
        
    else:
        if debug_mode:
            print(f'[{position, current_height}] call (final) - returning 1')
        
        return 1

total_count_part_2 = 0

for position in starting_indices:
    
    total_count_part_2 += check_trailhead_part_2(position, current_height = 0)
    
print(total_count_part_2)

# 1676
# your answer is too high