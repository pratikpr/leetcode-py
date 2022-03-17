def longest_substring_with_k_distinct(str1, k):
	freq = {}
	start = 0;
	end = 0
	max_length = 0
	
	while end < len(str1):
		last = str1[end]
		if last not in freq:
			freq[last] = 0
		freq[last] += 1
		
		while len(freq) > k:
			first = str1[start]
			freq[first] -= 1
			if freq[first] == 0:
				del freq[first]
			start += 1
		max_length = max(max_length, end - start + 1)
		end += 1
	
	return max_length


str1 = "cbebbi"
k = 3
print(longest_substring_with_k_distinct(str1, k))
