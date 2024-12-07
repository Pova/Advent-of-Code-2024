with open("real_inputs/day_01.txt", "r") as file:
    input_data = [(int(strings[0]),int(strings[-1])) for strings in [line.strip("\n").split(" ") for line in file.readlines()]]

# Part 1
input_data_1 = sorted([tuple[0] for tuple in input_data])
input_data_2 = sorted([tuple[1] for tuple in input_data])

part_1_sum = 0
for i, j in zip(input_data_1,input_data_2):
    part_1_sum += abs(i - j)

print(part_1_sum)

# Part 2
from collections import Counter

right_list_freq = Counter(input_data_2)

part_2_sum = 0

for left_num in input_data_1:
    part_2_sum += left_num*right_list_freq[left_num]
    
print(part_2_sum)