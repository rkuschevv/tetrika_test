

def merge_intervals(intervals: list[int]) -> list[list[int]]:
    if not intervals or len(intervals) < 2:
        return [[intervals[0], intervals[1]]] if intervals else []

    pairs = [[intervals[i], intervals[i + 1]] for i in range(0, len(intervals), 2)]
    pairs.sort(key=lambda x: x[0])

    merged = [pairs[0]]
    for current in pairs[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)

    return merged


def get_intersection(interval1: list[list[int]], interval2: list[list[int]]) -> list[list[int]]:
    result = []
    i = j = 0

    while i < len(interval1) and j < len(interval2):
        start = max(interval1[i][0], interval2[j][0])
        end = min(interval1[i][1], interval2[j][1])

        if start <= end:
            result.append([start, end])

        if interval1[i][1] < interval2[j][1]:
            i += 1
        else:
            j += 1

    return result


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = [[intervals["lesson"][0], intervals["lesson"][1]]]

    pupil_intervals = merge_intervals(intervals["pupil"])
    tutor_intervals = merge_intervals(intervals["tutor"])

    pupil_tutor = get_intersection(pupil_intervals, tutor_intervals)

    final_intervals = get_intersection(lesson, pupil_tutor)

    total_time = sum(end - start for start, end in final_intervals)

    return total_time
