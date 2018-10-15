#2015313966 박승혜
#Counting Sort


def countingSort(A, B, n):
     C=[0 for i in range(k)]
     print (C)
     for j in range(0, n):
          C[A[j]]+=1
     print("Counting: ", C)
     for i in range(1, k):
          C[i] = C[i] + C[i-1]
     print("Counting2: ", C)
     for j in range(n-1, -1, -1):
          B[C[A[j]]-1] = A[j]
          C[A[j]]-=1
     print("countingSort: ", B)


A = [3,3,2,1,1,2,0,3,2,1,4,0]
n= len(A)
B = [0 for i in range(n)]
k = 5

countingSort(A,B,n)
