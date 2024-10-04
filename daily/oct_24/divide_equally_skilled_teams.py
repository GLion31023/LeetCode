def divide_players(skill: list[int]) -> int:
    total_sum = sum(skill)
    num_teams = len(skill) // 2

    if total_sum % num_teams != 0:
        return -1

    per_team = total_sum / num_teams
    sorted_skills = sorted(skill)

    s, e = 0, len(skill) - 1
    result = 0

    while s < e:
        if sorted_skills[s] + sorted_skills[e] != per_team:
            return -1
        result += (sorted_skills[s] * sorted_skills[e])
        s += 1
        e -= 1

    return result


print(divide_players([3, 2, 5, 1, 3, 4]))
print(divide_players([3, 4]))
print(divide_players([1, 1, 2, 3]))
print(divide_players([10, 14, 16, 15, 9, 4, 4, 4]))

# Example 1:
# Input: skill = [3,2,5,1,3,4]
# Output: 22
# Explanation:
# Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
# The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

# Example 2:
# Input: skill = [3,4]
# Output: 12
# Explanation:
# The two players form a team with a total skill of 7.
# The chemistry of the team is 3 * 4 = 12.

# Example 3:
# Input: skill = [1,1,2,3]
# Output: -1
# Explanation:
# There is no way to divide the players into teams such that the total skill of each team is equal.
