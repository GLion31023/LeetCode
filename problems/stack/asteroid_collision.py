def asteroid_collision(asteroids: list[int]) -> list[int]:
    stack = []

    for a in asteroids:
        while stack and stack[-1] > 0 > a:
            if stack[-1] < -a:
                stack.pop()
                continue
            elif stack[-1] == -a:
                stack.pop()
            break
        else:
            stack.append(a)

    return stack


print(asteroid_collision([5, 10, -5]))
print(asteroid_collision([8, -8]))
print(asteroid_collision([10, 2, -5]))
print(asteroid_collision([-2, -1, 1, 2]))
print(asteroid_collision([-2, -2, 1, -2]))
