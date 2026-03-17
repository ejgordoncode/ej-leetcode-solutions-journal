1class Solution:
2    def findErrorNums(self, nums: List[int]) -> List[int]:
3
4        n = len(nums)
5
6        desired_sum = n * (n + 1) // 2
7        desired_sum_sq = n * (n+1) * ((2 * n) + 1) //6 # sum of digits from 1 to n inclusive
8
9        actual_sum = sum(nums)
10        actual_sum_sq = sum(num*num for num in nums)
11        sum_diff = actual_sum - desired_sum # (x - y)
12        sum_diff_sq = actual_sum_sq - desired_sum_sq # (x^2 - y^2)
13        x_plus_y = sum_diff_sq // sum_diff # (x + y)
14        missing = (x_plus_y - sum_diff) // 2 # (x + y - (x - y))/2 = y
15        duplicate = (x_plus_y + sum_diff) // 2 # (x + y + x - y) = x
16        return [duplicate, missing]
17        
18    