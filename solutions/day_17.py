debug_mode = True
testing = True

if testing:
    
    with open("test_inputs/day_17.txt", "r") as file:

        input_data = [line.strip("\n") for line in file.readlines()]
        break_idx = input_data.index("")

        register_lines = input_data[:break_idx]
        program = input_data[break_idx+1]

else:
    
    with open("real_inputs/day_17.txt", "r") as file:

        input_data = [line.strip("\n") for line in file.readlines()]
        break_idx = input_data.index("")

        register_lines = input_data[:break_idx]
        program = input_data[break_idx+1]
        
print(register_lines)
print(program)

# instruction, opcode



# The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.

# The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.

# The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.

# The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.

# The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)

# The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)

# The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)

# The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)