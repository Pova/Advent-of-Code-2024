debug_mode = False
testing = False

if testing:
    
    with open("test_inputs/day_05.txt", "r") as file:

        input_data = [line.strip("\n") for line in file.readlines()]
        break_idx = input_data.index("")

        rules_str = input_data[:break_idx]
        pages_str = input_data[break_idx+1:]

else:
    
    with open("real_inputs/day_05.txt", "r") as file:

        input_data = [line.strip("\n") for line in file.readlines()]
        break_idx = input_data.index("")

        rules_str = input_data[:break_idx]
        pages_str = input_data[break_idx+1:]
        
rules = [(rule.split("|")[0],rule.split("|")[1]) for rule in rules_str]
pages = [page.split(',') for page in pages_str]


sum = 0
incorrect_pages = []

for page in pages:

    for rule in rules:
        # print(page, rule, page.index(rule[0]), page.index(rule[0]))
        if (rule[0] in page and rule[1] in page):
            if (page.index(rule[0]) < page.index(rule[1])):
                continue
            else:
                incorrect_pages.append(page)
                break
        else:
            continue
    else:
        sum += int(page[int((len(page)-1)/2)])
            
print(sum)

## part 2

part_2_sum = 0

for page in incorrect_pages:
    loop_condition = True
    
    if debug_mode:
        print(f'incorrect page: {page}')
        
    while loop_condition:

        for rule in rules:
            if (rule[0] in page and rule[1] in page):
                
                if debug_mode:
                    print(f'checking rule: {rule}')
                    
                left_idx = page.index(rule[0])
                right_idx = page.index(rule[1])
                
                if (left_idx < right_idx):
                    continue
                else:
                    # need to reorder page
                    page[left_idx], page[right_idx] = page[right_idx], page[left_idx]
                    break
            else:
                continue
        else:
            if debug_mode:
                print('for loop terminates')
            loop_condition = False
    
    print(page)
    part_2_sum += int(page[int((len(page)-1)/2)])
        
print(part_2_sum)