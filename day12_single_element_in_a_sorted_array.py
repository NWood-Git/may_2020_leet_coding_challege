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

# Faster Way - Do it with Binary Search

def singleNonDuplicate(nums):
    left = 0
    right = len(nums) -1

    while left < right:
        mid = (left+right) //2
        check_if_halves_are_even = (right - mid) % 2 == 0
        if nums[mid+1] == nums[mid]:
            if check_if_halves_are_even:
                left = mid + 2
            else:
                right = mid - 1
        elif nums[mid - 1] == nums[mid]:
            if check_if_halves_are_even:
                right = mid -2
            else:
                left = mid + 1
        else:
            return nums[mid]
    return nums[left]

# Submission Detail
# 12 / 12 test cases passed.
# Status: Accepted
# Runtime: 68 ms / 68 ms
# Memory Usage: 16 MB / 16.1 MB
# Your runtime beats 88.51 % / 88.51 % of python3 submissions.

'''
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
'''
# Submission Detail
# 12 / 12 test cases passed.
# Status: Accepted
# Runtime: 68 ms / 76 ms / 76 ms / 64 ms
# Memory Usage: 16 MB / 16 MB / 16.1 MB / 16.2 MB
# Your runtime beats 88.51 % / 46.36 % / 46.36 % / 96.93 % of python3 submissions.

print(singleNonDuplicate([1,1,2,3,3,4,4,8,8])) #2
print(singleNonDuplicate([3,3,7,7,10,11,11])) # 10
print(singleNonDuplicate([1,1,2,3,3,4,4,8,8])) #2
print(singleNonDuplicate([1, 1, 4, 4, 5, 5, 6, 8, 8])) #6