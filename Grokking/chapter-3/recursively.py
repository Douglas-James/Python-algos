# Pseudocode
# def look_for_key(main_box):
#   pile = main_box.make_a_pile_to_look_through()
#   while pile is not empty:
#     box = pile.grab_a_box()
#     for item in box:
#       if item.is_a_box():
#         pile.append(item)
#       elif item.is_a_key():
#         print("found the key!")


# def look_for_key(box):
#   for item in box:
#     if item.is_a_box():
#       look_for_key(item)
#     else item.is_a_key():
#       print("Find the key!")

# cound Down recursively
def countdow(i):
  print(i)  # 3 -> 2 -> 1 -> so etc..
  # base case
  if i <= 1:
    return
  else:
    # call the recursive function
    countdow(i-1)

countdow(3)
