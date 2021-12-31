class DutchNationalFlag:
	def dutch_national_flag(self, arr):
		i, mid, j = 0, 0, len(arr)-1

		while mid <= j:
			if arr[mid] == 0:
				swap(arr, mid, i)
				mid += 1
				i += 1
			elif arr[mid] == 2:
				swap(arr, mid, j)
				j -= 1
			else:
				mid += 1


def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp


obj = DutchNationalFlag()
print("Before DNF")
arr = [2, 0, 0, 1, 2, 1]
print(arr)
print("After DNF")
obj.dutch_national_flag(arr)
print(arr)
