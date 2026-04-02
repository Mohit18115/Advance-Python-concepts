#Merge Sort (Efficient Sorting)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

nums = [38,27,43,3,9,82,10]
print(merge_sort(nums))

#Sliding Window (Maximum Sum Subarray)

def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum

nums = [2,1,5,1,3,2]
print(max_sum_subarray(nums,3))

#Two Pointer Technique (Pair Sum)

def pair_sum(arr, target):
    left = 0
    right = len(arr)-1

    while left < right:
        s = arr[left] + arr[right]

        if s == target:
            return (arr[left], arr[right])
        elif s < target:
            left += 1
        else:
            right -= 1

    return None

nums = [1,2,3,4,6]
print(pair_sum(nums,6))

#Stack Problem (Valid Parentheses)

def valid_parentheses(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}

    for char in s:
        if char in mapping:
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return not stack

print(valid_parentheses("()[]{}"))

#Binary Tree Level Order Traversal

from collections import deque

def level_order(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

#from collections import deque

def level_order(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

#Longest Increasing Subsequence

def length_of_lis(nums):
    dp = [1]*len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)

print(length_of_lis([10,9,2,5,3,7,101,18]))

#Anagram Check

def is_anagram(s,t):
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char,0) + 1

    for char in t:
        if char not in count:
            return False
        count[char] -= 1

    return True

print(is_anagram("listen","silent"))