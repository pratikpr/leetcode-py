class SubsetSum:
    '''
    Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.
    '''

    def can_partition(self, num, sum):
        n = len(num)
        dp = [[False for x in range(sum+1)] for y in range(n)]

        # empty set
        for i in range(n):
            dp[i][0] = True

        # only one number present
        for s in range(1, sum+1):
            dp[0][s] = True if num[0] == s else False

        for i in range(1, n):
            for s in range(1, sum+1):
                if dp[i-1][s]:
                    dp[i][s] = True
                elif s >= num[i]:
                    dp[i][s] = dp[i-1][s-num[i]]

        return dp[n-1][sum]


obj = SubsetSum()
nums = [1,3,4,8]
sum = 6
print(obj.can_partition(nums, sum))