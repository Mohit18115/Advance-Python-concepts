#find length of string
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

print(string_length("python"))

#Check Armstrong Number
def is_armstrong(n):
    s = str(n)
    power = len(s)
    total = sum(int(d)**power for d in s)
    return total == n

print(is_armstrong(153))

#Find GCD

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(12, 18))

#Remove Spaces from String

def remove_spaces(s):
    return s.replace(" ", "")

print(remove_spaces("I love python"))

#Count Occurrence of Element

def count_occurrence(nums, target):
    count = 0
    for n in nums:
        if n == target:
            count += 1
    return count

print(count_occurrence([1,2,2,3,2], 2))

#Find All Factors

def factors(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result

print(factors(12))

#Merge Two Lists

def merge_lists(a, b):
    return a + b

print(merge_lists([1,2], [3,4]))

#Check Substring

def is_substring(s, sub):
    return sub in s

print(is_substring("python programming", "gram"))

#Find All Pairs with Given Sum

def pair_sum(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append((nums[i], nums[j]))
    return result

print(pair_sum([1,2,3,4,5], 5))

#Count Unique Elements

def count_unique(nums):
    return len(set(nums))

print(count_unique([1,2,2,3,4,4,5]))
