# 1. Find Minimum Element in Rotated Sorted Array
def find_min(nums):
    return min(nums)

print(find_min([4,5,6,7,0,1,2]))


# 2. Check if Array is Monotonic
def is_monotonic(nums):
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)

print(is_monotonic([1,2,2,3]))


# 3. Reverse Words in a String
def reverse_words(s):
    return " ".join(s.split()[::-1])

print(reverse_words("I love python"))


# 4. Find Majority Element (> n/2 times)
def majority(nums):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
        if count[n] > len(nums)//2:
            return n

print(majority([3,2,3]))


# 5. Check if String Contains Only Digits
def is_digits(s):
    return s.isdigit()

print(is_digits("12345"))


# 6. Find Second Smallest Element
def second_smallest(nums):
    nums = list(set(nums))
    nums.sort()
    return nums[1]

print(second_smallest([4,1,2,3,2]))


# 7. Count Vowels in String
def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for ch in s.lower() if ch in vowels)

print(count_vowels("hello world"))


# 8. Find All Even Numbers in List
def even_numbers(nums):
    return [n for n in nums if n % 2 == 0]

print(even_numbers([1,2,3,4,5,6]))


# 9. Check if Two Lists are Equal
def list_equal(a, b):
    return a == b

print(list_equal([1,2,3], [1,2,3]))


# 10. Find Length of Longest Word
def longest_word_len(s):
    return max(len(word) for word in s.split())

print(longest_word_len("I love python programming"))