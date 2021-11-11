def can_partition(num):
    s = sum(num)
    n = len(num)
    dp = [[False for x in range((s//2)+1)] for y in range(n)]

    for i in range(n):
        dp[i][0] = True

    for j in range((s//2)+1):
        dp[0][j] = num[0] == j

    for i in range(n):
        for j in range((s//2)+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif num[i] <= j:
                dp[i][j] = dp[i-1][j-num[i]]

    s1 = 0
    for i in range(s//2, -1, -1):
        if dp[n-1][i]:
            s1 = i
            break
    s2 = s-s1
    return abs(s1-s2)

print("Can partition: " + str(can_partition([1, 2, 3, 9])))
print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
print("Can partition: " + str(can_partition([1, 3, 100, 4])))