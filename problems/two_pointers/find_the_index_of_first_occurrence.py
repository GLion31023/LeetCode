def index_of_first_occurrence(haystack: str, needle: str) -> int:
    left, right, target_i = 0, 0, 0

    while right <= len(haystack) - 1:
        if haystack[right] == needle[target_i]:
            right += 1
            target_i += 1
            if target_i == len(needle):
                return left
        else:
            target_i = 0
            left += 1
            right = left

    return - 1


print(index_of_first_occurrence("sadbutsad", "sad"))
print(index_of_first_occurrence("leetcode", "leeto"))
print(index_of_first_occurrence("azsumbglove", "bglove"))
print(index_of_first_occurrence("mississippi", "issip"))
