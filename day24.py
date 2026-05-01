#dsa problem 1(Binary Search)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
        
# Example
arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 7))  # Output: 3

#dsa problem 2(Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]

#dsa problem 3(Linked List Implementation)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Output: 1 -> 2 -> 3 -> None

#dsa problem 4(Stack Implementation)
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

# Example
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2

#dsa problem 5(Queue Implementation)
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None
    
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None
    
    def is_empty(self):
        return len(self.queue) == 0

# Example
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.front())    # Output: 2

#dsa problem 5(Binary Tree Traversal)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder_traversal(root):
    result = []
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    inorder(root)
    return result

# Example
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(inorder_traversal(root))  # Output: [4, 2, 5, 1, 3]

#dsa problem 6(print right angles triagle)

def print_pattern(n):
    for i in range(1, n + 1):
        print('*' * i)

# Test
print_pattern(5)

#dsa problem 7(Sum of Digits)
def sum_of_digits(num):
    
    # Handle negative numbers
    num = abs(num)
    total = 0
    
    while num > 0:
        digit = num % 10  # Get last digit
        total += digit    # Add to sum
        num //= 10        # Remove last digit
    
    return total

# Test cases
print(sum_of_digits(1234))    # Output: 10
print(sum_of_digits(9876))    # Output: 30
print(sum_of_digits(1001))    # Output: 2

#dsa problem 8(Find Prime Numbers)

def find_primes(limit):
    """
    Find all prime numbers up to the given limit
    """
    primes = []
    
    for num in range(2, limit + 1):
        is_prime = True
        
        # Check if num is divisible by any number from 2 to sqrt(num)
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(num)
    
    return primes

# Test
print(find_primes(30))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

#dsa problem 9(Reverse a String)
def reverse_string(s):
    """
    Reverse a string using loop
    Example: "hello" -> "olleh"
    """
    reversed_str = ""
    
    # Method 1: Iterate from end to start
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    
    return reversed_str

# Alternative method using while loop
def reverse_string_while(s):
    reversed_str = ""
    i = len(s) - 1
    
    while i >= 0:
        reversed_str += s[i]
        i -= 1
    
    return reversed_str

# Test
print(reverse_string("Python"))        # Output: nohtyP
print(reverse_string_while("Loop"))    # Output: pooL

#dsa problem 10(Multiplication Table)

def multiplication_table(num, limit=10):
    """
    Print multiplication table for a number
    Example: num=5, limit=10
    5 x 1 = 5
    5 x 2 = 10
    ...
    5 x 10 = 50
    """
    print(f"Multiplication Table for {num}:")
    print("-" * 25)
    
    for i in range(1, limit + 1):
        result = num * i
        print(f"{num} x {i:2} = {result:3}")

# Test
multiplication_table(7, 12)
