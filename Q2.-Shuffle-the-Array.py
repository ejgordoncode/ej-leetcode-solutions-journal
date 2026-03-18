1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3        ans = []
4        x_index = 0
5        for x_index in range(n):
6            ans.extend([nums[x_index], nums[x_index + n]])
7        return ans
8