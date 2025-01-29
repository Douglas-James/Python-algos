# Chapter 5: Hash Tables

This chapter focuses on how we can use hash tables, which are used for caching by companies like Facebook and Google. We will also cover collisions in hash tables and the performance of hash tables in terms of Big O notation for different operations such as deletion and adding.

## Hash Tables Overview

A hash table is a data structure that maps keys to values. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

## Uses of Hash Tables

- **Caching**: Hash tables are used for caching data to improve performance. For example, Facebook and Google use hash tables to cache frequently accessed data.
- **Database Indexing**: Hash tables are used to index database records for quick retrieval.
- **Sets**: Hash tables can be used to implement sets, which are collections of unique elements.

## Handling Collisions

Collisions occur when two keys hash to the same index. There are several methods to handle collisions:

- **Chaining**: Store multiple elements in the same index using a linked list.
- **Open Addressing**: Find another open slot within the hash table.

## Performance of Hash Tables

The performance of hash tables is typically measured in terms of Big O notation:

| Operation | Average Case | Worst Case |
| --------- | ------------ | ---------- |
| Insert    | O(1)         | O(n)       |
| Delete    | O(1)         | O(n)       |
| Search    | O(1)         | O(n)       |

In the average case, hash table operations (insert, delete, search) have a time complexity of O(1). However, in the worst case, due to collisions, the time complexity can degrade to O(n).

## Graphic Table

Below is a graphic representation of the performance of hash table operations:

```
+-----------+--------------+------------+
| Operation | Average Case | Worst Case |
+-----------+--------------+------------+
| Insert    | O(1)         | O(n)       |
| Delete    | O(1)         | O(n)       |
| Search    | O(1)         | O(n)       |
+-----------+--------------+------------+
```

This table summarizes the time complexity for hash table operations.
