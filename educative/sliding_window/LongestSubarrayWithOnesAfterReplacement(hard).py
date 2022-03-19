def length_of_longest_substring(arr, k):
	start, end = 0, 0
	max_length = 0
	max_ones = 0
	
	while end < len(arr):
		if arr[end] == 1:
			max_ones += 1
			
		if end-start+1 - max_ones > k:
			if arr[start] == 1:
				max_ones -= 1
			start += 1
		max_length = max(max_length, end-start+1)
		end += 1
		
	return max_length


arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
k = 3
print(length_of_longest_substring(arr, k))