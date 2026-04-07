#Print Numbers Using Loop
for i in range(1,11):
    print(i)
#Find Length of List
nums = [10, 20, 30, 40]

print(len(nums))
#Simple Function Example
def add(a , b):
    return a + b
print(add(3,4))    

#remove duplicates from list
nums = [1, 2, 2, 3, 4, 4]

unique = list(set(nums))

print(unique)

#count characters in string
text = "apple"

count = {}

for char in text:
    count[char] = count.get(char, 0) + 1

print(count)
#Check Palindrome String
word = "level"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
#Sum of List Elements
nums = [2, 4, 6, 8]

total = sum(nums)

print(total)
#Count Even Numbers
nums = [1, 2, 3, 4, 5, 6]

count = 0

for num in nums:
    if num % 2 == 0:
        count += 1

print(count)

#Find Maximum Number
nums = [10, 5, 8, 20, 3]

largest = max(nums)

print(largest)

#Reverse a List
nums = [1, 2, 3, 4, 5]

nums.reverse()

print(nums)