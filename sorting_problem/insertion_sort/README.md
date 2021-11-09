

# DataStructure Journey
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

## Insertion Sort
Insertion sort works the way many people sort a hand of playing cards. We start with an empty left hand and the cards face down on the table. We then remove one card at a time from the table and insert it into the correct position in the left hand. To find the correct position for a card, we compare it with each of the cards already in the hand, from right to left.
This is an efficient algorithm for sorting a small number of elements.

## Process
The whole process in insertion sort is based on key an arbitary element in array and put it in it's correct place in sorted section of array.

It will need an iterator like i which can iterate through all elements and it has two main section in the array: 1-**Sorted Section**    2-**Unsorted section**

Each time, let say key = array[i]. It has another loop which discover key's correct possition in sorted section. When we iterate from i to correct index, we swap all elements to right side(Like right bitwise). We can say that after every loop in this algorithm, one of the unsorted section elements join sorted section and member of unsorted section is decreasing and number of sorted section is increasing. After finishing second loop, we are sure that key element is in it's correct place.

After doing this loop for whole array, all elements will be in their correct index and they are sorted.

### Example
[**12**, 11, 13, 5, 6  ]
Let us loop for i = 1 (second element of the array) to 4 (last element of the array)
i = 1. Since 11 is smaller than 12, move 12 and insert 11 before 12
[**11, 12**, 13, 5, 6  ]
i = 2. 13 will remain at its position as all elements in A[0..I-1] are smaller than 13
[**11, 12, 13**, 5, 6  ]
i = 3. 5 will move to the beginning and all other elements from 11 to 13 will move one position ahead of their current position.
[**5, 11, 12, 13**, 6  ]
i = 4. 6 will move to position after 5, and elements from 11 to 13 will move one position ahead of their current position.
[**5, 6, 11, 12, 13**]
Now this array is sorted.


## Analysis

### Time complexity:

#### Best Case:

Best case for this algorithm will be an array which is sorted right now and function need to check every element once to see if it is sorted or not. Time complexity for this case will be
<div>T(n) = c<sub>1</sub>&times; n + (c<sub>2</sub> + c<sub>3</sub>) &times; (n - 1) + c<sub>4</sub> &times; (<span>  </span><sup>(n-1)(n)</sup> &#8260; <sub>2</sub><span>  </span>) + (c<sub>5</sub> + c<sub>6</sub>)&times;  ( (<span>  </span><sup>(n-1)(n)</sup> &#8260; <sub>2</sub><span>  </span>) - 1) + c<sub>8</sub> &times; (n - 1)</div>
<p align='center'><i> T(n) = O(n)</i> </p>

#### Worst Case:
Worst case for this algorithm will be a decreasing order array. In this case every element need to travel whole array for being in correct index. Time complexity for this case will be
<p align='center'><i> T(n) =O(n<sup>2</sup>)</i> </p>

#### Average Case:
For average case let's say: T( n ) = C1 * n + ( C2 + C3 ) * ( n - 1 ) + C4/2 * ( n - 1 ) ( n ) / 2 + ( C5 + C6 )/2 * ( ( n - 1 ) (n ) / 2 - 1) + C8 * ( n - 1 )
<p align='center'><i> T(n) =O(n<sup>2</sup>)</i> </p>

### Memory Complexity:
This algorithm is an in place algorithm and it doesn't use any extra memory. Due to this fact, memory comlexity for this algorithm is O(1).
