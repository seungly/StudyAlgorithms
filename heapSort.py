#2015313966 박승혜
#Heap Sort


def buildHeap(A, n):
     for i in range(n//2, 0, -1):
          heapify(A, i-1, n)

def heapify(A, k, n):
     left = 2 * k +1               #When parent is k, children's index in the list
     right = 2 * k+2               #(According to complete binary tree)

     print("Start heapify \n Current: ", A)

     if k == 0:                     #It is Root
          left = 1
          right = 2

     if (right<= n-1):             #Right child is not outranged = Right child is exist
          if (A[left]<A[right]):
               smaller = A[left]
               tmp = left
          else:
               smaller = A[right]
               tmp = right
     elif left<= n-1:                   #Only Left child is exist
          smaller = A[left]
          tmp = left
     else:
          return              #There are no leaves

     ##Change the position in the list
     if (smaller < A[k]):     #If child is smaller than its parent, swap
          a = A[k]
          A[k] = smaller
          A[tmp] = a

          print("heapify: ", A)
          heapify(A, tmp, n)

def heapSort(A, n):
     buildHeap(A,n)
     print("Heap: ", A)
     for i in range (n-1, 0, -1):
          print ("Pick The Root Element : ", i)
          tmp = A[0]               #Pick the root, and place it in the last position
          A[0] = A[i]              #The last element goes to root, and refine the heap
          A[i] = tmp               #Until all elements are sorted in descending order
          heapify(A, 0, i-1)
     print("***********\nHeapSort: ", A)


A = [7,3,2,5,6,1,4,8]
n = len(A)

heapSort(A, n)
