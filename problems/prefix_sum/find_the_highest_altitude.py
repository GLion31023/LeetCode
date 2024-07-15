def largest_altitude(gain: list[int]) -> int:
    highest = 0

    if gain[0] > 0:
        highest = gain[0]

    for n in range(1, len(gain)):
        gain[n] += gain[n - 1]
        highest = max(highest, gain[n])

    return highest


print(largest_altitude([-5, 1, 5, 0, -7]))
print(largest_altitude([-4, -3, -2, -1, 4, 3, 2]))
