"""
Binary Search Takes a sorted array and an item.
arr = [1,  2, 3, 4, 5, 6, 7, 8, 9, 10]
index= 0 , 1, 2, 3, 4, 5, 6, 7, 8, 9
low = 0
high = 9
mid  = 0 + 9 % 2 = 4 index = 5 value arr[mid]
guess = 5 value
check guess equal to the target value if so return 4
guess greater then the target high = 3 index = 4 arr[mid] value
else low = 4 + 1 = 5 index = 6 arr[mid] value
mid = 5 + 9 % 2 = 7 index = 8 arr[mid] value
"""
# Log time O(log n) (input 10 arrays % 2 = 3 times) log2(10) = 3.32
def binary_search(arr, item):
  # low pointer and high pointer
  low = 0
  high = len(arr) - 1
  # loop through 1-10
  while low <= high:
    mid = (low + high) // 2
    guess = arr[mid]

    # if statement and if else and else
    if guess == item:
      return mid
    elif guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(my_list, 10)) # => 9
print(binary_search(my_list, 3)) # => 2
print(binary_search(my_list, 11)) # => - 1

# Linear time O(n) (input 10 = 10 times)
def simpleSearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
      guess = arr[low]
      if guess == target:
        return low
      low += 1
    return -1

# print(simpleSearch(my_list, 7)) # => 6
# print(simpleSearch(my_list, 10)) # => 9
# print(simpleSearch(my_list, 11)) # => - 1


# Binary search using recursion
def binary_search_recursion(arr, target):
  if len(arr) == 0:
    return -1
  mid = len(arr) // 2
  guess = arr[mid]
  if guess == target:
    return mid
  elif guess > target:
    return binary_search_recursion(arr[:mid], target)
  else:
    return binary_search_recursion(arr[mid + 1:], target)


print(binary_search_recursion(my_list, 10)) # => 9
print(binary_search_recursion(my_list, 3)) # => 2
