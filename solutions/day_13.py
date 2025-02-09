import numpy as np
from numpy.linalg import inv, det

with open("real_inputs/day_13.txt", "r") as file:

    input_data = [line.strip("\n") for line in file.readlines()]

# print(input_data)

machines = []

idx = 0

while idx < len(input_data):
    
    a_x = int(input_data[idx].split(':')[1].split(',')[0].split('+')[1])
    a_y = int(input_data[idx].split(':')[1].split(',')[1].split('+')[1])
    b_x = int(input_data[idx+1].split(':')[1].split(',')[0].split('+')[1])
    b_y = int(input_data[idx+1].split(':')[1].split(',')[1].split('+')[1])
    prize_x = int(input_data[idx+2].split(':')[1].split(',')[0].split('=')[1])
    prize_y = int(input_data[idx+2].split(':')[1].split(',')[1].split('=')[1])
    
    machines.append(
        {
            'A':np.array([a_x,a_y]),
            'B':np.array([b_x,b_y]),
            'Prize':np.array([prize_x,prize_y]),
            'M':np.matrix([np.array([a_x,a_y]),np.array([b_x,b_y])]).T
        }
    )
    
    idx += 4

def check_machine(machine, printout = False):
    
    if det(machine['M']) == 0:
        if printout:
            print('determinant is zero')
        return None
    
    solution = inv(machine['M'])@machine['Prize'].T
    print(f'sol = {solution}')
    print(f'rounded sol = {np.round(solution)}')
    print(f'diff = {np.abs(solution - np.round(solution))}')
    # print(np.abs(solution - np.round(solution))<1e-5)
    if (
        np.all(np.abs(solution - np.round(solution))<1e-3) and
        solution[0,0] >= 0 and 
        solution[0,1] >= 0
        ):
        if printout:
            print(f'valid solution: {np.round(solution)}')
        return solution
    else:
        if printout:
            print(f'invalid solution: {solution}')
        return None

total_cost = 0

for machine in machines:
    print(machine)

for i, machine in enumerate(machines):
    print(f'on machine #{i+1}')
    solution = check_machine(machine, printout=True)
    
    if solution is None:
        print('skipping sum')
        continue
    
    extra_cost = solution*np.array([[3,1]]).T
    total_cost += extra_cost
    print(f'updated sum to {total_cost}')
    
print(int(total_cost[0,0]))

# part 2

print('updating machines for part 2')
for machine in machines:
    
    print(f"old: {machine['Prize']}")
    machine['Prize'] = machine['Prize'] + np.array([10000000000000,10000000000000])
    print(f"new: {machine['Prize']}")
    # print(machine)
    
total_cost = 0

for i, machine in enumerate(machines):
    print(f'on machine #{i+1}')
    solution = check_machine(machine, printout=True)
    
    if solution is None:
        print('skipping sum')
        continue
    
    extra_cost = solution*np.array([[3,1]]).T
    total_cost += extra_cost
    print(f'updated sum to {total_cost}')
    
print(total_cost[0,0])