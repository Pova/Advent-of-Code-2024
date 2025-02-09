
with open("real_inputs/day_04.txt", "r") as file:

    input_data = [line.strip("\n") for line in file.readlines()]

debug_mode = False
print_no_finds = False
print_starting_board = True
print_boolean_board = False

total_xmas_count = 0

check_horizontal = True
check_vertical = True
check_diagonal_1 = True
check_diagonal_2 = True


# idea: scan across in 6 days:

# Horizontal
# ----------------------
# left --> right
# right --> left
# ----------------------

# Vertical
# ----------------------
# up --> down
# down --> up
# ----------------------

# Diagonal 1 (/)
# ----------------------
# down left --> up right
# up right --> down left
# ----------------------

# Diagonal 2 (\)
# ----------------------
# up left --> down right
# down right --> up left
# ----------------------

if print_starting_board:
    print('\n')
    print('Starting board:\n')
    print('\n'.join([''.join(line) for line in input_data]))
    print()

# part 1

boolean_board = [[False for col_count in range(len(input_data[0]))] for row_count in range(len(input_data))]

if check_horizontal:
    # Horizontal (left --> right)
    for y_idx in range(len(input_data)):
        
        text_line = input_data[y_idx]
        
        if text_line.find('XMAS') == -1:
            if print_no_finds:
                print(f'no horizontal (left-to-right) XMAS on line: {y_idx}')
            continue
        else:
            for x_idx in range(len(input_data[0])-3):
                if text_line[x_idx:x_idx+4] == 'XMAS':
                    total_xmas_count += 1
                    for i in range(x_idx,x_idx+4):
                        boolean_board[y_idx][i] = True

    # Horizontal (right --> left)
    for y_idx in range(len(input_data)):
        
        text_line = input_data[y_idx][::-1]
        
        if text_line.find('XMAS') == -1:
            if print_no_finds:
                print(f'no horizontal (right-to-left) XMAS on line: {y_idx}')
            continue
        else:
            for x_idx in range(len(input_data[0])-3):
                if text_line[x_idx:x_idx+4] == 'XMAS':
                    total_xmas_count += 1
                    for i in range(x_idx,x_idx+4):
                        boolean_board[y_idx][len(input_data[0])-1-i] = True
                        
if check_vertical:
    # Vertical (up --> down)
    for x_idx in range(len(input_data[0])):
        
        text_line = ''.join([line[x_idx] for line in input_data])
        
        if text_line.find('XMAS') == -1:
            if print_no_finds:
                print(f'no vertical (up-to-down) XMAS on line: {x_idx}')
            continue
        else:
            for y_idx in range(len(input_data)-3):
                if text_line[y_idx:y_idx+4] == 'XMAS':
                    total_xmas_count += 1
                    for j in range(y_idx,y_idx+4):
                        boolean_board[j][x_idx] = True
    
    # Horizontal (down --> up)
    for x_idx in range(len(input_data[0])):
        
        text_line = ''.join([line[x_idx] for line in input_data])[::-1]
        
        if text_line.find('XMAS') == -1:
            if print_no_finds:
                print(f'no horizontal (down-to-up) XMAS on line: {y_idx}')
            continue
        else:
            for y_idx in range(len(input_data)-3):
                if text_line[y_idx:y_idx+4] == 'XMAS':
                    total_xmas_count += 1
                    for j in range(y_idx,y_idx+4):
                        boolean_board[len(input_data)-1-j][x_idx] = True

# Diagonal 1 (/)
# ----------------------
# down left --> up right
# up right --> down left
# ----------------------
                        
if check_diagonal_1:
    
    # down left --> up right
    
    for diag_value in range(len(input_data) + len(input_data[0]) - 1):
        
        if debug_mode:
            print(f'diag_value = {diag_value}')
        diagonal_positions = []
        diagonal_characters = []
        y_idx = diag_value if diag_value < len(input_data) else len(input_data)-1
        
        for x_idx in range(diag_value-y_idx,len(input_data[0])):
            if diag_value-x_idx < 0:
                break
            
            diagonal_positions.append((x_idx, diag_value-x_idx))
            diagonal_characters.append(input_data[diag_value-x_idx][x_idx])
            # print(f'x_idx, y_idx = {x_idx}, {y_idx} ')
        
        if len(diagonal_positions) < 4:
            continue
         
        if debug_mode:
            print(diagonal_positions, len(diagonal_positions))
        text_line = ''.join(diagonal_characters)
        if debug_mode:
            print(text_line)
        
        if text_line.find('XMAS') == -1:
            if print_no_finds:
                print(f'no diagonal (/) XMAS on line: {diagonal_positions}')
            continue
        else:
            for idx in range(len(text_line)):
                if text_line[idx:idx+4] == 'XMAS':
                    total_xmas_count += 1
                    for tuple in diagonal_positions[idx:idx+4]:
                        i = tuple[0]
                        j = tuple[1]
                        boolean_board[j][i] = True
                        
    # up right --> down left
    
    for diag_value in range(len(input_data) + len(input_data[0]) - 1):
        
        if debug_mode:
            print(f'diag_value = {diag_value}')
        diagonal_positions = []
        diagonal_characters = []
        y_idx = diag_value if diag_value < len(input_data) else len(input_data)-1
        
        for x_idx in range(diag_value-y_idx,len(input_data[0])):
            if diag_value-x_idx < 0:
                break
            
            diagonal_positions.append((x_idx, diag_value-x_idx))
            diagonal_characters.append(input_data[diag_value-x_idx][x_idx])
            # print(f'x_idx, y_idx = {x_idx}, {y_idx} ')
        
        if len(diagonal_positions) < 4:
            continue
         
        if debug_mode:
            print(diagonal_positions, len(diagonal_positions))
        text_line = ''.join(diagonal_characters)
        if debug_mode:
            print(text_line)
        
        if text_line.find('SAMX') == -1:
            if print_no_finds:
                print(f'no diagonal (/) SAMX on line: {diagonal_positions}')
            continue
        else:
            for idx in range(len(text_line)):
                if text_line[idx:idx+4] == 'SAMX':
                    total_xmas_count += 1
                    for tuple in diagonal_positions[idx:idx+4]:
                        i = tuple[0]
                        j = tuple[1]
                        boolean_board[j][i] = True

