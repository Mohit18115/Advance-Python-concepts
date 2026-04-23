#Two Pointer Pattern
#Question: Check if a string is a palindrome.
def is_palindrome(s):
    l, r = 0, len(s)-1

    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

print(is_palindrome("level"))

#Sliding Window (Fixed Size)
#Question: Find maximum sum of subarray of size k.
def max_sum(arr, k):
    window = sum(arr[:k])
    max_val = window

    for i in range(k, len(arr)):
        window += arr[i] - arr[i-k]
        max_val = max(max_val, window)

    return max_val

print(max_sum([2,1,5,1,3,2], 3))

#Hashing Pattern
#Check if array has duplicates
def has_duplicate(nums):
    seen = set()

    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

print(has_duplicate([1,2,3,1]))

#Frequency Count (Hash Map)
#Count frequency of characters.
def count_chars(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return freq

print(count_chars("apple"))

#Binary Search Pattern
#Find element in sorted array.
def search(arr, target):
    l, r = 0, len(arr)-1

    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid+1
        else:
            r = mid-1

    return -1

print(search([1,2,3,4,5], 4))

#Stack Pattern
#Check valid parentheses.

def valid(s):
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()

    return not stack

print(valid("()()"))

#Prefix Sum Pattern
#Find sum of elements between two indexes.

def prefix_sum(arr):
    prefix = [0]

    for n in arr:
        prefix.append(prefix[-1] + n)

    return prefix

arr = [1,2,3,4]
p = prefix_sum(arr)

# sum from index 1 to 3
print(p[4] - p[1])

#Greedy Pattern
#Max profit from stock prices
def max_profit(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit

print(max_profit([7,1,5,3,6,4]))

#Recursion Pattern
#Print numbers from n to 1.
def print_n(n):
    if n == 0:
        return
    print(n)
    print_n(n-1)

print_n(5)

#BFS (Queue Pattern)
#Simple BFS traversal
from collections import deque

def bfs(graph, start):
    q = deque([start])
    visited = set([start])

    while q:
        node = q.popleft()
        print(node)

        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                q.append(n)