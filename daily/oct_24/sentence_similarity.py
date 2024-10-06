def are_similar(sentence1: str, sentence2: str) -> bool:
    s1 = sentence1.split()
    s2 = sentence2.split()

    if s1 == s2:
        return True

    lower = min(len(s1), len(s2))
    pre = suf = 0

    while pre < lower and s1[pre] == s2[pre]:
        pre += 1

    while suf < lower - pre and s1[len(s1) - 1 - suf] == s2[len(s2) - 1 - suf]:
        suf += 1

    return pre + suf >= lower


print(are_similar(sentence1="My name is Haley", sentence2="My Haley"))
print(are_similar(sentence1="of", sentence2="A lot of words"))
print(are_similar(sentence1="Eating right now", sentence2="Eating"))
print(are_similar(sentence1="Luky", sentence2="Lucccky"))
print(are_similar(sentence1="Are You Okay", sentence2="are you okay"))
print(are_similar(sentence1="CwFfRo regR", sentence2="CwFfRo H regR"))
print(are_similar(sentence1="eTUny i b R UFKQJ EZx JBJ Q xXz", sentence2="eTUny i R EZx JBJ xXz"))
print(are_similar(sentence1="a", sentence2="a aa a"))


# Example 1:
# Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
# Output: true
# Explanation:
# sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".
#
# Example 2:
# Input: sentence1 = "of", sentence2 = "A lot of words"
# Output: false
# Explanation:
# No single sentence can be inserted inside one of the sentences to make it equal to the other.
#
# Example 3:
# Input: sentence1 = "Eating right now", sentence2 = "Eating"
# Output: true
# Explanation:
# sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.
