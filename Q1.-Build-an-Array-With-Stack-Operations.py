1class Solution:
2    def buildArray(self, target: List[int], n: int) -> List[str]:
3        operations = [] # pushes and pops taken to get to target
4        i = 0
5        current_stream_element = 0
6        for num in range(1,n+1): # range represents stream of ints from 1 to n inclusive
7            operations.append("Push")
8            
9            if num != target[i]:
10                operations.append("Pop")
11            else:
12                i += 1
13
14            if num == target[-1]:
15                return operations
16            
17
18
19            
20            
21
22            
23        
24        