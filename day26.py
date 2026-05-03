#if else
a = 50

if a > 10:
    print("Big")
else:
    print("Small")
#for loop
for i in range (1, 11):
        print(i)
#function
def add (a , b):
     return a + b
print(add(3 ,3))        
#list
a = [12,13,14,15,16,17,28,19,20]

for num in a:
     print(num)

#logic practice

b = 4

if b%2 == 0:
     print("Even")
else:
     print("Odd")

#Problem 1 — Largest Number
numbers = [4, 7, 2, 9, 1]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)

#or
numbers = [4, 7, 2, 9, 1]
print(max(numbers))

#reverse a number
c = "1 2 3 4"
number = c.split()
number.reverse()
print(" ".join(number))

    
#count even numbers
counts=[1,2,3,4,5,6]     
count = 0
for num in counts:
     if num%2==0:
          count +=1
print(count)
#Question 1 — Strings
name = "Mohit"
print(name[0])
print(name[4])
#Question 1 —Reverse a Strings
variable = "Python"
print(variable[::-1])
#palindrome
word = "madam"
if word == word[::-1]:
     print("Yes, it is Palindrome")
else:
     print("No")
#Dictionary
info = {
     "name" : "Mohit" ,
     "age" : 20 , 
     "city" : "Chandigarh"
     } 
print(info["name"])     
print(info["age"])
print(info["city"])

no_1 = 3
if no_1 % 2 == 0:
     print(no_1 , "IS EVEN")
else:
     print(no_1 ,"IS NOT EVEN")
