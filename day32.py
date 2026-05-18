# 1. Find Median of List
def median(nums):
    nums.sort()
    n = len(nums)

    if n % 2 == 0:
        return (nums[n//2 - 1] + nums[n//2]) / 2
    return nums[n//2]

print(median([5,1,3,2,4]))


# 2. Count Uppercase Letters
def count_uppercase(s):
    count = 0

    for ch in s:
        if ch.isupper():
            count += 1

    return count

print(count_uppercase("PyThOn"))


# 3. Find Common Prefix Between Two Strings
def common_prefix(a, b):
    res = ""

    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            res += a[i]
        else:
            break

    return res

print(common_prefix("flower", "flow"))


# 4. Find Maximum Difference
def max_difference(nums):
    return max(nums) - min(nums)

print(max_difference([10,2,8,1,15]))


# 5. Remove Negative Numbers from List
def remove_negative(nums):
    return [n for n in nums if n >= 0]

print(remove_negative([-1,2,-3,4,5]))


# 6. Check if List Contains Target
def contains(nums, target):
    return target in nums

print(contains([1,2,3,4], 3))


# 7. Find Character with Maximum Frequency
def max_frequency_char(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return max(freq, key=freq.get)

print(max_frequency_char("programming"))


# 8. Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(25))


# 9. Find Missing Elements Between Range
def missing_elements(nums):
    res = []

    for i in range(min(nums), max(nums)+1):
        if i not in nums:
            res.append(i)

    return res

print(missing_elements([1,2,4,6]))


# 10. Swap First and Last Element of List
def swap_first_last(nums):
    nums[0], nums[-1] = nums[-1], nums[0]
    return nums

print(swap_first_last([1,2,3,4,5]))