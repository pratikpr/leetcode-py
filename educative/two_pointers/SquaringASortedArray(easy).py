def make_squares(arr):
	squares = []
	
	i, j = 0, len(arr) - 1
	
	while i <= j:
		if arr[i] * arr[i] > (arr[j] * arr[j]):
			squares.insert(0, arr[i] * arr[i])
			i += 1
		else:
			squares.insert(0, arr[j] * arr[j])
			j -= 1

	return squares

def main():

	print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
	print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
