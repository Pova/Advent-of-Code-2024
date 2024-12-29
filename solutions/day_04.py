
with open("test_inputs/day_04.txt", "r") as file:

    input_data = [line.strip("\n") for line in file.readlines()]

print('\n')
print('Starting board:\n')
print('\n'.join([''.join(line) for line in input_data]))
print()

check_horizontal = False
check_vertical = False
check_diagonal_1 = True
check_diagonal_2 = False

print_no_finds = False

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
                    for j in range(y_idx,y_idx+4):
                        boolean_board[len(input_data)-1-j][x_idx] = True

# Diagonal 1 (/)
# ----------------------
# down left --> up right
# up right --> down left
# ----------------------
                        
if check_diagonal_1:
    # Diagonal 1 (down left --> up right)
    for y_idx in range(len(input_data)):
        index_list = []
        
        for x_idx in range(y_idx+1):
            
            index_list.append((x_idx,y_idx-x_idx))
            
        print(y_idx, index_list)
        
        text_line = ''.join([input_data[tuple[1]][tuple[0]] for tuple in index_list])
        print(text_line)
                        
                                      
print()
print('Boolean board:\n')
boolean_board_str = [['X' if bool else '.' for bool in bool_list] for bool_list in boolean_board]
print('\n'.join([''.join(line) for line in boolean_board_str]))
print()