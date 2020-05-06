# May LeetCoding Challenge - Day 5
# First Unique Character in a String - 387. First Unique Character in a Stringe
# Difficulty - Easy
# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/
# https://leetcode.com/problems/first-unique-character-in-a-string/

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:
# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

# Note: You may assume the string contain only lowercase letters.

def firstUniqChar(s: str) -> int:
        import collections
        unqiue_indices = []
        for character in collections.Counter(s).keys():
            if collections.Counter(s)[character] == 1:
                unqiue_indices.append(s.index(character))
        
        return min(unqiue_indices) if unqiue_indices else -1 


# 104 / 104 test cases passed.
# Status: Accepted
# Runtime: 904 ms / 948 ms / 884 ms
# Memory Usage: 13.8 MB / 13.9 MB / 13.8 MB
# Your runtime beats 6.81 % / 6.74% / 6.96% of python3 submissions.

'''
def firstUniqChar(s: str) -> int:
        import collections
        return min([s.index(x) for x in collections.Counter(s).keys() if collections.Counter(s)[x] == 1])\
            if 1 in collections.Counter(s).values() else -1
'''

print(firstUniqChar('leetcode')) # -> 0
print(firstUniqChar('loveleetcode')) # -> 2