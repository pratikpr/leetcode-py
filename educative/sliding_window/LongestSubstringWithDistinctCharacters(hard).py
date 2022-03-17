def non_repeat_substring(str):
	start = 0
	max_length = 0
	end = 0
	freqs = {}
	
	while end < len(str):
		last = str[end]
		if last in freqs:
			start = max(start, freqs[last] + 1)
		freqs[last] = end
		max_length = max(max_length, end-start+1)
		end += 1
	
	return max_length
		
str = "abccde"
print(non_repeat_substring(str))
