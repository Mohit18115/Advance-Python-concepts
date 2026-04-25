# 1. Two Sum (return indices)
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return []

print(two_sum([2,7,11,15], 9))


# 2. Longest Substring Without Repeating Characters
def longest_substring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

print(longest_substring("abcabcbb"))


# 3. Move Zeros to End
def move_zeros(nums):
    result = [n for n in nums if n != 0]
    result += [0] * nums.count(0)
    return result

print(move_zeros([0,1,0,3,12]))


# 4. First Non-Repeating Character
def first_unique(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None

print(first_unique("aabbcde"))


# 5. Rotate Array by K Steps
def rotate(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

print(rotate([1,2,3,4,5], 2))


# 6. Group Anagrams
from collections import defaultdict

def group_anagrams(words):
    d = defaultdict(list)
    for w in words:
        key = ''.join(sorted(w))
        d[key].append(w)
    return list(d.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))


# 7. Valid Parentheses
def valid_parentheses(s):
    stack = []
    mapping = {')':'(', ']':'[', '}':'{'}

    for ch in s:
        if ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return not stack

print(valid_parentheses("()[]{}"))


# 8. Product of Array Except Self
def product_except_self(nums):
    res = [1]*len(nums)

    left = 1
    for i in range(len(nums)):
        res[i] = left
        left *= nums[i]

    right = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= right
        right *= nums[i]

    return res

print(product_except_self([1,2,3,4]))


# 9. Merge Intervals
def merge_intervals(intervals):
    intervals.sort()
    res = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= res[-1][1]:
            res[-1][1] = max(res[-1][1], end)
        else:
            res.append([start, end])

    return res

print(merge_intervals([[1,3],[2,6],[8,10]]))


# 10. Number of Islands (DFS)
def num_islands(grid):
    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count

grid = [
    ['1','1','0','0'],
    ['1','0','0','1'],
    ['0','0','1','1']
]

print(num_islands(grid))