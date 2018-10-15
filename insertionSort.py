#2015313966 박승혜
#Insertion Sort


def insertionSort(A):
     for i in range(1, len(A)):                   # Start with the second element
          tmp = A[i]                         #The element which is going to move
          j = i-1                            #The element which is compared with 'tmp'
          while j>=0:                             #Loop until compared element's position is zero
               print ("Current: ", A)
               if (tmp < A[j]):
                    A[j+1] = A[j]                 #Compared element which is bigger than tmp, moved to j+1 position
                    A[j] = tmp                    # On that empty position, tmp is placed
                    print("Moving: ", A)
                    j = j-1
               else:
                    print ("Not change")
                    break
                    

A = [7, 3, 2, 5, 6, 1, 4, 8]
insertionSort(A)
