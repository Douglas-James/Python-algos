# Call Stack
def greeting(name):
  print(f"Hello, {name}!")
  greeting2(name)
  print("Getting ready to say by...")
  bye()

def greeting2(name):
  print(f"How are you, {name}?")

def bye():
  print("ok bye! ")

greeting("James")

# call Stack with recursive
def fact(x):
  # base case
  if x == 1: # x equal 1 it return 1 and stop the recursive call
    return 1
  # recursive case
  else:
    return x * fact(x-1) # 3 * 2 = 6

print("Recursive call stack:",fact(3))
