# sortingInPython
Sorting Exercise 16 (in Python) from "Learn More Python the Hard Way 3"

The main purpose of implementing different sorting algorithms was to get practice using measuring performance.  
Using:  
__$python -m cProfile -s cumtime sortingTest.py__  
the speed of the different alrorithms was studied.  

Of the sorts that I wrote, as expected:   
1. Over psuedo-random lists, 
    * QuickSort (3 way partitioning) was fastest 
    * BubbleSort was slowest 
2. Over a collection of vectors [0, 0 ... 0] to [2, 2, ... 2]
    * BubbleSort compared well with the others since it is adaptive to the repeated patterns  

The built in list.sort() method was by the far the faster than any algorithm I coded.
