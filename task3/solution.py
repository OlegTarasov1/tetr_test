def appearance(
        intervals: dict[str, list[int]]
    ) -> int:
    
    pupil_intervals = intervals.get("pupil")
    tutor_intervals = intervals.get("tutor")
    lesson = intervals.get("lesson")

    pupil_intervals = [[pupil_intervals[i], pupil_intervals[i+1]] for i in range(0, len(pupil_intervals), 2)]
    tutor_intervals = [[tutor_intervals[i], tutor_intervals[i+1]] for i in range(0, len(tutor_intervals), 2)]

    pupil_intervals = interval_trim(pupil_intervals, lesson)
    tutor_intervals = interval_trim(tutor_intervals, lesson)

    if not pupil_intervals or not tutor_intervals:
        return 0

    pupils_merged = merge(pupil_intervals, lesson)
    tutor_merged = merge(tutor_intervals, lesson)

    result = merge_pupils_and_tutors(
        pupils_sorted = pupils_merged,
        tutors_sorted = tutor_merged
    )

    return result


def merge(
        intervals: list[list[int]],
        lesson: list[int]
    ) -> list[list[int]]:

    intervals.sort(key = lambda i: i[0])
    current_start, current_end = intervals[0]
    merged = []
    for start, end in intervals[1:]:
        if start <= current_end:
            current_end = current_end if current_end >= end else end
        else:
            merged.append([current_start, current_end])
            current_start, current_end = start, end

    merged.append([current_start, current_end])

    return merged


def merge_pupils_and_tutors(
        pupils_sorted: list[list[int]],
        tutors_sorted: list[list[int]]
    ) -> int:

    i = j = 0
    result = 0

    while i < len(pupils_sorted) and j < len(tutors_sorted):
        ps_start, ps_end = pupils_sorted[i]
        ts_start, ts_end = tutors_sorted[j]

        start = max(ps_start, ts_start)
        end = min(ps_end, ts_end)

        if start < end:
            result += end - start

        if ps_end <= ts_end:
            i += 1
        else:
            j += 1

    return result

def interval_trim(
        interval: list[list[int]],
        lesson: list[int]
    ) -> list[int]:

    new_list = []
    start, end = lesson
    for i in interval:
        if i[1] <= start or i[0] >= end:
            continue
        trimmed_start = max(i[0], start)
        trimmed_end = min(i[1], end)
        new_list.append([trimmed_start, trimmed_end])

    return new_list








# def attendance(intervals: dict[str, list[int]]) -> int:
#     start, finish = intervals['lesson']

#     starts, finishes = [], []
#     for i, value in enumerate([*intervals['pupil'], *intervals['tutor']]):
#         if i % 2 == 0:
#             if value >= finish:
#                 starts.append(finish)
#             elif value <= start:
#                 starts.append(start)
#             else:
#                 starts.append(value)
#         else:
#             if value >= finish:
#                 finishes.append(finish)
#             elif value <= start:
#                 finishes.append(start)
#             else:
#                 finishes.append(value)
    
#     starts = sorted(starts)
#     finishes = sorted(finishes)

#     total_time = 0
#     active_intervals = 0
#     last_time = start

#     for start_time, end_time in zip(starts, finishes):
#         if start_time < last_time:
#             start_time = last_time
#         if start_time < end_time:
#             total_time += end_time - start_time
#             last_time = end_time

#     return total_time

