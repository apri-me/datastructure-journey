
# DataStructure Journey

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
## Divide and Conquer


Maybe you first heard this expression in politics. In that context it means that encourage your united enemies to fight each other and then conquer them as they're weaker without each other.

  

Actually in computer science *Divide and Conquer* means almost the same. It means that you need to recursively break down your problem into sub-problems and then try to solve them and combine them.

  

So there's three steps in each *Divide and Conquer* algorithm.

  

1.  **Divide**:

Divide the problem into smaller subproblems.

2.  **Conquer**:

Conquer subproblems by solving them recursively and if the size of subproblem is small enough (base case), solve them in straight-forward manner.

3.  **Combine**:

Combine the solutions of subproblems to reach the solution of larger subproblems and finally the solution of original problems.

## Time Complexity
Technically an algorithm that is implemented by *Divide and Conquer* approach are recursive algorithms. In each recursion, algorithm tries to divide original problem to one or multiple sub-problems with smaller input size. Then after solving each sub-problem we reach *combine* step. 

Assume in each recursion original problem divides into *a* sub-problem with *n/b* input size and the time complexity of *combine* step is denoted by *f(n)*. Thus we can show the time complexity of every *Divide and Conquer* algorithm by below function:

<p align=center > <i>T(n) =  a &times; T(n/b) + f(n)</i></p>

## Algorithms
  There are a lot of algorithms that uses *Divide and Conquer* approach. Here are some of them that we implemented.
 

 - [Merge Sort](../sorting_problem/merge_sort)
 - [Quick Sort](../sorting_problem/quick_sort)
 - [Maximum Finder](max_finder)
 - &#8943;

