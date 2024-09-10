def robot_sim(commands: list[int], obstacles: list[list[int]]) -> int:
    res = 0

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 0: Nord, 1: East, 2: South, 3: West
    cur_d = 0
    x, y = 0, 0

    obstacle_set = set(map(tuple, obstacles))

    for c in commands:
        if c == -2:
            cur_d = (cur_d - 1) % 4  # Using modulo to keep current direction in range 0 - 3 when turning
        elif c == -1:
            cur_d = (cur_d + 1) % 4
        else:
            for _ in range(c):
                nx = x + dirs[cur_d][0]
                ny = y + dirs[cur_d][1]

                if (nx, ny) not in obstacle_set:
                    x, y = nx, ny
                    res = max(res, x * x + y * y)
                else:
                    break

    return res


print(robot_sim(commands=[4, -1, 3], obstacles=[]))
print(robot_sim(commands=[4, -1, 4, -2, 4], obstacles=[[2, 4]]))
print(robot_sim([6, -1, -1, 6], obstacles=[]))


# Example 1:
#
# Input: commands = [4,-1,3], obstacles = []
# Output: 25
# Explanation: The robot starts at (0, 0):
# 1. Move north 4 units to (0, 4).
# 2. Turn right.
# 3. Move east 3 units to (3, 4).
# The furthest point the robot ever gets from the origin is (3, 4), which squared is 3^2 + 4^2 = 25 units away.

# Example 2:
#
# Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# Output: 65
# Explanation: The robot starts at (0, 0):
# 1. Move north 4 units to (0, 4).
# 2. Turn right.
# 3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
# 4. Turn left.
# 5. Move north 4 units to (1, 8).
# The furthest point the robot ever gets from the origin is (1, 8), which squared is 1^2 + 8^2 = 65 units away.

# Example 3:
#
# Input: commands = [6,-1,-1,6], obstacles = []
# Output: 36
# Explanation: The robot starts at (0, 0):
# 1. Move north 6 units to (0, 6).
# 2. Turn right.
# 3. Turn right.
# 4. Move south 6 units to (0, 0).
# The furthest point the robot ever gets from the origin is (0, 6), which squared is 6^2 = 36 units away.
