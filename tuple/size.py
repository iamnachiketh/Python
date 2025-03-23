import sys
import timeit

tuple_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tuple_size = sys.getsizeof(tuple_data)
list_size = sys.getsizeof(list_data)

tuple_creation_time = timeit.timeit("tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))", number=1000000)
list_creation_time = timeit.timeit("list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])", number=1000000)

print(f"Size of tuple: {tuple_size} bytes")
print(f"Size of list: {list_size} bytes")
print(f"Creation time for tuple (in seconds): {tuple_creation_time}")
print(f"Creation time for list (in seconds): {list_creation_time}")