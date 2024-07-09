def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    i = 0
    count = 0

    while i < len(flowerbed):
        if flowerbed[i] == 0:
            prev_empty = (i == 0 or flowerbed[i - 1] == 0)
            next_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

            if prev_empty and next_empty:
                count += 1
                if count >= n:
                    return True
                i += 1

        i += 1

    return count >= n


print(can_place_flowers([1, 0, 0, 0, 1], n=1))
print(can_place_flowers([0], n=1))
print(can_place_flowers([0, 0, 1, 0, 1], n=1))
print(can_place_flowers([1, 0, 0, 0, 1], n=2))
print(can_place_flowers([1, 0, 0, 0, 1, 0, 0], n=2))
print(can_place_flowers([1, 0, 1, 0, 0, 1, 0, 0, 0, 1], n=1))
