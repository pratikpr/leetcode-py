import sys


def hackerCards(collection, d):
    # Write your code here
    res = []
    print(sys.maxsize)
    start, end = 0, 0

    for i in range(0, len(collection) + 1):
        start = 1 if i == 0 else collection[i - 1] + 1
        end = collection[i] if i != len(collection) else sys.maxsize
        if d < start:
            break
        for j in range(start, end):
            if j <= d:
                res.append(j)
                d -= j
            else:
                break
    return res

hackerCards()