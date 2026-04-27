# 1. Find Intersection of Two Arrays
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

print(intersection([1,2,2,3], [2,3,4]))


# 2. Find First Missing Positive Number
def first_missing(nums):
    nums = set(nums)
    i = 1
    while True:
        if i not in nums:
            return i
        i += 1

print(first_missing([3,4,-1,1]))


# 3. Check if Two Strings are Isomorphic
def is_isomorphic(s, t):
    m1, m2 = {}, {}

    for a, b in zip(s, t):
        if m1.get(a, b) != b or m2.get(b, a) != a:
            return False
        m1[a] = b
        m2[b] = a

    return True

print(is_isomorphic("egg", "add"))


# 4. Maximum Sum Subarray (Kadane’s Algorithm)
def max_subarray(nums):
    curr = nums[0]
    max_sum = nums[0]

    for n in nums[1:]:
        curr = max(n, curr + n)
        max_sum = max(max_sum, curr)

    return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))


# 5. Find All Duplicates in Array
def find_duplicates(nums):
    seen = set()
    res = []

    for n in nums:
        if n in seen:
            res.append(n)
        else:
            seen.add(n)

    return res

print(find_duplicates([4,3,2,7,8,2,3,1]))


# 6. Check Valid Anagram
def is_anagram(s, t):
    return sorted(s) == sorted(t)

print(is_anagram("anagram", "nagaram"))


# 7. Find Peak Element
def find_peak(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return i
    return len(nums)-1

print(find_peak([1,2,3,1]))


# 8. Merge Two Sorted Arrays
def merge_sorted(a, b):
    return sorted(a + b)

print(merge_sorted([1,3,5], [2,4,6]))


# 9. Longest Common Prefix
def longest_prefix(strs):
    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]

    return prefix

print(longest_prefix(["flower","flow","flight"]))


# 10. Count Subarrays with Sum = K
def subarray_sum(nums, k):
    count = 0

    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total == k:
                count += 1

    return count

print(subarray_sum([1,1,1], 2))