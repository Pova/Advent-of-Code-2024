import numpy as np
import time
import os 

from time import perf_counter

testing = False

if testing:
    width, height = 11, 7
    
    with open("test_inputs/day_14.txt", "r") as file:

        input_data = [line.strip("\n") for line in file.readlines()]
else:
    width, height = 101, 103
    
    with open("real_inputs/day_14.txt", "r") as file:

        input_data = [line.strip("\n") for line in file.readlines()]
    
# print(width,height)
# print(input_data)

robots = []

robots_position = [] # optimizing speed
robots_velocity = [] # optimizing speed

for robot_line in input_data:
    
    pos_part = robot_line.split()[0]
    vel_part = robot_line.split()[1]
    
    p_x = int(pos_part.split(',')[0].split('=')[1].strip())
    p_y = int(pos_part.split(',')[1].strip())
    v_x = int(vel_part.split(',')[0].split('=')[1].strip())
    v_y = int(vel_part.split(',')[1].strip())
    
    robots.append(
        {
            'pos':np.array([p_x,p_y]),
            'vel':np.array([v_x,v_y])
        }
    )
    
    robots_position.append(np.array([p_x,p_y])) # optimizing speed
    robots_velocity.append(np.array([v_x,v_y])) # optimizing speed

pos_matrix = np.vstack(robots_position) # optimizing speed
vel_matrix = np.vstack(robots_velocity) # optimizing speed
mod_column = np.array([width, height])

# print(pos_matrix)
# print(vel_matrix)

def update_position(robots, num_of_seconds = 100, time_printout = True):
    
    if time_printout:
        start_time = time.time()

    # update position
    for robot in robots:
        robot['new_pos'] = robot['pos'] + num_of_seconds*robot['vel']
        robot['new_pos'] = robot['new_pos'] % [width, height]
        # robot['new_pos'][0] = robot['new_pos'][0]%width
        # robot['new_pos'][1] = robot['new_pos'][1]%height

    if time_printout:
        end_time = time.time()
        print(f'[update_position] total time taken = {end_time-start_time:.10f}')

    return robots

def update_position_single(robots, time_printout = False):
    
    if time_printout:
        start_time = time.time()

    # update position
    for robot in robots:
        robot['new_pos'] = robot['new_pos'] + robot['vel']
        robot['new_pos'] = robot['new_pos'] % [width, height]
        # robot['new_pos'][0] = robot['new_pos'][0]%width
        # robot['new_pos'][1] = robot['new_pos'][1]%height

    if time_printout:
        end_time = time.time()
        print(f'[update_position_single] total time taken = {end_time-start_time:.10f}')

    return robots

def update_position_matrix(pos_matrix, vel_matrix, num_of_seconds, time_printout = True):

    if time_printout:
        start_time = time.time()

    new_position = (pos_matrix + num_of_seconds*vel_matrix)%mod_column
    
    if time_printout:
        end_time = time.time()
        print(f'[update_position_matrix] total time taken = {end_time-start_time:.10f}')
    
    return new_position

def create_display(robots):
    
    display = {}
    
    # count robot positions
    for j in range(height):
        for i in range(width):
            display[(i,j)] = 0
            
    for robot in robots:
        display[(robot['new_pos'][0], robot['new_pos'][1])] += 1
        
    return display

def create_display_from_matrix(matrix):
    
    display = {}
    
    # count robot positions
    for j in range(height):
        for i in range(width):
            display[(i,j)] = 0
            
    for row in matrix:
        display[(row[0], row[1])] += 1
        
    return display
    
def print_display(display, printout=True):
    display_str = ''

    for j in range(height):
        new_line = ''
        for i in range(width):
            if display[(i,j)]>0:
                new_line += str(display[(i,j)])
            else:
                new_line += '.'
        new_line += '\n'
        display_str += new_line
    
    if printout:    
        print(display_str)
        
    return display_str

def print_display_for_symmetry(display, printout=True):
    display_str = ''

    for j in range(height):
        new_line = ''
        for i in range(width):
            
            if i == (width-1)/2:
                new_line += '|'
                continue
            
            if display[(i,j)]>0:
                new_line += str(display[(i,j)])
            else:
                new_line += '.'
        new_line += '\n'
        display_str += new_line
    
    if printout:    
        print(display_str)
        
    return display_str

def calculate_safety(display):
    # print('top left quad')
    # top left
    sum_1 = 0
    for j in range(int((height+1)/2)-1):
        for i in range(int((width+1)/2)-1):
            # print(i,j, display[(i,j)])
            sum_1 += display[(i,j)]
    # print('-'*20)
    # print('top right quad')    
    # top right
    sum_2 = 0
    for j in range(int((height+1)/2)-1):
        for i in range(int((width+1)/2),width):
            # print(i,j, display[(i,j)])
            sum_2 += display[(i,j)]
    # print('-'*20)
    # print('bottom left quad')    
    # bottom left
    sum_3 = 0
    for j in range(int((height+1)/2), height):
        for i in range(int((width+1)/2)-1):
            # print(i,j, display[(i,j)])
            sum_3 += display[(i,j)]
    # print('-'*20)
    # print('bottom right quad')    
    # bottom right
    sum_4 = 0
    for j in range(int((height+1)/2), height):
        for i in range(int((width+1)/2), width):
            # print(i,j, display[(i,j)])
            sum_4 += display[(i,j)]
    
    # print(sum_1,sum_2,sum_3,sum_4)
            
    return sum_1*sum_2*sum_3*sum_4

