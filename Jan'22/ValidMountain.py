from typing import List


def validMountainArray(arr: List[int]) -> bool:
	l, r = 0, len(arr) - 1
	if len(arr) == 1:
		return False
	while l < len(arr) - 1 and arr[l] < arr[l + 1]:
		l += 1
	while r > 0 and arr[r] < arr[r - 1]:
		r -= 1
	if r == 0 or l == len(arr)-1:
		return False
	return l == r

arr = [0,1,2,3,4,5,6,7,8,9]
print(validMountainArray(arr))