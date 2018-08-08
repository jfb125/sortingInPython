class QuickSort:

    message_level = 0
    quicksort_msg_level_none = 0    # don't do any checking
    quicksort_msg_level_error = 1   # only report errors
    quicksort_msg_level_debug = 2   # report all diagnostic messages

    @staticmethod
    def swap(data: list, i, j):
        tmp = data[i]
        data[i] = data[j]
        data[j] = tmp

    @staticmethod
    def isThreeWayPartitioned(data: list, left: int, right: int, comparator, pval):
        """Verifies that the data is partitioned around pval
            <pval, ... <pval | pval ... pval | >pval ... > pval"""
        i = left
        # move through the left side to find the first value > partition
        while i <= right and comparator(data[i], pval) < 0:
            i += 1
        if i > right:
            return True     # no values > or = partition were found
        while i <= right and comparator(data[i], pval) == 0:
            i += 1
        if i > right:
            return True     # no values > partition were found
        while i <= right and comparator(data[i], pval) > 0:
            i += 1
        return i > right    # if not early breakouts from loops, partitioning is correct

    @staticmethod
    def isPartitioned(data: list, left: int, right: int, comparator, n: int):
        """Verifies that everything before the nth element is <= [n] and
            that everything after the nth element is >= [n]"""
        stop_place = right+1
        part_value = data[n]
        for i in range(left, n):
            if comparator(data[i], part_value) > 0:
                print("NOT PARTITIONED CORRECTLY, left side: data[",i,"]=",data[i]," > data[",n,"]=",data[n])
                return False
        for i in range(n+1, stop_place):
            if comparator(data[i], part_value) < 0:
                print("NOT PARTITIONED CORRECTLY, right side: data[",i,"]=",data[i]," < data[",n,"]=",data[n])
                return False
        return True

    @staticmethod
    def partition(data: list, comparator, left, right):
        """Partitions the array around a value 'v' such that:
             all elements on the left side of the partition value's place are <= partition value
             all elements on the right side of the partition value's place are >= partition value
           The partition value 'v' is chosen as the value in the left most place (data[left])
           Inputs: data,            a list of value to sort
                   comparator(a,b)  a function that returns -1 if a > b, 0 if a==b and 1 if a < b
                   left             index of data[]'s left most element to include
                   right            index of data[]'s right most element to include
           Returns: position of partition value"""

        # the value in the array that will form the partition
        partition_value = data[left]
        # this value will be continuously pre-decremented, then the array value will be checked against partition
        # this value will eventually stop because it will reach the partition_value's position of [0]
        descending_smaller_seeker = right+1
        # this value will be continuously pre-incremented, then the array value will be checked against partition
        #   if this value is equal to or smaller than descending_smaller_seeker.  It is possible that there
        #   will be no values in the array that are less than the partition_value.
        ascending_larger_seeker = left

        while True:
            # Starting with the next item on the left side of the array
            ascending_larger_seeker += 1
            # find the left-most item in the array that is greater than **or equal** to partition
            while comparator(data[ascending_larger_seeker], partition_value) < 0:
                # make sure that we do not go past the right end of the array
                if ascending_larger_seeker >= right:
                    break
                ascending_larger_seeker += 1

            # Starting with the next item on the right side of the array
            descending_smaller_seeker -= 1
            # find the right-most item in the array that is less than the partition
            while comparator(partition_value, data[descending_smaller_seeker]) < 0:
                # make sure that we do not go past the left end of the array
                if descending_smaller_seeker <= left:
                    break
                descending_smaller_seeker -= 1

            # if the indexes have met, all values < 'partition_value' are to the left of meeting point
            #   all values > 'partition_value' are to the right of meeting point
            #   however, the meeting point may have the partition_value
            if ascending_larger_seeker >= descending_smaller_seeker:
                break

            # data[descending_smaller_seeker] is a value less than the partition that is on the right
            # data[ascending_larger_seeker] is a value greater than the partition that is on the left
            QuickSort.swap(data, ascending_larger_seeker, descending_smaller_seeker)

        # swap the partition value with the value before ascending_larger_seeker,
        #    which is either the right-most value < partition_value OR
        #    the partition_value itself (e.g. [5, 6, 6, 6]
        QuickSort.swap(data, descending_smaller_seeker, left)

        if QuickSort.message_level > QuickSort.quicksort_msg_level_none:
            # any message level above an error should check that the list is partitioned
            if not QuickSort.isPartitioned(data, left, right, comparator, descending_smaller_seeker):
                print(left, " to ", right, " returning ", descending_smaller_seeker, " !!!PARTITIONING ERROR: ", data)
            elif QuickSort.message_level >= QuickSort.quicksort_msg_level_debug:
                # there was no error & the message level is set to 'debug'
                shadow = list()
                for i in range(0, len(data)):
                    shadow += [data[i]]
                print("{:-3} to {:-3} using {:-4} returning {:-3} for {}".format(left, right, partition_value,
                                                                                 descending_smaller_seeker, shadow))

        return descending_smaller_seeker

    @staticmethod
    def sort(data: list, comparator):
        """Sorts an array by partitioning smaller & smaller portions of the array"""
        if data is None or len(data) < 2:
            return
        right = len(data)-1
        partition_position = QuickSort.partition(data, comparator, 0, right)
        QuickSort.subArraySort(data, comparator, 0, partition_position-1)
        QuickSort.subArraySort(data, comparator, partition_position+1, right)

    @staticmethod
    def sortThreeWay(data: list, comparator):
        """Uses quick-sort with the optimization of partitioning into 3 bands"""
        if data is None or len(data) < 2:
            return
        QuickSort.subArraySortThreeWay(data, comparator, 0, len(data)-1)

    @staticmethod
    def subArraySort(data: list, comparator, left, right):

        if right <= left:
            return
        else:
            partition_position = QuickSort.partition(data, comparator, left, right)
            QuickSort.subArraySort(data, comparator, left, partition_position-1)
            QuickSort.subArraySort(data, comparator, partition_position+1, right)

    @staticmethod
    def subArraySortThreeWay(data: list, comparator, left, right):
        if right <= left:
            return

        value_of_partition = data[left]
        leftmost_copy_of_partition = left
        rightmost_unknown_value = right
        location_to_inspect = left+1
        while location_to_inspect <= rightmost_unknown_value:
            cmp = comparator(data[location_to_inspect], value_of_partition)
            if      cmp < 0:
                # the value is less than the partition, so it needs to be
                #  sent down below the band of partition values in the middle
                #  by exchanging it with the left-most location of the partition value
                data[leftmost_copy_of_partition] = data[location_to_inspect]
                data[location_to_inspect] = value_of_partition
                location_to_inspect += 1
                leftmost_copy_of_partition += 1
            elif    cmp > 0:
                # the value is greater than the partition, so it needs to be
                #  sent up to the right end of the array and whatever value is
                #  up at the right end of the array will get brought down to
                #  here so it can be compared on the next pass through the loop
                tmp = data[rightmost_unknown_value]
                data[rightmost_unknown_value] = data[location_to_inspect]
                data[location_to_inspect] = tmp
                rightmost_unknown_value -= 1
            else:
                # the value is the partition, look for the next value
                location_to_inspect += 1

        if QuickSort.message_level > QuickSort.quicksort_msg_level_none:
            if not QuickSort.isThreeWayPartitioned(data, left, right, comparator, value_of_partition):
                print("3-way partitioned over ", left, " to ", right, " using ", value_of_partition, " !!!ERROR!!! ", data)
            elif QuickSort.message_level >= QuickSort.quicksort_msg_level_debug:
                # there was no error & the message level is set to 'debug'
                shadow = list()
                for i in range(0, len(data)):
                    shadow += [data[i]]
                print("3-way partitioned over {:-3} to {:-3} using {:-4} gives {}".format(left, right,
                                                                                          value_of_partition, shadow))
                # print("3-way partitioned over ", left, " to ", right, " using ", value_of_partition, shadow)

        # sort the un-ordered left partition of the original array
        QuickSort.subArraySortThreeWay(data, comparator, left, leftmost_copy_of_partition-1)
        # sort the un-ordered right partition of the orininal array
        QuickSort.subArraySortThreeWay(data, comparator, rightmost_unknown_value+1, right)
