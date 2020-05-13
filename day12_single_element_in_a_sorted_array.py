# May LeetCoding Challenge - Day 12
#  Single Element in a Sorted Array - 540. Single Element in a Sorted Array
# Difficulty - Medium
# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/
# https://leetcode.com/problems/single-element-in-a-sorted-array/

# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

# Example 1: Input: [1,1,2,3,3,4,4,8,8]
# Output: 2

# Example 2: Input: [3,3,7,7,10,11,11]
# Output: 10

# Note: Your solution should run in O(log n) time and O(1) space.

def singleNonDuplicate(nums):
    result = None
    for i in nums:
        if result == None:
            result = i
        elif i == result:
            result = None
        elif result != i:
            return result
    return result

# Submission Detail
# 12 / 12 test cases passed.
# Status: Accepted
# Runtime: 68 ms / 76 ms / 76 ms / 64 ms
# Memory Usage: 16 MB / 16 MB / 16.1 MB / 16.2 MB
# Your runtime beats 88.51 % / 46.36 % / 46.36 % / 96.93 % of python3 submissions.

print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(singleNonDuplicate([3,3,7,7,10,11,11]))