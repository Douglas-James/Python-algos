# Linear time o(n)
def findSmallest(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  # return smallest index of the value
  return smallest_index

# Quadratic time O(n^2)
def selectionSort(arr):
  newArray = []
  copiedArr = list(arr)
  for i in range(len(copiedArr)):
    smallest = findSmallest(copiedArr)
    newArray.append(copiedArr.pop(smallest)) # add the smallest value and removed from the copiedArr
  return newArray


unsortedArray = [10, 7, 9, 1, 3, 2, 4, 5, 8, 6]
print(selectionSort(unsortedArray)) # => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
