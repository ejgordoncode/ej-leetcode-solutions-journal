1class Solution:
2    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
3        frequencies = [0] * 101
4        summation = 0
5        i = 0
6        j = 0
7        temp_sum = 0
8        for num in nums:
9            frequencies[num] += 1
10        for i in range(101):
11            temp_sum = frequencies[i]
12            frequencies[i] = summation
13            summation += temp_sum
14        for j in range(len(nums)):
15            nums[j] = frequencies[nums[j]]
16
17
18        return nums
19