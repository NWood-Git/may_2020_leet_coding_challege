# May LeetCoding Challenge - Day 1
# First Bad Version - 278. First Bad Version
# Difficulty - Easy
# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/
# https://leetcode.com/problems/first-bad-version/

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Example: Given n = 5, and version = 4 is the first bad version.

# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true

# Then 4 is the first bad version. 

####NOTE: The API function doesn't work because it is from leetcode
####NOTE

def version_list(n):
    '''n is the last version number'''
    from random import randint
    is_bad_v_list = []
    x = randint(1, n)
    print(f"The first bad version is {x}.")
    for num in range(n+1):
        if num < x:
            is_bad_v_list.append(False)
        else:
            is_bad_v_list.append(True)
    return is_bad_v_list


def isBadVersion(i, v_list):
    return v_list[i]
    


def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    v_list = version_list(n)
    
    start = 1
    end = n
    
    if isBadVersion(1, v_list) == True:
        return 1            
    elif isBadVersion(n, v_list) == False:
        return None
    
    while True:
        mid1 = (start + end) // 2
        mid2 = mid1 + 1
        
        if isBadVersion(mid1, v_list) == isBadVersion(mid2, v_list) == False:
            start  = mid2 + 1
        elif isBadVersion(mid1,v_list) == isBadVersion(mid2, v_list) == True:
            end  = mid1 - 1 
        elif isBadVersion(mid1, v_list) == False and isBadVersion(mid2, v_list) == True:
            return mid2


print(f"Result: {firstBadVersion(25)} is the bad version.")
print(f"Result: {firstBadVersion(100)} is the bad version.")
print(f"Result: {firstBadVersion(10)} is the bad version.")



# Submission Detail
# 22 / 22 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 14 MB
# Your runtime beats 31.15 % of python3 submissions.


# 22 / 22 test cases passed.
# Status: Accepted
# Runtime: 24 ms / 24 ms
# Memory Usage: 13.9 MB / 13.7 MB
# Your runtime beats 89.22 % of python3 submissions.
# Your runtime beats 89.22 % of python3 submissions


#### Code as put into LeetCode:
'''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        
        if isBadVersion(1) == True:
            return 1            
        elif isBadVersion(n) == False:
            return None
        
        while True:
            mid1 = (start + end) // 2
            mid2 = mid1 + 1
            
            if isBadVersion(mid1) == isBadVersion(mid2) == False:
                start  = mid2 + 1
            elif isBadVersion(mid1) == isBadVersion(mid2) == True:
                end  = mid1 - 1 
            elif isBadVersion(mid1) == False and isBadVersion(mid2) == True:
                return mid2

'''


'''
# This is the simple slow version that exceeds the time limit

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    for i in range(n+1):
        if isBadVersion(i) == True:
            return i
'''

