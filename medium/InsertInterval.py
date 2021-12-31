from typing import List

'''
https://leetcode.com/problems/insert-interval/
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals 
'''
class InsertInterval:
	def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
		start, end = newInterval
		idx, n = 0, len(intervals)
		result = []

		# the strat of the newinterval is after all the intervals whose starts are smaller than it
		while idx < n and intervals[idx][0] < start:
			result.append(intervals[idx])
			idx += 1

		# if there are no intervals or if tge end of the last added interval is lesser than the start of the new interval
		if not result or result[-1][1] < start:
			# non overlap between last element and new interval
			result.append(newInterval)
		else:
			#there is an overlap
			result[-1][1] = max(result[-1][1], end)

		# add remaining intervals and merge them if needed
		while idx < n:
			interval = intervals[idx]
			int_start, int_end = interval
			idx += 1

			if int_start > result[-1][1]:
				result.append(interval)
			else:
				result[-1][1] = max(result[-1][1], int_end)

		return result


obj = InsertInterval()
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

print(obj.insert(intervals, newInterval))