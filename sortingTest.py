import types
from bubbleSort import BubbleSort
from mergeSort import MergeSort
from quickSort import QuickSort
from testVectorGenerator import *
from heapSort import HeapSort

sorted_correctly = -1           # return value
random_test_cases = list()      # a list of randomly ordered lists
all_permutations = list()       # a list of all permutations of a vector
all_possible_lists = list()     # a list of all possible sequences


class TestSortableObject:
    """An object that is ordered with a comparison function"""
    suits = ["clubs", "diamonds", "hearts", "spades"]  # ascending order
    values = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]    # ascending order

    def __init__(self, a, b):
        self.suit = a
        self.value = b

    def __repr__(self):
        return "<{} of {}>".format(self.value, self.suit)

    @staticmethod
    def compare(a, b):
        ret_val = 0
        i_a = TestSortableObject.suits.index(a.suit)
        i_b = TestSortableObject.suits.index(b.suit)
        if i_a < i_b:
            ret_val = -1
        elif i_a > i_b:
            ret_val = 1
        else:
            i_a = TestSortableObject.values.index(a.value)
            i_b = TestSortableObject.values.index(b.value)
            if i_a < i_b:
                ret_val = -1
            elif i_a > i_b:
                ret_val = 1
        return ret_val

    @staticmethod
    def generate_random_list():
        array = list()
        for i in TestSortableObject.suits:
            for j in TestSortableObject.values:
                array += [TestSortableObject(i, j)]
        random.seed()
        for i in range(0, 52):
            j = random.randrange(0, 52)
            tmp = array[0]
            array[0] = array[j]
            array[j] = tmp
        return array


def is_sorted(data: list, cmp):
    """Checks to see if the list is in the correct order """
    """  Returns index of first mismatch or -1 if no error"""
    num_elements = len(data)
    if num_elements > 1:
        for i in range(0, num_elements-1):
            if cmp(data[i], data[i+1]) > 0:
                return i
    return sorted_correctly


def compare_ints(a: int, b: int):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


def test_sort(sorting_function: types.FunctionType, algorithm_name=""):
    """Sorts a series of lists using the function 'sorting_function' that is passed
        returns the count of errors.
        If sorting_function is None, it uses the built in list.sort()"""

    error_count = 0

    # Random tests give an average sort time, but do not check for optimizations
    print("Using", algorithm_name, " to sort ", len(random_test_cases),
          " lists of length ", len(random_test_cases[0]))

    for j in range(0, len(random_test_cases)):
        test_case = list(random_test_cases[j])    # make a copy
        print("Sorting with ", algorithm_name, ": ", test_case)
        if sorting_function:
            sorting_function(test_case, compare_ints)
        else:
            test_case.sort()
        if not is_sorted(test_case, compare_ints):
            error_count += 1
            print(" !!!!! ERROR !!!!! sort with ", algorithm_name, " failed:")
            print(" Before", random_test_cases[j])
            print(" After ", test_case)

    # Test that are affected by whether a sort is adaptive or not
    # sort_test_cases = list()
    # for q in range(0, i):
    #     sort_test_cases += [buildList(i)]
    print("Using {} to sort {} test cases consisting of all {} element lists that can be built using 0-{}".\
            format(algorithm_name, len(all_possible_lists), len(all_possible_lists[0]), all_possible_lists[-1][-1]))
    for j in range(0, len(all_possible_lists)):
        test_case = list(all_possible_lists[j])
        if sorting_function:
            sorting_function(test_case, compare_ints)
        else:
            test_case.sort()
        if not is_sorted(test_case, compare_ints):
            error_count += 1
            print(" !!!!! ERROR !!!!! sort with ", algorithm_name, " failed:")
            print(" Before", all_possible_lists[j])
            print(" After ", test_case)

    return error_count


if __name__ == '__main__':
    # Build the test cases first.  Each sort algorithm will go over the same test cases

    # random lists
    random_test_cases = list()
    num_random_lists = 30
    size_random_list = 30
    print("Generating {} randomized lists of length {}".format(num_random_lists, size_random_list))
    for q in range(0, num_random_lists):
        random_test_cases += [build_random_list(size_random_list)]

    # all permutations of the list [0, 0, 1, 1, 2, 2, 3, 3...] (two of each value)
    # list_to_permutate = list()
    # for j in range(0, i):
    #     list_to_permutate += [j]
    #     list_to_permutate += [j]
    # all_permutations = HeapPermutationGenerator.generatePermutations(list_to_permutate)
    # print("Using", algorithm_name, " to sort ", len(all_permutations), " permutations of: ", list_to_permutate)

    #   run through all the possible lists made from digits in a given base b: 0, 1, ... b-1
    #   Base 3 uses digits 0, 1, 2 which will test the comparator function returns 0, -1 & 1
    digit_base = 3
    num_digits = 10
    print("Generating all {} digit numbers of base {}".format(num_digits, digit_base))
    all_possible_lists = generate_all_n_digit_lists_of_values_m(num_digits, digit_base)

    # Sort the test cases using each set of test vectors

    bubble_sort_error_count = test_sort(BubbleSort.sort, "bubble sort")
    merge_sort_error_count = test_sort(MergeSort.sort, "merge sort")
    quick_sort_2w_error_count = test_sort(QuickSort.sort, "quick sort with 2-way partitioning")
    quick_sort_3w_error_count = test_sort(QuickSort.sortThreeWay, "quick sort with 3-way partitioning")
    heap_sort_error_count = test_sort(HeapSort.sort, "heap sort")
    built_in_sort_error_count = test_sort(None, "Built in sorting algorithm")

    print("bubble sort test completed with ", bubble_sort_error_count," errors")
    print("merge sort test completed with ", merge_sort_error_count, " errors")
    print("quick sort 2 way partitioning test completed with ", quick_sort_2w_error_count, " errors")
    print("quick sort 3 way partitioning test completed with ", quick_sort_3w_error_count, " errors")
    print("heap sort test completed with ", heap_sort_error_count, " errors")
    print("built in sorting algorithm completed with ", built_in_sort_error_count, " errors")
