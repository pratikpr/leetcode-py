class MinimumSubsetSumDiff:

    def can_partition(self, num):
        s = sum(num)
        n = len(num)
        dp = [[False for x in range(int(s/2)+1)] for y in range(n)]

        for i in range(n):
            dp[i][0] = True

        for j in range(1, int(s/2)+1):
            dp[0][j] = (num[0] == j)

        for i in range(1, n):
            for j in range(1, int(s/2)+1):
                if dp[i-1][j]:
                    dp[i][j] = True
                elif j >= num[i]:
                    dp[i][j] = dp[i-1][j - num[i]]

        s1 = 0
        #largest index in the last row that is true
        for i in range(int(s/2), -1, -1):
            if dp[n-1][i]:
                s1 = i
                break

        s2 = s-s1
        return abs(s2-s1)

obj = MinimumSubsetSumDiff()
num = [1, 3, 100, 4]
print(obj.can_partition(num))