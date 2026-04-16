#Second Largest Element
def second_largest(nums):
    nums = list(set(nums))
    nums.sort()
    return nums[-2]

print(second_largest([10, 20, 4, 45, 99]))

#Check Anagram
def is_anagram(s, t):
    return sorted(s) == sorted(t)

print(is_anagram("listen", "silent"))

#Move Zeros to End

def move_zeros(nums):
    result = [n for n in nums if n != 0]
    result += [0] * nums.count(0)
    return result

print(move_zeros([0,1,0,3,12]))

#Find Missing Number

def missing_number(nums):
    n = len(nums) + 1
    return n*(n+1)//2 - sum(nums)

print(missing_number([1,2,4,5]))

#First Non-Repeating Character
def first_unique(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None

print(first_unique("aabbcde"))

##Rotate List
def rotate(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

print(rotate([1,2,3,4,5], 2))

#Intersection of Two Lists

def intersection(a, b):
    return list(set(a) & set(b))

print(intersection([1,2,2,3], [2,3,4]))

#Longest Word in Sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("I love learning python programming"))

#Count Substrings
def count_substring(s, sub):
    return s.count(sub)

print(count_substring("abababa", "aba"))

#Reverse Words in Sentence
def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

print(reverse_words("I love python"))