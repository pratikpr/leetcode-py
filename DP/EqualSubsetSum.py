class EqualSubsetSumPartition:
    def can_partition(self, num):
        s = sum(num)
        if s % 2 != 0:
            return False

        s = int(s/2)

        n = len(num)
        dp = [[False for x in range(s+1)] for y in range(n)]

        # if sum = 0, it can be had by not including any elements
        for i in range(n):
            dp[i][0] = True

        #If there's only one element
        for i in range(s+1):
            dp[0][i] = num[0] == i

        for i in range(1, n):
            for j in range(1, s+1):
                if dp[i-1][j]:
                    dp[i][j] = dp[i-1][j]
                elif j >= num[i]:
                    dp[i][j] = dp[i-1][j-num[i]]

        return dp[n-1][s]

obj = EqualSubsetSumPartition()
num = [1,2,3,8]
print(obj.can_partition(num))