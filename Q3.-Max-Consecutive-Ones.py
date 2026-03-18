1class Solution:
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        curr = maximum = 0
4        for num in nums:
5            if num == 1:
6                curr += 1
7            else:
8                if curr > maximum: maximum = curr
9                curr = 0
10        maximum = max(curr, maximum)
11        return maximum
12            
13        