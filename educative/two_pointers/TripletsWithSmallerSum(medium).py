def triplet_with_smaller_sum(arr, target):
	arr.sort()
	count = 0
	for i in range(len(arr)):
		l = i + 1
		r = len(arr) - 1
		while l < r:
			sum = arr[i] + arr[l] + arr[r]
			if sum >= target:
				r -= 1
			else:
				count += (r - l)
				l += 1
	
	return count


def main():
	print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
	print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()
