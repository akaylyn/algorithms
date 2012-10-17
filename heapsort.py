# Heap Sort

def left(i):
  return 2*i+1

def right(i):
  return 2*i+2

def parent(i):
  return abs(i/2)

def maxHeapify(A, i):
  # Set debug = 1 to see output
  debug = 0

  l = left(i)
  r = right(i)

  if debug:
    print()
    print("# Begin ###############################")
    print("A: ", A)
    print("i: ", i)
    # Print indexes in a tree
    print("---------------------------------------")
    print(" ", i)
    print(l, " ", r)
    print("---------------------------------------")

  if l < len(A) and A[l] > A[i]:
    largest = l
  else:
    largest = i
  
  if r < len(A) and A[r] > A[largest]:
    largest = r
    
  if debug:
    print()
    print("Largest Index: ", largest)
    print("Largest Value: ", A[largest])  

  if largest != i:
    A[largest], A[i] = A[i], A[largest]
    maxHeapify(A, largest)
    
def buildMaxHeap(A):
  size = int(len(A)/2)
  for i in range(size, -1, -1):
    maxHeapify(A, i)

def heapsort(A):
  debug = 0
  sortedA = []
  size = len(A)
  for i in range(size-1, -1, -1):
    if debug:
      print("---------------------------------------")
      print("i: ", i, "len(A):", len(A))
      print("swap ", A[0], A[i])
      print("insert", A[i], "at", i-size)
      
    A[0], A[i] = A[i], A[0]
    sortedA.insert(i-size, A[i])
    A.pop(i)

    if debug:
      print(A)
      print(sortedA)
      print()
      
    maxHeapify(A, 0)
  return sortedA
