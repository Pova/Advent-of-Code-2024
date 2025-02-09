with open("test_inputs/day_12_c.txt", "r") as file:

    input_data = [line.strip("\n") for line in file.readlines()]

char_set = set()

for line in input_data:
    print(line)
    for char in set(line):
        char_set.add(char)
    
print(char_set)
