# Chapter 3: Recursion and Stacks

In this chapter, we will explore the concepts of recursion and stacks, which are fundamental to many algorithms and data structures.

## Recursion

Recursion is a method of solving problems where a function calls itself as a subroutine. This allows the function to be repeated several times, as it can call itself during its execution.

### Example of a Recursive Function

```python
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
```

## Stacks

A stack is a data structure that follows the Last In, First Out (LIFO) principle. It allows operations at one end only, typically referred to as the "top" of the stack.

### Example of Stack Operations

```python
stack = []

# Push operation
stack.append(1)
stack.append(2)
stack.append(3)

# Pop operation
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1
```

Understanding recursion and stacks is crucial for solving complex problems efficiently. This chapter will provide you with the necessary knowledge and examples to master these concepts.
