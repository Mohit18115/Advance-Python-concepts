#Rerverse a String
def reverse_string(s):
    return s[::-1]

print(reverse_string("python"))

#Check Palindrome
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("level"))

#Find largest number in list
def find_max(nums):
    return max(nums)

print(find_max([4, 8, 2, 10, 6]))

#Count even numbers
def count_even(nums):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    return count

print(count_even([1,2,3,4,5,6]))

#Sum of list elements
def list_sum(nums):
    return sum(nums)

print(list_sum([5,10,15]))

#linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([2,4,6,8], 6))

#factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))

#remove duplicates from list
def remove_duplicates(nums):
    return list(set(nums))

print(remove_duplicates([1,2,2,3,4,4]))

#find prime numbers
def find_primes(n):
    primes = []

    for num in range(2, n+1):
        is_prime = True

        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes

print(find_primes(20))

#Fibonacci Series
def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(7)
