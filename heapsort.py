# Heap Sort

def left(i):
  return 2*i+1

def right(i):
  return 2*i+2

def parent(i):
  return abs(i/2)

def maxHeapify(A, i):
  l = left(i)
  r = right(i)

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

  print()
  print("Largest Index: ", largest)
  print("Largest Value: ", A[largest])  

  if largest != i:
    A[largest], A[i] = A[i], A[largest]
    maxHeapify(A, largest)
    
def buildMaxHeap(A):
  size = int(len(A)/2)
  for i in range(size, -1, -1):
    print("BUILD #: ", i)
    maxHeapify(A, i)

