debug_mode = False

with open('test_inputs/day_08.txt') as file:
    
    lines = [line.strip('\n') for line in file.readlines()]
    
print(lines)

width = len(lines[0])
height = len(lines)

# Process the lines

symbols = {}

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '.':
            continue
        
        if char in symbols.keys():
            symbols[char].append((x,y))
        else:
            symbols[char] = [(x,y),]
            
print(symbols)
    
unique_pairs = {}

for antenna, positions in symbols.items():
    
    # calculate all unique pairs...
    # dont worry about redundant calculation - this should work for now.
    # improve later.
    
    unique_pairs[antenna] = []
    
    for position_1 in positions:
        for position_2 in positions:
            
            if position_1 == position_2:
                continue
            
            unique_pairs[antenna].append((position_1, position_2))
            
print(unique_pairs)

antinode_locations = []

for antenna_code, location_tuples in unique_pairs.items():
    
    for location_tuple in location_tuples:
            
        # v: from A' (2nd tuple) to A (1st tuple)
        
        delta_x = location_tuple[0][0] - location_tuple[1][0]
        delta_y = location_tuple[0][1] - location_tuple[1][1]
        
        new_tuple = (location_tuple[0][0]+delta_x,location_tuple[0][1]+delta_y)
        
        if new_tuple[0] >= width or new_tuple[0] < 0:
            continue
        
        if new_tuple[1] >= height or new_tuple[1] < 0:
            continue
        
        antinode_locations.append(new_tuple)

antinode_locations = set(antinode_locations)

print(antinode_locations)
print(len(antinode_locations))

# part 2

antinode_locations_2 = []

for antenna_code, location_tuples in unique_pairs.items():
    
    for location_tuple in location_tuples:
            
        # v: from A' (2nd tuple) to A (1st tuple)
        
        delta_x = location_tuple[0][0] - location_tuple[1][0]
        delta_y = location_tuple[0][1] - location_tuple[1][1]
        multiplier = 0
        tuple_location = location_tuple[0]
        
        while (tuple_location[0]):
            
            new_tuple = (location_tuple[0][0]+delta_x*multiplier,location_tuple[0][1]+delta_y*multiplier)
            
            if new_tuple[0] >= width or new_tuple[0] < 0:
                break
            
            if new_tuple[1] >= height or new_tuple[1] < 0:
                break
            
            antinode_locations_2.append(new_tuple)
            multiplier += 1
        

antinode_locations_2 = set(antinode_locations_2)

print(antinode_locations_2)
print(len(antinode_locations_2))

for j in range(height):
    for i in range(width):
        pass