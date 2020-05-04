# May LeetCoding Challenge - Day 4
# Number Complement - 476. Number Complement
# Difficulty - Easy
# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/
# https://leetcode.com/problems/number-complement/

# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

# Example 1: Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

# Example 2: Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

# Note:
# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.
# This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/

# Note: Normally I'd put the helper functions outside the main functions
# but i did it this way for leetcode

def findComplement(num: int) -> int:
    def int_to_binary(x):
        bin_list = []
        quotient = x
        while quotient >= 1:
            if quotient > 1:
                remainder = quotient % 2
                quotient = quotient // 2
                bin_list.insert(0, remainder)
            elif quotient == 1:
                bin_list.insert(0,1)
                quotient = 0
        
        return [0] if bin_list == [] else bin_list

    def bin_list_to_int(bin_list):
        complement_int = 0
        for num in bin_list:
            complement_int = ((2 * complement_int) + num) 
        return complement_int


    binary_num_list = int_to_binary(num)
    complement_list = []
    for num in binary_num_list:
        if num == 1:
            complement_list.append(0)
        elif num == 0:
            complement_list.append(1)
    return bin_list_to_int(complement_list)


print(findComplement(5))
print(findComplement(1))

# Submission Detail
# 149 / 149 test cases passed.
# Status: Accepted
# Runtime: 28 ms / 32 ms / 28 ms
# Memory Usage: 13.9 MB / 13.8 MB / 14 MB
# Your runtime beats 71.18 % / 37.10 % / 71.18 % of python3 submissions.








# Checks for helper function
# print(int_to_binary(5))
# print(bin_list_to_int(int_to_binary(5)))
# print(int_to_binary(13))
# print(bin_list_to_int(int_to_binary(13)))
# print(int_to_binary(12))
# print(bin_list_to_int(int_to_binary(12)))
# print(bin_list_to_int([1,0,1,1]))

# # for i in range(17):
# #     print(i, int_to_binary(i))