# May LeetCoding Challenge - Day 9
# Valid Perfect Square - 367. Valid Perfect Square
# Difficulty - Easy
# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/
# https://leetcode.com/problems/valid-perfect-square/

# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1: Input: 16
# Output: true

# Example 2: Input: 14
# Output: false

def isPerfectSquare(num: int) -> bool: 
    return True if num**.5 == int(num**.5) else False

# Submission Detail
# 68 / 68 test cases passed.
# Status: Accepted
# Runtime: 24 ms / 32 ms / 28 ms
# Memory Usage: 13.8 MB / 13.9 MB / 13.8 MB
# Your runtime beats 92.05 % / 46.70 % / 75.96 %  of python3 submissions.

print(isPerfectSquare(16))
print(isPerfectSquare(14))