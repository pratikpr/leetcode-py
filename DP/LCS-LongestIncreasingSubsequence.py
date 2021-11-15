'''
Given a number sequence, find the length of its Longest Increasing Subsequence
'''
def find_LIS_length(nums):
    n = len(nums)
    maxLen = 1
    dp = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j]:
                dp[i] += 1
                maxLen = max(maxLen, dp[i])

    return maxLen

def main():
    # print(find_LIS_length([4, 2, 3, 6, 10, 1, 12]))
    print(find_LIS_length([-4, 10, 3, 7, 15]))

main()