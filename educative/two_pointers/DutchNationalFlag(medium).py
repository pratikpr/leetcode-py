def dutch_flag_sort(arr):
	lo, hi = 0, len(arr)-1
	i = 0
	
	while i <= hi:
		if arr[i] == 0:
			arr[lo], arr[i] = arr[i], arr[lo]
			i += 1
			lo += 1
		elif arr[i] == 1:
			i += 1
		else:
			arr[hi], arr[i] = arr[i], arr[hi]
			hi -= 1
	
arr = [1, 0, 2, 1, 0]
print(arr)
dutch_flag_sort(arr)
print(arr)
print()
arr = [2, 2, 0, 1, 2, 0]
print(arr)
dutch_flag_sort(arr)
print(arr)