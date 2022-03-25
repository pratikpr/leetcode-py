def backspace_compare(str1, str2):
	i, j = len(str1)-1, len(str2)-1
	
	while i >= 0:
		count_bs_1 = 0
		count_bs_2 = 0
		while i >= 0 and str1[i] == '#':
			i -= 1
			count_bs_1 += 1
		while j >= 0 and str2[j] == '#':
			j -= 1
			count_bs_2 += 1
		i -= count_bs_1
		j -= count_bs_2
		
		if str1[i] != str2[j]:
			return "false"
		i -= 1
		j -= 1
		
	if j >= 0:
		return "false"
	
	return "true"

print(backspace_compare("xy#z", "xzz#"))
print(backspace_compare("xy#z", "xyz#"))
print(backspace_compare("xp#", "xyz##"))
print(backspace_compare("xywrrmp", "xywrrmu#p"))