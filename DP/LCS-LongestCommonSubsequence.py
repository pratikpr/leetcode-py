'''
Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence which is common in both the strings
'''
def find_LCS_length(s1, s2):
    n1, n2 = len(s1), len(s2)
    maxLength = 0
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            maxLength = max(dp[i][j], maxLength)

    return maxLength

def main():
  print(find_LCS_length("abdca", "cbda"))
  print(find_LCS_length("passport", "ppsspt"))


main()
