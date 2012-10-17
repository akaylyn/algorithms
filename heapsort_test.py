from heapsort import *

A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print("Original: ", A)

buildMaxHeap(A)
print("Heapified: ", A)

sortedList = heapsort(A)
print("Sorted: ", sortedList)


