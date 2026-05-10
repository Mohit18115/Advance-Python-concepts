#Two Sum (Hashing – Medium)
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target-n], i]
        seen[n] = i

print(two_sum([2,7,11,15], 9))

#Longest Substring Without Repeating (Sliding Window – Medium)
def longest_substring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right-left+1)

    return max_len

print(longest_substring("abcabcbb"))

#Container With Most Water (Two Pointer – Medium)
def max_area(height):
    l, r = 0, len(height)-1
    max_area = 0

    while l < r:
        area = min(height[l], height[r]) * (r-l)
        max_area = max(max_area, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area

print(max_area([1,8,6,2,5,4,8,3,7]))

#Group Anagrams (Hashing – Medium)
from collections import defaultdict

def group_anagrams(strs):
    d = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        d[key].append(word)
    return list(d.values())

print(group_anagrams(["eat","tea","tan","ate"]))

#Product of Array Except Self (Medium)
def product_except_self(nums):
    res = [1]*len(nums)

    left = 1
    for i in range(len(nums)):
        res[i] = left
        left *= nums[i]

    right = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= right
        right *= nums[i]

    return res

print(product_except_self([1,2,3,4]))

#Valid Parentheses (Stack – Medium)
def valid(s):
    stack = []
    m = {')':'(', ']':'[', '}':'{'}

    for ch in s:
        if ch in m:
            if not stack or stack[-1] != m[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return not stack

print(valid("()[]{}"))

#Number of Islands (DFS – Medium-Hard)

def num_islands(grid):
    def dfs(r,c):
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]=='0':
            return
        grid[r][c]='0'
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='1':
                dfs(i,j)
                count += 1

    return count

#Clone Graph (Graph – Hard)

def clone_graph(node):
    if not node:
        return None

    visited = {}

    def dfs(node):
        if node in visited:
            return visited[node]

        copy = Node(node.val)
        visited[node] = copy

        for n in node.neighbors:
            copy.neighbors.append(dfs(n))

        return copy

    return dfs(node)

#Kth Largest Element (Heap – Medium-Hard)

import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

print(kth_largest([3,2,1,5,6,4], 2))

#Word Ladder (BFS – Hard)

from collections import deque

def word_ladder(begin, end, word_list):
    word_set = set(word_list)
    q = deque([(begin,1)])

    while q:
        word, steps = q.popleft()
        if word == end:
            return steps

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new = word[:i] + c + word[i+1:]
                if new in word_set:
                    word_set.remove(new)
                    q.append((new, steps+1))
    return 0
