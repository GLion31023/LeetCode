from collections import defaultdict


def most_common_word(paragraph: str, banned: list[str]) -> str:
    for c in "!?',;.":
        paragraph = paragraph.replace(c, ' ')

    words = paragraph.lower().split()
    counter = defaultdict(int)
    for w in words:
        if w not in banned:
            counter[w] += 1

    return max(counter, key=counter.get)


print(most_common_word(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"]))
print(most_common_word(paragraph="a.", banned=[]))
print(most_common_word(paragraph="Bob", banned=[]))
print(most_common_word(paragraph="Bob. hIt, baLl", banned=["bob", "hit"]))
