# May LeetCoding Challenge - Day 10
# Find the Town Judge - 997. Find the Town Judge
# Difficulty - Easy
# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/
# https://leetcode.com/problems/find-the-town-judge/

# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

# Example 1: Input: N = 2, trust = [[1,2]]
# Output: 2

# Example 2: Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3

# Example 3: Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1

# Example 4: Input: N = 3, trust = [[1,2],[2,3]]
# Output: -1

# Example 5: Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3

# Note:
# 1 <= N <= 1000
# trust.length <= 10000
# trust[i] are all different
# trust[i][0] != trust[i][1]
# 1 <= trust[i][0], trust[i][1] <= N


def findJudge(N, trust):
    from numpy import zeros
    if len(trust) < N-1:
        return -1
    elif N == 1 and trust == []:
        return 1
    trust_list = zeros(N+1)

    for x in trust:
        trust_list[x[0]] -= 1
        trust_list[x[1]] += 1

    for i in range(len(trust_list)):
        if trust_list[i] == N-1:
            return i
    return -1

# Submission Detail
# 89 / 89 test cases passed.
# Status: Accepted
# Runtime: 1788 ms / 976 ms / 1500 ms
# Memory Usage: 34.2 MB / 34 MB / 34 MB
# Off the charts slow/
# Your runtime beats 15.84 % of python3 submissions./
# Your runtime beats 6.85 % of python3 submissions.



'''
def findJudge(N, trust):
    from numpy import zeros
    if len(trust) < N-1:
        return -1
    elif N == 1 and trust == []:
        return 1
    trust_list = list(zeros(N+1))

    for x in trust:
        trust_list[x[0]] -= 1
        trust_list[x[1]] += 1
    
    try:
        return trust_list.index(N-1)
    except ValueError:
        return -1
'''
# 89 / 89 test cases passed.
# Status: Accepted
# Runtime: 1752 ms / 940 ms / 1932 ms
# Memory Usage: 34.1 MB / 34 MB / 33.7 MB
# Off the charts slow /
# Your runtime beats 16.26 % of python3 submissions./
# Off the charts slow


print(findJudge(2,[[1,2]]))                          #  2
print(findJudge(3,[[1,3],[2,3]]))                    #  3
print(findJudge(3,[[1,3],[2,3],[3,1]]))              # -1
print(findJudge(3,[[1,2],[2,3]]))                    # -1
print(findJudge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]]))  #  3

'''
#744ms solution from leetcode
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        society_level = [0 for i in range(N)]
        suspicion_level = [0 for i in range(N)]

        for el in trust:
            society_level[el[1] - 1] += 1
            suspicion_level[el[0] - 1] += 1

        for i in range(N):
            if society_level[i] == N - 1:
                if suspicion_level[i] == 0:
                    return i + 1

        return -1
'''