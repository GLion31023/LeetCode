def num_water_bottles(numBottles: int, numExchange: int) -> int:
    drink = numBottles

    while numBottles >= numExchange:
        remaining = numBottles % numExchange
        numBottles //= numExchange
        drink += numBottles
        numBottles += remaining

    return drink


print(num_water_bottles(numBottles=9, numExchange=3))
print(num_water_bottles(numBottles=15, numExchange=4))
print(num_water_bottles(numBottles=15, numExchange=8))
