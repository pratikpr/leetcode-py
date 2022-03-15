def search_rotated_array(arr, element):
	return searchRotatedArray(arr, 0, len(arr)-1, element)

def searchRotatedArray(arr, lo, hi, e):
	mid = (lo + hi)//2
	
	if arr[mid] == e:
		return mid
	if lo > hi:
		return -1
	
	if arr[lo] < arr[mid]:
		# left half is sorted
		if arr[lo] <= e and arr[mid] > e:
			return searchRotatedArray(arr, lo, mid-1, e)
		else:
			return searchRotatedArray(arr, mid+1, hi, e)
		
	elif arr[mid] < arr[hi]:
		# right half is sorted
		if arr[mid] <= e and arr[hi] > e:
			return searchRotatedArray(arr, mid+1, hi, e)
		else:
			return searchRotatedArray(arr, lo, mid-1, e)
			
	elif arr[hi] == arr[mid]:
		# repeated elements
		if arr[mid] != arr[lo]:
			return searchRotatedArray(arr, lo, mid-1, e)
		else:
			result = searchRotatedArray(arr, lo, mid-1, e)
			if result == -1:
				return searchRotatedArray(arr, mid+1, hi, e)
			else:
				return result
			
	return -1
	
	
arr = [7, 8, 9, 0, 3, 5, 6]
print(search_rotated_array(arr, 3))