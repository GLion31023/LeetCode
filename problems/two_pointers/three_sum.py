def three_sum(nums: list[int]) -> list[list[int]]:
    triplets = []
    sorted_nums = nums.sort()

    

    # end = len(nums) - 1
    #
    # for i in range(end - 1):
    #     left = i + 1
    #     while left <= end - 1:
    #         right = left + 1
    #         while right <= end:
    #             if nums[i] + nums[left] + nums[right] == 0:
    #                 triplet = sorted([nums[i], nums[left], nums[right]])
    #                 if triplet not in triplets:
    #                     triplets.append(triplet)
    #             right += 1
    #         left += 1
    #
    # return triplets


print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([0, 1, 1]))
print(three_sum([0, 0, 0]))

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