# part 1

# # PERFORMANCE TESTING
# # ----------------------------------------------------------------------------------------------------------------
# time_1 = 0
# time_2 = 0

# for _ in range(10000):
#     # method A (for loop)
#     start_1 = perf_counter()
#     robots = update_position(robots, num_of_seconds = 100, time_printout=False)
#     end_1 = perf_counter()

#     # method B (vectorized)
#     start_2 = perf_counter()
#     new_pos_matrix = update_position_matrix(pos_matrix, vel_matrix, num_of_seconds=100, time_printout=False).copy()
#     end_2 = perf_counter()
    
#     time_1 += (end_1-start_1)
#     time_2 += (end_2-start_2)

# print(f'method A: {(time_1)/10000:.10f} seconds')
# print(f'method B: {(time_2)/10000:.10f} seconds')
# # ----------------------------------------------------------------------------------------------------------------

# print(robots)
# print(new_pos_matrix)

# display = create_display(robots)
# print(calculate_safety(display))

# ---------------------------------------------------------------------------

# part 2

def check_for_symmetry(robots, symmetry_threshold, print_out=False, time_printout=False):
    
    if time_printout:
        start_time = time.time()
    
    symmetry_count = 0
    unique_positions = set([tuple(robot['new_pos']) for robot in robots])
    
    for position in unique_positions:
        if (width-1-position[0],position[1]) in unique_positions:
            symmetry_count += 1
    
    if print_out:
        print(f'symmetry_count (v1) = {symmetry_count}')
            
    if symmetry_count/len(unique_positions) > symmetry_threshold:
        if time_printout:
            end_time = time.time()
            print(f'[check_for_symmetry] total time taken = {end_time-start_time:.10f}')
        return True
    else:
        if time_printout:
            end_time = time.time()
            print(f'[check_for_symmetry] total time taken = {end_time-start_time:.10f}')
        return False
    
def check_for_symmetry_2(robots, symmetry_threshold, print_out=False):
    
    unique_positions = set([tuple(robot['new_pos']) for robot in robots])
    mirrored_positions = {(width-1-position[0],position[1]) for position in unique_positions}
    symmetry_count = len(unique_positions & mirrored_positions)
    
    if print_out:
        print(f'symmetry_count (v2) = {symmetry_count}')
            
    if symmetry_count/len(unique_positions) > symmetry_threshold:
        return True
    else:
        return False

def check_for_symmetry_matrix(matrix, symmetry_threshold, print_out=False):
    
    mirrored_matrix = matrix.copy()
    mirrored_matrix[:,0] = width-1-mirrored_matrix[:,0]
    
    unique_matrix = np.unique(matrix, axis=0)
    unique_mirrored_matrix = np.unique(mirrored_matrix, axis=0)
    
    sorted_matrix = unique_matrix[np.lexsort((unique_matrix[:,1], unique_matrix[:,0]))]
    sorted_mirrored_matrix = unique_mirrored_matrix[np.lexsort((unique_mirrored_matrix[:,1], unique_mirrored_matrix[:,0]))]
    
    set_a = set(map(tuple, sorted_matrix))
    set_b = set(map(tuple, sorted_mirrored_matrix))

    symmetry_count = len(set_a & set_b)
    
    if print_out:
        print(f'symmetry_count (v2) = {symmetry_count}')
            
    # if symmetry_count/len(unique_positions) > symmetry_threshold:
    #     return True
    # else:
    #     return False
    
    return symmetry_count

# ---------------------------------------------------------------------------

for robot in robots:
    robot['new_pos'] = robot['pos']
    
symmetry_threshold = 0.9
max_symmetry = 0
# counter_limit = 1000000000
counter_limit = 10000

counter = 0
winning_count = 0
found_symmetry = False

start_time = time.time()
last_recent_time = start_time

os.makedirs('day_14_renders', exist_ok=True)

while not found_symmetry and counter < counter_limit:
    
    # robots = update_position_single(robots, time_printout=True)
    matrix = update_position_matrix(pos_matrix, vel_matrix, counter, time_printout = False)
    symmetry_count = check_for_symmetry_matrix(matrix, symmetry_threshold, print_out=False)
    
    display = create_display_from_matrix(matrix)
    display_str = print_display_for_symmetry(display, printout=True)
    
    with open(f'day_14_renders.txt', 'a') as file:
        file.write(f'{counter}'+'\n')
        file.write('-'*width+'\n')
        file.write(display_str)
        file.write('-'*width+'\n')
        file.write('\n')
    # print_display(display, printout=True)
    # print(f"{symmetry_count}/{pos_matrix.shape[0]}")
    
    if symmetry_count/matrix.shape[0]>symmetry_threshold:
        winning_count = counter
        
        break
    
    counter += 1
    
    if counter % 100000 == 0:
        new_time = time.time()
        print(f'Count: {counter}')
        print(f'Time elapsed last million: {new_time - last_recent_time:.10f}')
        print(f'Total time elapsed: {new_time - start_time:.10f}')
        last_recent_time = new_time

print(f"{counter}")

