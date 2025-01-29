# Hash table
"""
A hash table is a data structure that stores key-value pairs. It uses a hash function to compute an index into an array of buckets or slots,
from which the desired value can be found.
"""
# simple hash table is not ordered and has a key-value pair, most usefull for complex data structures.
# name of variable maggie Key = "Eggs" value = 2.99
maggie = {
  "Eggs": 2.99,
  "Milk": 3.99,
  "Cheese": 4.99,
  "Butter": 5.99,
  "Apple": 1.99,
  "Banana": 0.99,
  "Orange": 1.99,
  "Grapes": 2.99,
  "Strawberry": 3.99,
  "Avocado": 4.99,
  "Peach": 1.99,
  "Pineapple": 0.99,
}

# this constant time O(1) (input 7 = 7 times) if ask maggie for the price of eggs
print(maggie["Eggs"]) # => 2.99

# this constant time O(1) (input 7 = 7 times) if ask maggie for the price of milk
print(maggie["Milk"]) # => 3.99

# this constant time O(1) (input 7 = 7 times) if ask maggie for the price of cheese
print(maggie["Cheese"]) # => 4.99

# this constant time O(1) (input 7 = 7 times) if ask maggie for the price of butter
print(maggie["Butter"]) # => 5.99

# This is statement that checks if the key is in the hash table
if("Eggs" in maggie):
  print("Yes, I have eggs")
else:
  print("No, I don't have eggs")

# This hash table for phone book
phone_book = {
  "John": 123456789,
  "Jane": 987654321,
  "Alice": 123456789,
  "Bob": 987654321,
  "Charlie": 123456789,
  "David": 987654321,
  "Eve": 123456789,
  "Frank": 987654321,
  "Grace": 123456789,
  "Helen": 987654321,
  "Ivy": 123456789,
  "Jack": 987654321,
}

# if ask phone book for John number
print(phone_book["John"]) # => 123456789

# if ask phone book for Jane number
print(phone_book["Jane"]) # => 987654321

# how about ask phone book for James number that is not in the phone book
# print(phone_book["James"]) # => KeyError: 'James'

# This statement checks if the key "James" is in the phone book hash table.
# Since we haven't added James to the phone book yet, it will return false.
if("James" in phone_book):
  print("Yes, I have James number")
else:
  print("No, I don't have James number")

# Adding James' number to the phone book
phone_book["James"] = 123456789
print(phone_book["James"]) # => 123456789

# Preventing duplicate entries in votes hash table
votes = {}
def check_voter(name):
  if name in votes:
    print("Kick them out!")
  else:
    votes[name] = True
    print("Let them vote!")

check_voter("Tom") # => Let them vote!
check_voter("Mike") # => Let them vote!
check_voter("Tom") # => Kick them out!
check_voter("Mike") # => Kick them out
check_voter("James") # => Let them vote!
# This cache hash table is used to store data from the server
cache = {
  "http://www.google.com": "We have stored in cache for http://www.google.com",
  "http://www.facebook.com": "We have stored in cache for http://www.facebook.com",
  "http://www.twitter.com": "We have stored in cache for http://www.twitter.com",
  "http://www.instagram.com": "We have stored in cache for http://www.instagram.com",
}

# This function gets data from the server
def get_data_from_server(url):
  return f"Data from server {url}"

# This function gets the page from the cache hash table
def get_page(url):
  if url in cache:
    return cache[url]
  else:
    data = get_data_from_server(url)
    cache[url] = data
    return data

print(get_page("http://www.google.com")) # => We have stored in cache for http://www.google.com
print(get_page("http://www.facebook.com")) # => We have stored in cache for http://www.facebook.com
print(get_page("http://www.linkedin.com")) # => Data from server http://www.linkedin.com
