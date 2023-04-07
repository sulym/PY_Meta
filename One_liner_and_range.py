student_runs = [
    [5.9, 12.8, 26.5, 145.9],
    [6.1, 13.2, 30.1, 149],
    [6.6, 14.3, 32.3, 152.5]
]

def group_runs(student_runs: list) -> list:
    # write your code here
    
            
    return [[k[index] for k in student_runs] for index in range(4)]

print(group_runs(student_runs))
