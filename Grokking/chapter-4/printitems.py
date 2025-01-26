# from time import sleep


# def print_items(arr):
#   for item in arr:
#     sleep(1) # sleep for 1 second
#     print(item)

# print_items([1, 2, 3, 4, 5]) # 1, 2, 3, 4, 5


def multiplyTable(arr):
  for i in arr:
    for j in arr:
      print(f"{i} * {j} = {i * j}")

multiplyTable([2, 3, 7, 8, 10])
