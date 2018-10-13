# StudyAlgorithms
Study Algorithms with '알고리즘 도감'

1. Insertion Sort
- Consider the most-left element is sorted already.
- Strat with the second element(which is not sorted), compare it with its left element.
  if smaller, moves left.
    until when it is bigger than its left element or it is located in the most-left position
  else, it is considered to be right place. (Other word, sorted.)
- Repeat until reaching the last element

2. Worst Case
- All elements are reversely sorted.
- 1 + 2 + 3 + .... + (n-2) + (n-1)
- O(n^2)

3. Average Case
- 1/2 * Worst Case
- O(n^2)

4. Best Case
- 1 + 1 + 1 + ... + 1 = n-1
- O(n)
