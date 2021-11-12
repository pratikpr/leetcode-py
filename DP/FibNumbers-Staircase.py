'''
Given a stair with ‘n’ steps, implement a method to count how many possible ways are there to reach the top of the staircase,
given that, at every step you can either take 1 step, 2 steps, or 3 steps.
'''
def count_ways(n):
    dp = [0 for _ in range(n+1)]

    dp[0] = 1; dp[1] = 1; dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]

def main():
  print(count_ways(3))
  print(count_ways(4))
  print(count_ways(5))


main()