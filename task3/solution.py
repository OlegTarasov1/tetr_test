def attendance(intervals: dict[str, list[int]]) -> int:
    start, finish = intervals['lesson']

    starts, finishes = [], []
    for i, value in enumerate([*intervals['pupil'], *intervals['tutor']]):
        if i % 2 == 0:
            if value >= finish:
                starts.append(finish)
            elif value <= start:
                starts.append(start)
            else:
                starts.append(value)
        else:
            if value >= finish:
                finishes.append(finish)
            elif value <= start:
                finishes.append(start)
            else:
                finishes.append(value)
    
    starts = sorted(starts)
    finishes = sorted(finishes)

    total_time = 0
    active_intervals = 0
    last_time = start

    for start_time, end_time in zip(starts, finishes):
        if start_time < last_time:
            start_time = last_time
        if start_time < end_time:
            total_time += end_time - start_time
            last_time = end_time

    return total_time

