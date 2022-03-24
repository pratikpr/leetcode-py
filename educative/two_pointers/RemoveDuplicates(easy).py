def remove_duplicates(arr):
	# index of the next non-duplicate element
	next_non_duplicate = 0
	
	i = 1
	while (i < len(arr)):
		# if arr[next_non_duplicate - 1] != arr[i]:
		#   arr[next_non_duplicate] = arr[i]
		#   next_non_duplicate += 1
		# i += 1
		while i < len(arr) and arr[i] == arr[next_non_duplicate]:
			i += 1
		if i == len(arr):
			break
		next_non_duplicate += 1
		arr[next_non_duplicate], arr[i] = arr[i], arr[next_non_duplicate]
		i += 1
	
	return next_non_duplicate + 1


def main():
	print(remove_duplicates([1]))
	print(remove_duplicates([2, 2, 2, 11]))


main()
