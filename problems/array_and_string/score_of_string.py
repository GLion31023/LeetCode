def score_of_string(s: str) -> int:
    scores = [ord(x) for x in s]
    abs_v = 0
    for i in range(len(s) - 1):
        abs_v += abs(scores[i] - scores[i + 1])

    return abs_v


print(score_of_string("hello"))
print(score_of_string("zaz"))


# Example 1:
# Input: s = "hello"
# Output: 13
# Explanation:
# The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111.
# So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

# Example 2:
#
# Input: s = "zaz"
# Output: 50
# Explanation:
# The ASCII values of the characters in s are: 'z' = 122, 'a' = 97.
# So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.
