# 1 mark questions

```
1. What is a use case for a metaclass in Python?
Dynamically altering class creation behaviour.
```
```
2. Which of the following is true about Python’s Global Interpreter Lock (GIL)?
It allows only one thread to execute Python bytecode at a time.
```
```
3. What is the purpose of the `staticmethod` decorator in Python?
It allows a method to be called without instantiating the class.
```
```
4. What is the key difference between `@staticmethod` and `@classmethod` decorators in Python?
@classmethod can be used to create factory methods, whereas @staticmethod cannot.
```
```
5. How can you sort a Python dictionary by its values in descending order?
sorted(d.items(), key=lambda x: x[1], reverse=True)
```
```
6. Which of the following statements about Python’s `asyncio` module is true?
It enables asynchronous I/O in Python.
```
```
7. What is the difference between `__getattr__` and `__getattribute__` in Python?
__getattribute__ is called when an attribute lookup is attempted, and it is called for every attribute regardless whether it exists or not. It’s a part of the lookup chain that gets invoked before looking at the actual attributes on the object.

__getattr__, on the other hand, is only called when an attribute is not found in the usual places (i.e., it’s not an instance attribute nor is it found in the class tree for self). It’s used to define custom behavior when an attribute is not found.
```
```
8. What is the purpose of the `@functools.lru_cache` decorator in Python?
It caches the result of the function based on its arguments, avoiding redundant calculations.
```
```
9. What is python's 'pickle' module?
Python's `pickle` module is used for serializing and deserializing Python object structures, also called marshalling or flattening. Serialization refers to the process of converting a Python object into a byte stream to save it to a file or database, or to send it over a network. Deserialization is the inverse process of decoding the byte stream back into a Python object. This is useful for saving complex data types like Python dictionaries, lists, or class instances in a format that can be reconstructed later in the same or another Python program.
```