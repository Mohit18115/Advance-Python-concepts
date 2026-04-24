
#Check if List is Empty
#Question: Check if list is empty.

def is_empty(nums):
    return len(nums) == 0

print(is_empty([]))

#Print List Elements One by One
#Question: Print each element.

def print_list(nums):
    for n in nums:
        print(n)

print_list([1,2,3])

#Replace Character in String
#Question: Replace one character with another.

def replace_char(s):
    return s.replace("a", "x")

print(replace_char("banana"))

#check number divisibility by 5
#Questions: Check Divisiblity

def divisible_by_5(n):
    return n % 5 == 0

print(divisible_by_5(25))

#Multiply All Elements
#Question: Multiply all numbers in list.

def multiply(nums):
    result = 1
    for n in nums:
        result *= n
    return result

print(multiply([2,3,4]))

#Count Spaces in String
#Question: Count number of spaces.

def count_spaces(s):
    return s.count(" ")

print(count_spaces("I love python"))

#Find Last Element of List
#Question: Get last element.

def last_element(nums):
    return nums[-1]

print(last_element([10,20,30]))

#Convert String to Uppercase
#Question: Convert all letters to uppercase.

def to_upper(s):
    return s.upper()

print(to_upper("python"))

#Check Positive or Negative
#Question: Check if number is positive, negative, or zero.

def check_num(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"

print(check_num(-5))

#Find Square of Numbers
#Question: Print square of each number in a list.

def squares(nums):
    return [n*n for n in nums]

print(squares([1,2,3,4]))
