'''
Given a string, find the minimum number of characters that we can remove to make it a palindrome.
'''

def find_minimum_deletions(st):
    n = len(st)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            if st[start] == st[end]:
                dp[start][end] = 2 + dp[start+1][end-1]
            else:
                dp[start][end] = max(dp[start][end-1], dp[start+1][end])

    return n-dp[0][n-1]

def main():
    print(find_minimum_deletions("abdbca"))
    print(find_minimum_deletions("cddpd"))
    print(find_minimum_deletions("pqr"))

main()