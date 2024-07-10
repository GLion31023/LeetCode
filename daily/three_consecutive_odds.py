def three_consecutive_odds(arr: list[int]) -> bool:
    one = two = False

    for n in arr:
        if n % 2 == 0:
            one = two = False
        elif one and two and n % 2 == 1:
            return True
        elif one and n % 2 == 1:
            two = True
        elif n % 2 == 1:
            one = True

    return False


print(three_consecutive_odds([2, 6, 4, 1]))
print(three_consecutive_odds([1, 2, 34, 3, 4, 5, 7, 23, 12]))
