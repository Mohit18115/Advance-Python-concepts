# 1. Longest Palindromic Substring
def longest_palindrome(s):
    res = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            temp = s[i:j+1]
            if temp == temp[::-1] and len(temp) > len(res):
                res = temp
    return res

print(longest_palindrome("babad"))


# 2. Trapping Rain Water
def trap(height):
    left, right = 0, len(height)-1
    left_max = right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))


# 3. Word Break
def word_break(s, wordDict):
    dp = [False]*(len(s)+1)
    dp[0] = True

    for i in range(1, len(s)+1):
        for w in wordDict:
            if i >= len(w) and dp[i-len(w)] and s[i-len(w):i] == w:
                dp[i] = True

    return dp[-1]

print(word_break("leetcode", ["leet","code"]))


# 4. Longest Consecutive Sequence
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for n in num_set:
        if n-1 not in num_set:
            length = 1
            while n+length in num_set:
                length += 1
            longest = max(longest, length)

    return longest

print(longest_consecutive([100,4,200,1,3,2]))


# 5. LRU Cache (Simplified)
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
            return val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.cap:
            self.cache.pop(next(iter(self.cache)))
        self.cache[key] = value


# 6. Kth Smallest Element in Matrix
import heapq

def kth_smallest(matrix, k):
    flat = []
    for row in matrix:
        flat.extend(row)
    return heapq.nsmallest(k, flat)[-1]

print(kth_smallest([[1,5,9],[10,11,13],[12,13,15]], 3))


# 7. Course Schedule (Cycle Detection)
def can_finish(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}

    for a, b in prerequisites:
        graph[a].append(b)

    visiting = set()

    def dfs(node):
        if node in visiting:
            return False
        if not graph[node]:
            return True

        visiting.add(node)
        for nei in graph[node]:
            if not dfs(nei):
                return False
        visiting.remove(node)
        graph[node] = []
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False
    return True

print(can_finish(2, [[1,0]]))


# 8. Subarray Sum Equals K
def subarray_sum(nums, k):
    prefix = 0
    count = 0
    d = {0:1}

    for n in nums:
        prefix += n
        if prefix - k in d:
            count += d[prefix - k]
        d[prefix] = d.get(prefix, 0) + 1

    return count

print(subarray_sum([1,1,1], 2))


# 9. Top K Frequent Elements
from collections import Counter

def top_k(nums, k):
    count = Counter(nums)
    return [n for n,_ in count.most_common(k)]

print(top_k([1,1,1,2,2,3], 2))


# 10. Decode Ways
def num_decodings(s):
    if not s or s[0] == '0':
        return 0

    dp = [0]*(len(s)+1)
    dp[0] = dp[1] = 1

    for i in range(2, len(s)+1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]

    return dp[-1]

print(num_decodings("226"))