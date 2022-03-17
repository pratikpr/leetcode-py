import math


def smallest_subarray_sum(s, arr):
	start = 0
	end = 0
	min_len = math.inf
	sum = 0
	
	while end < len(arr):
		sum += arr[end]
		while sum >= s:
			min_len = min(min_len, end-start+1)
			sum -= arr[start]
			start += 1
		end += 1
	if min_len == math.inf:
		return 0
	return min_len
	
s = 8
arr = [3, 4, 1, 1, 6]
print(smallest_subarray_sum(s, arr))
