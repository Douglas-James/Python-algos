class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None

class HashTable:
  def __init__(self, size):
    self.size = size
    self.table = [None] * size

  def hash_function(self, key):
    return sum(ord(char) for char in key) % self.size

  def insert(self, key, value):
    index = self.hash_function(key)
    new_node = Node(key, value)
    if self.table[index] is None:
      self.table[index] = new_node
    else:
      current = self.table[index]
      while current.next:
        current = current.next
      current.next = new_node

  def get(self, key):
    index = self.hash_function(key)
    current = self.table[index]
    while current:
      if current.key == key:
        return current.value
      current = current.next
    return None

# Example usage
hash_table = HashTable(26)
hash_table.insert("apple", 1.2)
hash_table.insert("banana", 0.5)
hash_table.insert("orange", 0.8)

print("Price of apple:", hash_table.get("apple"))
print("Price of banana:", hash_table.get("banana"))
print("Price of orange:", hash_table.get("orange"))
