'''
The apple factory had a mixup when ordering labels, and now they are left with a whole bunch of letters they don't
need in the wrong order. Your boss needs to know how many apple baskets can be marked by salvaging the labels you do have.
Given a string as input, you need to return an integer representing the number of times that the word apple can be
spelled using each character a single time.
'''
import sys
from collections import defaultdict


def countApples(str):
    s = "apple"

    count = defaultdict()
    org = defaultdict()

    for c in s:
        if c not in org.keys():
            org[c] = 1
        else:
            org[c] += 1

    for c in str:
        if c not in count.keys():
            count[c] = 1
        else:
            count[c] += 1

    ans = sys.maxsize
    for c in s:
        if c in count.keys():
            ans = min(ans, count[c]//org[c])
        else:
            return 0

    return ans

str = input()
print(countApples(str))