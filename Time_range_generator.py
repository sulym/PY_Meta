time_start = (23, 59, 58)
time_end = (0, 0, 10)

def time_range(time_start: tuple, time_end: tuple) -> tuple:
    start_seconds = time_start[0] * 3600 + time_start[1] * 60 + time_start[2]
    end_seconds = time_end[0] * 3600 + time_end[1] * 60 + time_end[2]

    current_seconds = start_seconds
    while current_seconds != end_seconds:  
        current_time = (current_seconds // 3600, (current_seconds % 3600) // 60, current_seconds % 60)
        yield current_time
        
        current_seconds = (current_seconds + 1) % 86400 

iterator = time_range(time_start, time_end)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

### M ###

def time_range(time_start: tuple, time_end: tuple) -> tuple:
    current_time = list(time_start)

    while time_end != tuple(current_time):
        yield tuple(current_time)
        if (
            current_time[0] == 23
            and current_time[1] == 59
            and current_time[2] == 59
        ):
            current_time = [0, 0, 0]
        elif current_time[1] == 59 and current_time[2] == 59:
            current_time = [current_time[0] + 1, 0, 0]
        elif current_time[2] == 59:
            current_time = [current_time[0], current_time[1] + 1, 0]
        else:
            current_time[2] += 1
iterator = time_range(time_start, time_end)
print(next(iterator))
print(next(iterator))