# Diagonal 2 (/)
# ----------------------
# up left --> down right
# down right --> up left
# ----------------------
                        
if check_diagonal_2:
    
    # down left --> up right
    
    for diag_value in range(len(input_data) + len(input_data[0]) - 1):
        
        if debug_mode:
            print(f'diag_value = {diag_value}')
        diagonal_positions = []
        diagonal_characters = []
        
        y_idx = diag_value if diag_value < len(input_data) else len(input_data)-1
        # for x_idx in range(diag_value-y_idx,len(input_data[0])):
        
        for x_idx in range((len(input_data[0])-1-(diag_value-y_idx)),-1,-1):
            
            if x_idx-((len(input_data[0])-1)-diag_value)<0:
                break
            
            diagonal_positions.append((x_idx, x_idx-((len(input_data[0])-1)-diag_value)))
            diagonal_characters.append(input_data[x_idx-((len(input_data[0])-1)-diag_value)][x_idx])
            
            # print(f'x_idx, y_idx = {x_idx}, {y_idx} ')
        
        if len(diagonal_positions) < 4:
            continue
         
        if debug_mode:
            print(diagonal_positions, len(diagonal_positions))
        text_line = ''.join(diagonal_characters)
        if debug_mode:
            print(text_line)
        
        if text_line.find('XMAS') == -1:
            if print_no_finds:
                print(f'no diagonal (/) XMAS on line: {diagonal_positions}')
            continue
        else:
            for idx in range(len(text_line)):
                if text_line[idx:idx+4] == 'XMAS':
                    total_xmas_count += 1
                    for tuple in diagonal_positions[idx:idx+4]:
                        i = tuple[0]
                        j = tuple[1]
                        boolean_board[j][i] = True
    
    # --------------
                        
    for diag_value in range(len(input_data) + len(input_data[0]) - 1):
        
        if debug_mode:
            print(f'diag_value = {diag_value}')
        diagonal_positions = []
        diagonal_characters = []
        
        y_idx = diag_value if diag_value < len(input_data) else len(input_data)-1
        # for x_idx in range(diag_value-y_idx,len(input_data[0])):
        
        for x_idx in range((len(input_data[0])-1-(diag_value-y_idx)),-1,-1):
            
            if x_idx-((len(input_data[0])-1)-diag_value)<0:
                break
            
            diagonal_positions.append((x_idx, x_idx-((len(input_data[0])-1)-diag_value)))
            diagonal_characters.append(input_data[x_idx-((len(input_data[0])-1)-diag_value)][x_idx])
            
            # print(f'x_idx, y_idx = {x_idx}, {y_idx} ')
        
        if len(diagonal_positions) < 4:
            continue
         
        if debug_mode:
            print(diagonal_positions, len(diagonal_positions))
        text_line = ''.join(diagonal_characters)
        if debug_mode:
            print(text_line)
        
        if text_line.find('SAMX') == -1:
            if print_no_finds:
                print(f'no diagonal (/) SAMX on line: {diagonal_positions}')
            continue
        else:
            for idx in range(len(text_line)):
                if text_line[idx:idx+4] == 'SAMX':
                    total_xmas_count += 1
                    for tuple in diagonal_positions[idx:idx+4]:
                        i = tuple[0]
                        j = tuple[1]
                        boolean_board[j][i] = True

if print_boolean_board:                
    print()
    print('Boolean board:\n')
    boolean_board_str = [['X' if bool else '.' for bool in bool_list] for bool_list in boolean_board]
    print('\n'.join([''.join(line) for line in boolean_board_str]))
    print()

print('Part 1 answer:')
print('-'*15)
print(total_xmas_count)
print('-'*15+'\n')

# part 2

part_2_count = 0

def board(x,y):
    return input_data[y][x]

for j in range(1,len(input_data[0])-1):
    for i in range(1, len(input_data[0])-1):
        # print(i,j,board(i,j))
        
        if board(i,j) == 'A':
            # print(f'found an A at: {(i,j)}')
            
            # check 1
            # M.M
            # .A.
            # S.S
            if (
                (board(i-1,j-1)=='M') &
                (board(i+1,j-1)=='M') &
                (board(i-1,j+1)=='S') &
                (board(i+1,j+1)=='S')
            ):
                part_2_count += 1
            # check 2
            # M.S
            # .A.
            # M.S
            elif (
                (board(i-1,j-1)=='M') &
                (board(i+1,j-1)=='S') &
                (board(i-1,j+1)=='M') &
                (board(i+1,j+1)=='S')
            ):
                part_2_count += 1
            # check 3
            # S.S
            # .A.
            # M.M
            elif (
                (board(i-1,j-1)=='S') &
                (board(i+1,j-1)=='S') &
                (board(i-1,j+1)=='M') &
                (board(i+1,j+1)=='M')
            ):
                part_2_count += 1
            # check 4
            # S.M
            # .A.
            # S.M
            elif (
                (board(i-1,j-1)=='S') &
                (board(i+1,j-1)=='M') &
                (board(i-1,j+1)=='S') &
                (board(i+1,j+1)=='M')
            ):
                part_2_count += 1
                
print('Part 2 answer:')
print('-'*15)           
print(part_2_count)
print('-'*15)           