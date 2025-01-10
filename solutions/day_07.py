debug_mode = False

with open('real_inputs/day_07.txt') as file:
    
    lines = [line.strip('\n') for line in file.readlines()]
    
def check_sequence(target, current_number, numbers):
    if debug_mode:
        print(f'checking: {(target, starting_number, numbers)}')
    
    if numbers == []:
        
        if target == current_number:
            return True
        else:
            return False
        
    new_number = numbers[0]
    new_numbers = numbers.copy()
    new_numbers.remove(new_number)
    if debug_mode:
        print(new_number, new_numbers)
    
    return check_sequence(target, current_number+new_number, new_numbers) or check_sequence(target, current_number*new_number, new_numbers)

equation_sum = 0

for line in lines:
    
    target = int(line.split(':')[0])
    numbers = [int(num) for num in line.split(':')[1].strip().split()]
    starting_number = numbers.pop(0)
    
    if debug_mode:
        print(target)
    if debug_mode:
        print(starting_number)
    if debug_mode:
        print(numbers)
    
    if check_sequence(target, starting_number, numbers):
        
        if debug_mode:
            print(f'its possible to make {target}')
        equation_sum += target
        
print(equation_sum)

# Part 2 - add number concatenation

def check_sequence_part_2(target, current_number, numbers):
    if debug_mode:
        print(f'checking: {(target, starting_number, numbers)}')
    
    if numbers == []:
        
        if target == current_number:
            return True
        else:
            return False
        
    new_number = numbers[0]
    new_numbers = numbers.copy()
    new_numbers.remove(new_number)
    
    if debug_mode:
        print(new_number, new_numbers)
    
    return (
        check_sequence_part_2(target, current_number+new_number, new_numbers) or 
        check_sequence_part_2(target, current_number*new_number, new_numbers) or
        check_sequence_part_2(target, int(str(current_number)+str(new_number)), new_numbers)
    ) 

equation_sum = 0

for line in lines:
    
    target = int(line.split(':')[0])
    numbers = [int(num) for num in line.split(':')[1].strip().split()]
    starting_number = numbers.pop(0)
    
    if debug_mode:
        print(target)
    if debug_mode:
        print(starting_number)
    if debug_mode:
        print(numbers)
    
    if check_sequence_part_2(target, starting_number, numbers):
        
        if debug_mode:
            print(f'its possible to make {target}')
        equation_sum += target
        
print(equation_sum)