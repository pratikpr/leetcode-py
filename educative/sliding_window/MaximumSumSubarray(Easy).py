def max_sub_array_of_size_k(k, arr):
	if k == 0:
		return 0
	curr_sum = 0;
	max_sum = 0
	start_window = 0;
	end_window = 0
	for i in range(len(arr)):
		if end_window < start_window + k:
			curr_sum += arr[end_window]
			max_sum = curr_sum
			end_window += 1
		elif end_window < len(arr):
			curr_sum = curr_sum - arr[start_window] + arr[end_window]
			max_sum = max(curr_sum, max_sum)
			start_window += 1
			end_window += 1
	
	return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sub_array_of_size_k(k, arr))