# May LeetCoding Challenge - Day 2
# Jewels and Stones - 771. Jewels and Stones
# Difficulty - Easy
# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/
# https://leetcode.com/problems/jewels-and-stones/

# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1: Input: J = "aA", S = "aAAbbbb"
# Output: 3

# Example 2: Input: J = "z", S = "ZZ"
# Output: 0

# Note: S and J will consist of letters and have length at most 50.
# The characters in J are distinct.


def numJewelsInStones(J: str, S: str) -> int:
    num_of_j_in_s = 0

    for i in S:
        if i in J:
            num_of_j_in_s += 1

    return num_of_j_in_s

# Submission Detail
# 254 / 254 test cases passed.
# Status: Accepted
# Runtime: 24 ms/ 24 ms
# Memory Usage: 14 MB /14 MB
# Your runtime beats 89.93 % of python3 submissions./
# Your runtime beats 89.93 % of python3 submissions.

'''
def numJewelsInStones(J: str, S: str) -> int:
    jewel_set = set(J)
    num_of_j_in_s = 0

    for i in S:
        if i in jewel_set:
            num_of_j_in_s += 1

    return num_of_j_in_s

# Submission Detail
# 254 / 254 test cases passed.
# Status: Accepted
# Runtime: 60 ms / 52ms / 24 ms / 44 ms
# Memory Usage: 13.7 MB / 14 MB / 13.9 MB / 14 MB
# Greater than runtime distribution / 
# Your runtime beats 5.31 % of python3 submissions./
# Your runtime beats 89.93 % of python3 submissions./
# Your runtime beats 6.71 % of python3 submissions.
'''

J = "aA"
S = "aAAbbbb"
print(numJewelsInStones(J,S))

J = "z"
S = "ZZ"
print(numJewelsInStones(J,S))