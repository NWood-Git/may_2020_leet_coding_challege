# May LeetCoding Challenge - Day 3
# Ransom Note - 383. Ransom Note
# Difficulty - Easy
# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/
# https://leetcode.com/problems/ransom-note/

# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note: You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

def canConstruct(ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine):
        return False
    
    mag_dict = {}

    for letter in magazine:
        if letter in mag_dict.keys():
            mag_dict[letter] += 1
        else:
            mag_dict[letter] = 1
    
    for letter in ransomNote:
        if letter in mag_dict.keys() and mag_dict[letter] != 0:
            mag_dict[letter] -= 1
        else:
            return False
    
    return True

# Submission Detail
# 126 / 126 test cases passed.
# Status: Accepted
# Runtime: 88 ms / 84 ms / 92 ms
# Memory Usage: 13.9 MB / 14 MB
# Your runtime beats 16.96 % / 19.52 % / 15.30 %  of python3 submissions./


'''
def canConstruct(ransomNote: str, magazine: str) -> bool:
    # if ransomNote == '' and magazine == '' :
    #     return True
    # elif ransomNote and magazine == '':
    #     return None
    if len(ransomNote) > len(magazine):
        return False
    
    mag_dict = {}

    for letter in magazine:
        if letter in mag_dict.keys():
            mag_dict[letter] += 1
        else:
            mag_dict[letter] = 1
    
    for letter in ransomNote:
        if letter in mag_dict.keys() and mag_dict[letter] != 0:
            mag_dict[letter] -= 1
        else:
            return False
    
    return True
'''
# Submission Detail
# 126 / 126 test cases passed.
# Status: Accepted
# Runtime: 92 ms / 84 ms / 76 ms / 96 ms
# Memory Usage: 14.2 MB / 14.1 MB / 13.9 MB / 14.1 MB
# Your runtime beats 15.30 % of python3 submissions./
# Your runtime beats 19.52 % of python3 submissions./
# Your runtime beats 25.71 % of python3 submissions./
# Your runtime beats 13.27 % of python3 submissions.


print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))

'''
# Fast 20 ms solution:
def canConstruct(ransomNote: str, magazine: str) -> bool:
    for item in ransomNote:
        if not item in magazine:
            return False
        magazine = magazine.replace(item, "", 1)
    return True

print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))
'''