def kids_with_candies(candies: list[int], extra_candies: int) -> list[bool]:
    result = [False] * len(candies)
    max_candies = max(candies)

    for i in range(len(candies)):
        if candies[i] + extra_candies >= max_candies:
            result[i] = True

    return result


print(kids_with_candies(candies=[2, 3, 5, 1, 3], extra_candies=3))
print(kids_with_candies(candies=[4, 2, 1, 1, 2], extra_candies=1))
print(kids_with_candies(candies=[12, 1, 12], extra_candies=10))
