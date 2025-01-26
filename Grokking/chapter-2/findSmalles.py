"""
The Function findSmallest as takes array(JavaScript) or list(Python) and return the index of the smallest value
"""
# Linear time o(n)
def findSmallest(arr):
  # Store the smallest value
  smallest = arr[0]
  # Store the smallest index of the smallest value
  smallest_index = 0
  for i in range(1, len(arr)):
    #   9 = array started is greater then 10 = smallest is true so move into the array
    if arr[i] < smallest:
      smallest = arr[i] # -> 9  -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1
      smallest_index = i # -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
  # return index 9
  return smallest_index
# First Run
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# index 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
arr_2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
# index   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
print(findSmallest(arr)) # => 9
print(findSmallest(arr_2)) # => 11
