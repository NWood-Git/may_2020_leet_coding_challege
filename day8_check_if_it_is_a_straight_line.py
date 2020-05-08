# May LeetCoding Challenge - Day 8
# Check If It Is a Straight Line - 1232. Check If It Is a Straight Line
# Difficulty - Easy
# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/
# https://leetcode.com/problems/check-if-it-is-a-straight-line/

# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] 
# represents the coordinate of a point. Check if these points make a straight line in the XY plane.

# Note: There are images of graphs on te website

# Example 1: Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

# Example 2: Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false

def checkStraightLine(coordinates) -> bool:
    len_coordinates = len(coordinates)
    if len_coordinates == 0:
        return False
    elif len_coordinates == 1 or len_coordinates == 2:
        return True

    m = None
    for i in range(len_coordinates-2):
        numerator = coordinates[i+1][1] - coordinates[i][1]
        denominator = coordinates[i+1][0] - coordinates[i][0] 
        if denominator == 0:
            return False
        slope =  numerator / denominator
        if m == None:
            m = slope
        else:
            if m != slope:
                return False
    return True


# Submission Detail
# 66 / 66 test cases passed.
# Status: Accepted
# Runtime: 56 ms / 64 ms / 56 ms
# Memory Usage: 13.9 MB / 14.2 / 14 MB
# Your runtime beats 92.34 % / 52.57 % / 92.34 % of python3 submissions.


print(checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))