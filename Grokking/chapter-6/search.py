from collections import deque
def search(name):
    search_queue = deque() # Create a queue
    search_queue += graph[name] # Add all of your friends to the search queue
    searched = set() # Set to keep track of searched nodes
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return name + " is not a mango seller!"

def person_is_seller(name):
    return name[-1] == 'm'

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'bob']
graph['anuj'] = []
graph['peggy'] = []

print(search('you')) # True
print(search('bob')) # False




