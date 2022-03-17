def non_repeat_substring(str):
	start = 0
	max_length = 0
	end = 0
	freqs = {}
	
	while end < len(str):
		last = str[end]
		if last not in freqs:
			freqs[last] = 0
		freqs[last] += 1
		
		if freqs[last] > 1:
			while len(freqs) < end-start+1:
				first = str[start]
				freqs[first] -= 1
				if freqs[first] == 0:
					del freqs[first]
				start += 1
		max_length = max(max_length, end - start + 1)
		end += 1
	
	return max_length
		
str = "aabccbb"
print(non_repeat_substring(str))
