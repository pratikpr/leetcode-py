'''
There are n houses built in a line. A thief wants to steal the maximum possible money from these houses.
The only restriction the thief has is that he can’t steal from two consecutive houses, as that would alert the
security system. How should the thief maximize his stealing?
'''
def rob(wealth):
    n = len(wealth)
    if n == 0:
        return 0
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = wealth[0]

    for i in range(1, n):
        dp[i+1] = max(dp[i-1] + wealth[i], dp[i])

    return dp[-1]

def main():

  print(rob([1,2,3,1]))
  print(rob([2, 10, 14, 8, 1]))


main()