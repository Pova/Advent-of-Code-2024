with open("real_inputs/day_02.txt", "r") as file:

    input_data = [line.strip("\n") for line in file.readlines()]
    
# Part 1

# class Report():
#     def __init__(self, line):
#         self.levels = [int(level) for level in line.split(" ")]
        
#     def check_safety(self):
#         # code
#         pass
        
# line_1_report = Report(input_data[0])
# print(line_1_report.levels)

reports = [[int(level) for level in report.split(" ")] for report in input_data]
# print(reports)

safe_count_1 = 0

for report in reports:
    
    if report[0] > report[-1]:
        # must be decreasing (if safe)
        for i in range(len(report)-1):
            if report[i] - report[i+1] <= 0:
                # increasing
                break
            elif report[i] - report[i+1] > 3:
                # decrease bigger than 3
                break
        else:
            safe_count_1 += 1
            
        
    elif report[0] < report[-1]:
        # must be increasing (if safe)
        for i in range(len(report)-1):
            if report[i] - report[i+1] >= 0:
                # decreasing
                break
            elif report[i] - report[i+1] < -3:
                # increase bigger than 3
                break 
        else:
            safe_count_1 += 1
    

print(safe_count_1)   

# Part 2

def check_report(report_list):
    
    if report_list[0] > report_list[-1]:
        # must be decreasing (if safe)
        for i in range(len(report_list)-1):
            if report_list[i] - report_list[i+1] <= 0:
                # increasing
                return False
            elif report_list[i] - report_list[i+1] > 3:
                # decrease bigger than 3
                return False
        else:
            return True
            
        
    elif report_list[0] < report_list[-1]:
        # must be increasing (if safe)
        for i in range(len(report_list)-1):
            if report_list[i] - report_list[i+1] >= 0:
                # decreasing
                return False
            elif report_list[i] - report_list[i+1] < -3:
                # increase bigger than 3
                return False 
        else:
            return True
            
safe_count_2 = 0

for report in reports:
    
    if check_report(report):
        
        safe_count_2 += 1
        
    else:
        
        # full report isn't safe so need to check
        for idx in range(len(report)):
            
            if check_report(report[:idx] + report[idx+1:]):
                safe_count_2 += 1
                break
            

print(safe_count_2)
    
