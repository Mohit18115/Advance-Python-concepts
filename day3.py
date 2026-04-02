#Fibonacci with Dynamic Programming
#Topic:- Optimization technique used in DP problems.
def fibonacci(n):
    dp = [0,1]

    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])

    return dp[n]

# Example
print(fibonacci(10))
#Longest Common Prefix (String Problem)
#Topic:- Common question in interviews.
def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for word in strs[1:]:
        while word.find(prefix) != 0:
            prefix = prefix[:-1]

            if prefix == "":
                return ""

    return prefix


# Example
words = ["flower", "flow", "flight"]
print(longest_common_prefix(words))

#Quick Sort (Divide & Conquer)
#Topic:-Sorting algorithm faster than Bubble Sort.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example
nums = [10, 7, 8, 9, 1, 5]
print(quick_sort(nums))

