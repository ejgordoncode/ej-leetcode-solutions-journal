1class Solution:
2    def buildArray(self, target: List[int], n: int) -> List[str]:
3        s = deque() # stack s
4        operations = [] # pushes and pops taken to get to target
5        i = 0
6        current_stream_element = 0
7        for num in range(1,n+1):
8            operations.append("Push")
9            
10            if num != target[i]:
11                operations.append("Pop")
12            else:
13                i += 1
14
15            if num == target[-1]:
16                return operations
17            
18
19
20            
21            
22
23            
24        
25        