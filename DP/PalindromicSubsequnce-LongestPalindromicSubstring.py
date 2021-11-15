'''
Given a string, find the length of its Longest Palindromic Substring (LPS)
'''

def find_LPS_length(st):
    n = len(st)
    dp = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    maxLength = 1
    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            if st[start] == st[end]:
                if end-start == 1 or dp[start+1][end-1]:
                    dp[start][end] = True
                    maxLength = max(maxLength, end-start+1)
    return maxLength

def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()