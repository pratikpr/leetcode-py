def find_happy_number(num):
	slow, fast = num, num
	while True:
		slow = get_square_sum(slow)
		fast = get_square_sum(get_square_sum(fast))
		
		if slow == fast:
			break
	return slow == 1
		
		
def get_square_sum(num):
	_sum = 0
	while num > 0:
		digit = (num % 10)
		_sum += (digit * digit)
		num //= 10
	return _sum


print(find_happy_number(23))
print(find_happy_number(12))
