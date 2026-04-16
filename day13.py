#decode string

def decode_string(s):
    stack = []
    curr_num = 0
    curr_str = ""

    for ch in s:
        if ch.isdigit():
            curr_num = curr_num*10 + int(ch)
        elif ch == "[":
            stack.append((curr_str, curr_num))
            curr_str = ""
            curr_num = 0
        elif ch == "]":
            prev_str, num = stack.pop()
            curr_str = prev_str + num * curr_str
        else:
            curr_str += ch

    return curr_str

print(decode_string("3[a2[c]]"))

#Top K Frequent Words

from collections import Counter

def top_k_words(words, k):
    count = Counter(words)
    return [w for w,_ in count.most_common(k)]

print(top_k_words(["i","love","i","python"], 2))

#merge intervels

def merge(intervals):
    intervals.sort()
    res = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= res[-1][1]:
            res[-1][1] = max(res[-1][1], end)
        else:
            res.append([start, end])

    return res

print(merge([[1,3],[2,6],[8,10]]))

#comvbination sum

def combination_sum(candidates, target):
    res = []

    def backtrack(start, path, total):
        if total == target:
            res.append(path)
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            backtrack(i, path + [candidates[i]], total + candidates[i])

    backtrack(0, [], 0)
    return res

print(combination_sum([2,3,6,7], 7))

#search in rotated  sorted way 

def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

print(search([4,5,6,7,0,1,2], 0))

#sort colors

def sort_colors(nums):
    nums.sort()
    return nums

print(sort_colors([2,0,2,1,1,0]))

#majority element

def majority_element(nums):
    count = {}

    for n in nums:
        count[n] = count.get(n, 0) + 1

        if count[n] > len(nums)//2:
            return n

print(majority_element([2,2,1,1,2,2]))

#Minimum Size Subarray Sum

def min_subarray_len(target, nums):
    left = 0
    total = 0
    res = float('inf')

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            res = min(res, right-left+1)
            total -= nums[left]
            left += 1

    return res if res != float('inf') else 0

print(min_subarray_len(7, [2,3,1,2,4,3]))

#Longest Palindromic Substring

def longest_palindrome(s):
    res = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            temp = s[i:j+1]
            if temp == temp[::-1] and len(temp) > len(res):
                res = temp
    return res

print(longest_palindrome("babad"))
