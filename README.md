# sortingInPython
Sorting Exercise 16 (in Python) from "Learn More Python the Hard Way 3"

The main purpose of implementing different sorting algorithms was to get practice using measuring performance.  Using
$python -m cProfile -s cumtime sortingTest.py
the speed of the different alrorithms was studied.  As expected, over truly random inputs, quickSort (3 way partitioning) was fastest; BubbleSort was slowest.  However, when the algorithms were tested against lists that were partially ordered, BubbleSort was not much slower than the other sorts (MergeSort, QuickSort, QuickSort 3-way) since they are not adaptive as is BubbleSort.
The built in list.sort() method was by the far the fatest.
