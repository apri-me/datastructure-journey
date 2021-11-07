
# DataStructure Journey
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)  
  
## Merge Sort
Merge Sort is an algorithm that solves the sorting problem with *Divide and Conquer* approach.
### Divide and Conquer
---
Maybe you first heard this expression in politics. In that context it means that encourage your united enemies to fight each other and then conquer them as they're weaker without each other.

Actually in computer science *Divide and Conquer* means almost the same. It means that you need to recursively break down your problem into sub-problems and then try to solve them and combine them.

So there's three steps in each *Divide and Conquer* algorithm.

 1. **Divide**:
 Divide the problem into smaller subproblems.
 2. **Conquer**:
 Conquer subproblems by solving them recursively and if the size of subproblem is small enough (base case), solve them in straight-forward manner.
 3. **Combine**:
 Combine the solutions of subproblems to reach the solution of larger subproblems and finally the solution of original problems.

### Merge Sort
---
Now we define *Merge Sort* Algorithm in terms of *Divide and Conquer* approach.

 1. **Divide**:
 Divide each n-element sequence that should be sorted, into two subsequence of ( n / 2 ) elements each.
`q = floor((p+r) / 2)`
 2. :**Conquer**:
 Sort two subsequence recursively and if size of subsequence is very small just return it.
 `merge_sort(A, p, q)`
 `merge_sort(A, q+1, r)`
 3. : **Combine**:
 Merge the two subsequences that is sorted and produce the sorted answer.
 `merge(A, p, q, r)`
### Analysis:
---
#### Time:
We denote the time of algorithm by *T(n)*. Then we analyze this algorithm step by step. In *Divide* step it takes constant time to calculate `q` so it is *&theta;(1)*.  Conquer step is to solving two subproblem with half-size input. So it takes *2 &times; T(n)*. And in the last step, combining two sorted subsequence takes *&Theta;(n)* time for both worst case and best case. It means that:
<p align='center'><i> T(n) = 2 &times; T(n/2) + &Theta;(n) </i> </p>
Obviously it's a recursive relation, and after a lot of calculations we can say that:

<p align='center'><i> T(n) = &Theta;(n log(n) )</i> </p>

#### Memory:
Nowadays most sorting algorithms are in-place. It means that they don't use extra memory beside input. But merge sort's weakness is memory and it uses *&Theta;(n)* amount of memory. 

You may see in books and internet that it takes exactly same mount of memory as input, but in our version of merge code at most it uses about *1/2* of input size.
