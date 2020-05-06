# May LeetCoding Challenge - Day 6
# Majority Element - 169. Majority Element
# Difficulty - Easy
# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/
# https://leetcode.com/problems/majority-element/

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1: Input: [3,2,3]
# Output: 3

# Example 2: Input: [2,2,1,1,1,2,2]
# Output: 2

def majorityElement(nums: [int]) -> int:
    import collections
    num_count = collections.Counter(nums)
    for k,v in num_count.items():
        if v > len(nums)/2:
            return k

# Submission Detail
# 46 / 46 test cases passed.
# Status: Accepted
# Runtime: 168 ms / 172 ms
# Memory Usage: 15.2 MB / 15 MB
# Your runtime beats 89.32 % of python3 submissions./
# Your runtime beats 79.28 % of python3 submissions.


print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))
