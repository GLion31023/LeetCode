from collections import deque


def predict_party_victory(senate: str) -> str:
    radiant = deque()
    dire = deque()

    for i, s in enumerate(senate):
        if s == "R":
            radiant.append(i)
        else:
            dire.append(i)

    while radiant and dire:
        r = radiant.popleft()
        d = dire.popleft()

        if r < d:
            radiant.append(r + len(senate))
        else:
            dire.append(d + len(senate))

    return "Radiant" if radiant else 'Dire'


print(predict_party_victory("RD"))
print(predict_party_victory("RDD"))
print(predict_party_victory("DDRRR"))
