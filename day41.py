#Queue (FIFO)
from collections import deque

q = deque()

q.append(1)
q.append(2)

print(q.popleft())
#Stack (LIFO)
stack = []

stack.append(10)
stack.append(20)

print(stack.pop())
#Hash Map (Dictionary)
def count_numbers(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    return freq
#Recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

#Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

#Sliding Window
def max_sum(nums, k):
    max_sum = 0

    for i in range(len(nums) - k + 1):
        current = sum(nums[i:i+k])
        max_sum = max(max_sum, current)

    return max_sum

#Two Pointers Technique
def is_palindrome(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True