class Revision_LCS:
	def lcs(self, s1, s2):
		dp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
		
		max_len = 0
		for i in range(len(s1)+1):
			for j in range(len(s2)+1):
				if s1[i-1] == s2[j-1]:
					dp[i][j] = 1 + dp[i-1][j-1]
					max_len = max(max_len, dp[i][j])
					
		return max_len
	
obj = Revision_LCS()
s1 = "www.educative.io/explore"
s2 = "educative.io/edpresso"
s3 = "0abc321"
s4 = "123abcdef"
print(obj.lcs(s1, s2))
print(obj.lcs(s3, s4))
