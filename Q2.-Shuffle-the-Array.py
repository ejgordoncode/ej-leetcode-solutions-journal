1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3        ans = [0] * 2 * n
4        x_index = 0
5        y_index = n
6        while x_index < n:
7            ans[x_index*2:x_index*2 + 2] = ([nums[x_index], nums[y_index]])
8            x_index += 1
9            y_index += 1
10        return ans
11