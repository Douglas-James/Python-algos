# Quick sort implementation
def quicksort(arr):
  # Base case
  if len(arr) < 2:
    return arr
  # Recursive case
  else:
    # The pivot is the first element of the array or you can choose a random element
    pivot = arr[0] # pivot = -1
    less = [i for i in arr[1:] if i <= pivot] # loop through the array and check if i is less than or equal to the pivot
    greater = [i for i in arr[1:] if i > pivot] # loop through the array and check if i is greater than the pivot
    return quicksort(less) + [pivot] + quicksort(greater) # quicksort(less) = [-1] + [1, 2, 3, 4, 5, 6, 10] + quicksort(greater) = [10]

x = [-1, 10, 5, 3, 2, 4, 1, 6]
print(quicksort(x)) # [-1, 1, 2, 3, 4, 5, 6, 10]

# quick sort
def quicksort_1(arr):
  # base case
  if len(arr) < 2:
    return arr

  # pivot = arr[0] # pivot = -1
  pivot = arr[0]

  # less is an empty array
  less = []

  # greater is an empty array
  greater = []

  # loop through the array start from the second element 10, 5, 3, 2, 4, 1, 6
  for i in arr[1:]:
    # if i is less than or equal to the pivot
    if i <= pivot:
      less.append(i)
    # esle i is greater than the pivot
    else:
      greater.append(i)

  # recursisve call
  return quicksort_1(less) + [pivot] + quicksort_1(greater) # quicksort_1(less) = [-1] + [1, 2, 3, 4, 5, 6, 10] + quicksort_1(greater) = [10]

y = [-1, 10, 5, 3, 2, 4, 1, 6]
ys = [33, 15, 10]
print(quicksort_1(y)) # [-1, 1, 2, 3, 4, 5, 6, 10]
print(quicksort_1(ys)) # [10, 15, 33]
