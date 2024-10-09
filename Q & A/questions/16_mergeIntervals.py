# You are given an array of intervals, where each interval is represented as a list of two integers [start, end],
# where start is less than or equal to end.
# Merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]
# Explanation: Intervals [1, 3] and [2, 6] overlap, so they are merged into [1, 6].

# Input: intervals = [[1, 4], [4, 5]]
# Output: [[1, 5]]
# Explanation: Intervals [1, 4] and [4, 5] are considered overlapping and merged into [1, 5].

# constraints:
# 1 <= len(intervals) <= 10^4
# intervals[i].length == 2
# 0 <= intervals[i][0] <= intervals[i][1] <= 10^4

# Sort the intervals by the starting values.
# Initialize an empty result list.
# Iterate through the sorted intervals and merge them if overlapping or add them to the result otherwise.

def merge_intervals(intervals):


    return merged
