from collections import defaultdict


def groupAnagrams(words):
	result = list()
	words_dict = defaultdict()
	
	for word in words:
		sorted_word = ''.join(sorted(word))
		if sorted_word not in words_dict:
			words_dict[sorted_word] = [word]
		else:
			words_dict[sorted_word].append(word)
	
	for word in words_dict:
		result.append(words_dict[word])
	
	return result


words = ["cat", "dog", "tac", "god", "act", "tom marvolo riddle ", "abc", "def", "cab", "fed", "clint eastwood ",
         "i am lord voldemort","elvis", "old west action", "lives"]
print(groupAnagrams(words))
