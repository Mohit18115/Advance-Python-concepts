# 1. Find Average of List
def average(nums):
    return sum(nums) / len(nums)

print(average([10,20,30,40]))


# 2. Check if Number is Multiple of 3
def multiple_of_3(n):
    return n % 3 == 0

print(multiple_of_3(9))


# 3. Reverse List
def reverse_list(nums):
    return nums[::-1]

print(reverse_list([1,2,3,4]))


# 4. Find Largest Odd Number in List
def largest_odd(nums):
    odds = [n for n in nums if n % 2 != 0]
    return max(odds) if odds else None

print(largest_odd([2,4,7,9,10]))


# 5. Remove All Occurrences of Element
def remove_element(nums, val):
    return [n for n in nums if n != val]

print(remove_element([1,2,3,2,4], 2))


# 6. Check if String Starts with Given Prefix
def starts_with(s, prefix):
    return s.startswith(prefix)

print(starts_with("python", "py"))


# 7. Find Sum of Digits (Using String)
def sum_digits(n):
    return sum(int(d) for d in str(n))

print(sum_digits(1234))


# 8. Find Common Elements (Without Set)
def common_elements(a, b):
    res = []
    for n in a:
        if n in b and n not in res:
            res.append(n)
    return res

print(common_elements([1,2,3], [2,3,4]))


# 9. Check if All Elements are Positive
def all_positive(nums):
    for n in nums:
        if n < 0:
            return False
    return True

print(all_positive([1,2,3,4]))


# 10. Find Length of Longest List Element (Strings)
def longest_len(lst):
    max_len = 0
    for item in lst:
        if len(item) > max_len:
            max_len = len(item)
    return max_len

print(longest_len(["hi","hello","python"]))