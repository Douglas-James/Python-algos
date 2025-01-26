# Given array of numbers, find the sum of all numbers in the array
# Linear time complexity O(n)
def sum(arr):
  # Base case
  total = 0 # 0 is the identity element for addition
  for x in arr:
    # total = total + x
    total += x # 1+2+3+4 = 10
  # return total
  return total

x = [1, 2, 3, 4]
print(sum(x)) # 10


# Constant time complexity O(1)
def sum_constant(n):
  return n * (n + 1) // 2

print(sum_constant(4)) # 10

# RECURSION - Linear time complexity O(n)
def sum_recursion(arr):
  # Base case
  if len(arr) == 0:
    return 0
  # Recursive case
  return arr[0] + sum_recursion(arr[1:])
r = [1, 2, 3, 4, 10]
print(sum_recursion(r)) # 20

# Haskell implementation of sum using recursion
def sum_haskell(arr):
  # Base case
  if not arr:
    return 0
  # Recursive case
  return arr[0] + sum_haskell(arr[1:])
h = [1, 2, 3, 4]
print(sum_haskell(h)) # 10

# arr = [1, 2, 3, 4, 5]

# sums arr = if arr == []
#     then 0
#     else (head arr) + (sums (tail arr))
