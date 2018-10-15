<Heap Sort>

1. buildHeap
- Should be the complete binary tree
- Each element's position in the list should be corresponded with the position of tree
- Loop 'heapify' for n//2 times where n is the last element's position
  (It means nth node is the last child of the sub-parent node)

2. heapify
- Modifies the tree for each element to be located in right place
- In this case, the parent node should always be smaller than its children nodes.
- 1) Compare the left child node & the right child node
     Determine the smaller child
     (If there is no right child node, left child should be)
- 2) Compare the parent node to smaller node
- 3) Smaller node should be located in the parent node's position
     ==> switch the elements in the list

3. HeapSort
- Make the element in the list be sorted in descending order

- 1) buildHeap
- 2) Pick the Root element(which is located A[0])
- 3) Switch it to the last element (According to deletion of heap)
- 4) Use heapify to adjust the position of heap
- 5) Until all element is picked

