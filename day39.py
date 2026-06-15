#dynamic programming -Fibnacci
def fibonacci(n):
    dp = [0,1]

    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])

    return dp[n]

#Breadth First Search – BFS
from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])

    while q:
        node = q.popleft()
        print(node)

        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                q.append(n)
#Depth First Search
def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node)
        visited.add(node)

        for n in graph[node]:
            dfs(graph, n, visited)
#Queue Implementation
from collections import deque

q = deque()

q.append(1)
q.append(2)

print(q.popleft())            

#Stack Implementation

stack = []

stack.append(10)
stack.append(20)

print(stack.pop())

#Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    
    while left <= right:
        mid = (left + right)//2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
            
    return -1

#Linear Search
nums = [2, 5, 7, 9]

for n in nums:
    if n == 7:
        print("Found")

#Check Palindrome

word = "level"

if word == word[::-1]:
    print("Palindrome")

#Find Maximum in a List

nums = [4, 9, 2, 7]
print(max(nums))

#Reverse a String
s = "python"
print(s[::-1])