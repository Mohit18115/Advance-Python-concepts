#capitalize first letter
def capitalize_words(s):
    return s.title()

print(capitalize_words("i love python"))

#find duplicate element

def find_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return n
        seen.add(n)

print(find_duplicate([1,3,4,2,2]))

#sum of first n number

def sum_n(n):
    return n*(n+1)//2

print(sum_n(5))

#check sorted list

def is_sorted(nums):
    return nums == sorted(nums)

print(is_sorted([1,2,3,4]))

#find missing character

def missing_char(s1, s2):
    for ch in s1:
        if ch not in s2:
            return ch

print(missing_char("abcd", "abc"))

#remove vowels

def remove_vowels(s):
    vowels = "aeiou"
    return "".join(ch for ch in s if ch.lower() not in vowels)

print(remove_vowels("python programming"))

#find common prefix

def common_prefix(strs):
    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    return prefix

print(common_prefix(["flower","flow","flight"]))

#check perfect number

def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

print(is_perfect(6))

#reverse number
def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

print(reverse_number(1234))


#check leap year

def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

print(is_leap(2024))