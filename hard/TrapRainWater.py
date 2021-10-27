from typing import List

'''
https://leetcode.com/problems/trapping-rain-water/
Given n non-negative integers representing an elevation map where the width 
of each bar is 1, compute how much water it can trap after raining.
'''
class TrapRainWater:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        if size == 0:
            return 0

        left_max = list(); right_max = []

        left_max.insert(0, height[0])

        for i in range(1, size):
            left_max.insert(i, max(height[i], left_max[i-1]))

        right_max.append(height[size-1])
        for i in range(1, size):
            # print(i)
            right_max.append(max(height[size-i-1], right_max[i-1]))
        right_max.reverse()

        ans = 0
        for i in range(1, size-1):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans

obj = TrapRainWater()
height = [4,2,0,3,2,5]
print(obj.trap(height))