import math


def triplet_sum_close_to_target(arr, target_sum):
	arr.sort()
	smallest_diff = math.inf
	
	for i in range(len(arr)-2):
		left = i + 1
		right = len(arr) - 1
		while left < right:
			diff = target_sum - (arr[i] + arr[left] + arr[right])
			if abs(diff) < abs(smallest_diff) or (abs(diff) == abs(smallest_diff) and diff > smallest_diff):
				smallest_diff = diff
				
			if diff > 0:
				left += 1
			else:
				right -= 1
				
	return target_sum - smallest_diff

def main():
	print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
	print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
	print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()