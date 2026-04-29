# 1. Find Sum of Even Numbers in List
def sum_even(nums):
    return sum(n for n in nums if n % 2 == 0)

print(sum_even([1,2,3,4,5,6]))


# 2. Check if String is Empty or Not
def is_empty(s):
    return len(s) == 0

print(is_empty(""))


# 3. Find Index of First Occurrence
def first_index(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

print(first_index([1,2,3,4], 3))


# 4. Convert List to String
def list_to_string(chars):
    return "".join(chars)

print(list_to_string(['p','y','t','h','o','n']))


# 5. Find Smallest Element
def find_min(nums):
    return min(nums)

print(find_min([5,3,8,1,2]))


# 6. Count Words in Sentence
def word_count(s):
    return len(s.split())

print(word_count("I love learning python"))


# 7. Check if Number is Even or Odd
def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print(even_odd(7))


# 8. Remove Duplicate Characters from String
def remove_duplicates(s):
    return "".join(set(s))

print(remove_duplicates("programming"))


# 9. Find Difference Between Max and Min
def diff_max_min(nums):
    return max(nums) - min(nums)

print(diff_max_min([10,3,5,6]))


# 10. Count Occurrence of Each Element
def count_elements(nums):
    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1
    return d

print(count_elements([1,2,2,3,3,3]))