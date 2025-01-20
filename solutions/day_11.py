'''
If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
'''

import math
import time
import pickle
from tqdm import tqdm

debug_mode = False

memory = {}

with open('real_inputs/day_11.txt') as file:
    
    lines = [line.strip('\n') for line in file.readlines()]
    
numbers = [int(number) for number in lines[0].split()]

print(numbers)

def apply_rules(numbers):
    
    output_numbers = []
    
    for number in numbers:
        
        if debug_mode:
            print(number)
        if number != 0:
            if debug_mode:
                print(f"log = {int(math.log10(number))}")
        
        if number in memory.keys():
            if debug_mode:
                print('remembered')
            output_numbers += memory[number]
        elif number == 0:
            if debug_mode:
                print('zero')
            memory[number] = [1]
            output_numbers += [1]
        elif (int(math.log10(number))+1) % 2 == 0:
            if debug_mode:
                print('big number : split')
            char_num = int(math.log10(number))+1
            left_num = number//10**(char_num/2)
            right_num = number - left_num*(10**(char_num/2))
            if debug_mode:
                print(left_num, right_num)
            memory[number] = [left_num, right_num]
            output_numbers += [left_num, right_num]
        else:
            if debug_mode:
                print('leftover')
            memory[number] = [number*2024]
            output_numbers += [number*2024]
            
    return output_numbers

# part 1

start = time.time()

for i in range(25):
    print(i)
    numbers = apply_rules(numbers)
    
    # with open(f'day_11_lists/day_11_list_after_{i+1}.pkl', 'wb') as file:
    #     pickle.dump(numbers, file)
        
    # print(numbers)
    # print('-'*20)
    
print(len(numbers))

end = time.time()

diff = end - start

print(f"Time taken: {diff:.2f} seconds")

# part 2

def apply_rules_individual(number):
    
    output_numbers = []
        
    if debug_mode:
        print(number)
    if number != 0:
        if debug_mode:
            print(f"log = {int(math.log10(number))}")
    
    if number in memory.keys():
        if debug_mode:
            print('remembered')
        output_numbers += memory[number]
    elif number == 0:
        if debug_mode:
            print('zero')
        memory[number] = [1]
        output_numbers += [1]
    elif (int(math.log10(number))+1) % 2 == 0:
        if debug_mode:
            print('big number : split')
        char_num = int(math.log10(number))+1
        left_num = number//10**(char_num/2)
        right_num = number - left_num*(10**(char_num/2))
        if debug_mode:
            print(left_num, right_num)
        memory[number] = [left_num, right_num]
        output_numbers += [left_num, right_num]
    else:
        if debug_mode:
            print('leftover')
        memory[number] = [number*2024]
        output_numbers += [number*2024]
        
    return output_numbers

print(apply_rules_individual(0))

counts = {}

for num in range(10):
    
    print(f'On num = {num}')
    
    counts[num] = [1]
    numbers = [num]
    
    for _ in tqdm(range(75), desc="Processing"):
    
        numbers = apply_rules(numbers)
        counts[num].append(len(numbers))