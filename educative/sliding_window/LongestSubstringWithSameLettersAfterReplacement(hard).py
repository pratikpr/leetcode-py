def length_of_longest_substring(str1, k):
	start, end = 0, 0
	max_repeating_letter = 0
	max_length = 0
	freqs = {}
	
	while end < len(str1):
		right = str1[end]
		if right not in freqs:
			freqs[right] = 0
		freqs[right] += 1
		max_repeating_letter = max(max_repeating_letter, freqs[right])
		
		if end-start+1-max_repeating_letter > k:
			left = str1[start]
			freqs[left] -= 1
			start += 1
		
		max_length = max(max_length, end-start+1)
		end += 1
		
	return max_length


str1 = "abccde"
k = 1
print(length_of_longest_substring(str1, k))
