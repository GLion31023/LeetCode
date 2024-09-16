def find_min_difference(time_points: list[str]) -> int:
    minutes = []

    for tp in time_points:
        time = int(tp[:2]) * 60 + int(tp[3:])
        minutes.append(time)

    minutes.sort()
    min_diff = 1440 - minutes[-1] + minutes[0]

    for i in range(len(minutes) - 1):
        min_diff = min(min_diff, minutes[i + 1] - minutes[i])

    return min_diff


print(find_min_difference(["23:59", "00:00"]))
print(find_min_difference(["00:00", "23:59", "00:00"]))
print(find_min_difference(["09:00", "18:00", "17:00"]))

# Example 1:
#
# Input: timePoints = ["23:59","00:00"]
# Output: 1

# Example 2:
#
# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0
