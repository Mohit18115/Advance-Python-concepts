#1. Merge Two Sorted Arrays (without extra space)
def merge_sorted_arrays(a, b):
    
    #Merge two sorted arrays into a single sorted array
    #without using extra space.
    
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

# Test
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_sorted_arrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6]

#2. Find Maximum Subarray Sum (Kadane’s Algorithm)

def max_subarray_sum(arr):
    max_sum = curr_sum = arr[0]
    for num in arr[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

# Test
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))  # Output: 6 (4 + -1 + 2 + 1)

#3. Detect Cycle in Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head  # cycle
print(has_cycle(head))  # Output: True

#4. Find First Non-Repeating Character in a String

from collections import Counter

def first_non_repeating_char(s):
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

# Test
print(first_non_repeating_char("swiss"))  # Output: 'w'

#5. Minimum Window Substring (Sliding Window)

def min_window_substring(s, t):
    from collections import Counter
    need = Counter(t)
    missing = len(t)
    left = start = end = 0
    
    for right, char in enumerate(s):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        while missing == 0:
            if end == 0 or right - left + 1 < end - start + 1:
                start, end = left, right
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return s[start:end+1] if end != 0 else ""

# Test
s = "ADOBECODEBANC"
t = "ABC"
print(min_window_substring(s, t))  # Output: "BANC"


#6. Rotate Matrix by 90 Degrees

def rotate_matrix(mat):
    n = len(mat)
    # Transpose
    for i in range(n):
        for j in range(i, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    # Reverse each row
    for row in mat:
        row.reverse()
    return mat

# Test
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(rotate_matrix(matrix))
# Output: [[7,4,1],[8,5,2],[9,6,3]]

#7. LRU Cache Implementation

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Test
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # 1
lru.put(3, 3)      # Evicts key 2
print(lru.get(2))  # -1

#8. Word Ladder / Transformation Problem (BFS)

from collections import deque

def word_ladder(begin, end, word_list):
    word_set = set(word_list)
    queue = deque([(begin, 1)])
    
    while queue:
        word, steps = queue.popleft()
        if word == end:
            return steps
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in word_set:
                    word_set.remove(next_word)
                    queue.append((next_word, steps+1))
    return 0

# Test
print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # Output: 5