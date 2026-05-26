#Check Even or Odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

print(check_even_odd(7))

##Count Vowels in String
def count_vowels(s):
    vowels = "aeiou"
    count = 0

    for ch in s:
        if ch.lower() in vowels:
            count += 1

    return count

print(count_vowels("python"))

#Find Minimum Number
def find_min(nums):
    return min(nums)

print(find_min([5, 2, 8, 1]))

#Print Multiplication Table
def table(n):
    for i in range(1, 6):
        print(n, "x", i, "=", n*i)

table(5)

#Count Digits in Number

def count_digits(n):
    return len(str(n))

print(count_digits(12345))

#Find Sum of Digits

def sum_digits(n):
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total

print(sum_digits(123))

#Check Prime Number

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

print(is_prime(7))

#Swap Two Numbers

a = 5
b = 10

a, b = b, a

print(a, b)

##Find Common Elements in Two Lists
def common_elements(a, b):
    return list(set(a) & set(b))

print(common_elements([1,2,3], [2,3,4]))

#Count Words in Sentence
def count_words(sentence):
    return len(sentence.split())

print(count_words("I love python programming"))
