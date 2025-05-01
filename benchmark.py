import timeit
import random
from task1 import merge_sort, insertion_sort

# Створення масиву
data = [random.randint(0, 100000) for _ in range(100000)]

print("Час виконання алгоритмів на масиві з 10 000 елементів:")

# Merge Sort
merge_time = timeit.timeit("merge_sort(data)", setup="from __main__ import merge_sort, data", number=1, globals=globals())
print("Merge Sort:", round(merge_time, 6), "секунд")

# Insertion Sort
insert_time = timeit.timeit("insertion_sort(data)", setup="from __main__ import insertion_sort, data", number=1, globals=globals())
print("Insertion Sort:", round(insert_time, 6), "секунд")

# Timsort (built-in sorted)
timsort_time = timeit.timeit("sorted(data)", setup="from __main__ import data", number=1, globals=globals())
print("Timsort (built-in):", round(timsort_time, 6), "секунд")
