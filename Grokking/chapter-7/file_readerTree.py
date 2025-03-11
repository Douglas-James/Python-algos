from os import listdir
from os.path import isfile, join
from collections import deque

def printnames(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        current_dir = search_queue.popleft()
        print(current_dir)
        for file in listdir(current_dir):
            fullpath = join(current_dir, file)
            if isfile(fullpath):
                print(fullpath)
            else:
                search_queue.append(fullpath)

printnames("pics")