with open('real_inputs/day_06.txt') as file:
    
    lines = [line.strip('\n') for line in file.readlines()]

def get_new_coords(old_coords, direction):
    
    if direction == '^':
        return (old_coords[0], old_coords[1]-1)
    elif direction == 'v':
        return (old_coords[0], old_coords[1]+1)
    elif direction == '<':
        return (old_coords[0]-1, old_coords[1])
    elif direction == '>':
        return (old_coords[0]+1, old_coords[1])
    else:
        raise Exception
    
def check_if_inbounds(position, height, width):
    '''
    False : out of bounds
    True : in bounds
    '''
    
    if position[0] < 0 or position[0] >= width:
        return False
    elif position[1] < 0 or position[1] >= height:
        return False
    else: 
        return True

def check_for_obstacle(lab, position):
    
    '''
    True : no obstable
    False: obstable
    '''
    
    if lab[position] != '#':
        return True
    else:
        return False

update_rule = {
    '^':'>',
    '>':'v',
    'v':'<',
    '<':'^'
}

def update_direction(old_direction):
    
    return update_rule[old_direction]

def print_lab(lab):

    lab_string = ''
    
    for row_idx in range(height):
        lab_string += '\n'
        for col_idx in range(width):
            lab_string += lab[(col_idx, row_idx)]
    lab_string += '\n'        
    print(lab_string)

height = len(lines)
width = len(lines[0])

lab = {}
inbounds = True

for y_pos, line in enumerate(lines):
    
    for x_pos, char in enumerate(line):
        
        lab[(x_pos, y_pos)] = char
        
        if char in ['^', 'v', '>', '<']:
            
            initial_position = (x_pos, y_pos)
            initial_direction = char

current_position = initial_position
current_direction = initial_direction

previous_positions = {current_position,}
previous_positions_list = [current_position,]

counter = 0

print_updates = False
print_positions = False

print('-'*10)
print(f'starting position: {current_position}')
print('-'*10)

while inbounds and counter < 100000:
    
    new_position = get_new_coords(current_position, current_direction)
    
    if print_updates:
        print(f'new (potential) position: {new_position}')
    
    if check_if_inbounds(new_position, height, width):
        if print_updates:
            print(f'new position is inbounds')
        
        if not check_for_obstacle(lab, new_position):
            if print_updates:
                print(f'obstable at new position:')
            
            current_direction = update_direction(current_direction)
        else:
            if print_updates:
                print('no obstable at new position')
            
            if print_updates:
                print('updating position')
            current_position = new_position
            
            previous_positions.add(new_position)
            previous_positions_list.append(new_position)
            
    else:
        if print_updates:
            print(f'new position is out of bounds')
        inbounds = False        
        
    counter += 1

print()
print('Number of unique positions:')
print(len(previous_positions))
print()

output_lab = lab.copy()

for positions in previous_positions:
    output_lab[positions] = 'X'

if print_positions:
    print_lab(output_lab)
    
# PART 2

def check_for_loops(lab_dict):
    
    counter = 0
    inbounds = True
    current_position = initial_position
    current_direction = initial_direction
    lab_directions = {current_position:[current_direction,],}
    
    while inbounds and counter < 1000000:
    
        new_position = get_new_coords(current_position, current_direction)
        
        if print_updates:
            print(f'new (potential) position: {new_position}')
        
        if check_if_inbounds(new_position, height, width):
            if print_updates:
                print(f'new position is inbounds')
            
            if not check_for_obstacle(lab_dict, new_position):
                if print_updates:
                    print(f'obstable at new position:')
                
                current_direction = update_direction(current_direction)
                
                if current_position in lab_directions.keys() and current_direction in lab_directions[current_position]:
                    if print_updates:
                        print('found a loop!')
                    return True
                
                elif current_position in lab_directions.keys():
                    lab_directions[current_position].append(current_direction)
                    
                else:
                    lab_directions[current_position] = [current_direction,]
            else:
                if print_updates:
                    print('no obstable at new position')
                
                if print_updates:
                    print('updating position')
                    
                current_position = new_position
                
                if current_position in lab_directions.keys() and current_direction in lab_directions[current_position]:
                    if print_updates:
                        print('found a loop!')
                    return True
                
                elif current_position in lab_directions.keys():
                    lab_directions[current_position].append(current_direction)
                    
                else:
                    lab_directions[current_position] = [current_direction,]
                
        else:
            if print_updates:
                print(f'new position is out of bounds')
            return False        
            
        counter += 1
        
        if counter == 1000000:
            print('triggered counter failsafe')


position_count = 0

# Idea : can keep track of directions

for y_idx in range(height):
    for x_idx in range(width):
        
        if (x_idx, y_idx) == initial_position:
            if print_updates:
                print('cannot replace starting position')
            
        elif lab[(x_idx, y_idx)] == '#':
            if print_updates:
                print('already an obstacle')
        else:
            if print_updates:
                print(f'trying position: {(x_idx, y_idx)}')
            
            current_lab_version = lab.copy()
            current_lab_version[(x_idx, y_idx)] = '#'
            
            # print_lab(current_lab_version)
            
            if check_for_loops(current_lab_version):
                position_count += 1
            else:
                continue

print('Number of possible new obstacles:')    
print(position_count)