from collections import Counter


def isSupermajority(count, ints):
    maj_threshold = (2*count/3)

    counts = Counter(ints)

    for i in counts.keys():
        if counts[i] > maj_threshold:
            return True

    return False

count = input()
ints = []
for i in range(int(count)):

    ints.append(int(input()))

# count = 3
# ints = [1,2,1]
print(isSupermajority(int(count), ints))