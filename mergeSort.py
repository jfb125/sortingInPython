import copy

class MergeSort:

    @staticmethod
    def sort(data: list, comparator):
        """Uses a merge sort to put data in order"""

        # Trap all the cases that could cause a crash
        if data is None:
            # invalid data
            return data
        if type(data) is not list:
            print("Error - MergeSort.sort(data, cmp): data not a list")
            return data
        if len(data) < 2:
            # an empty list or a list with 1 element is already sorted
            return data

        size = len(data)
        final_step = size     # once the span is > this, stop
        delta = 1
        dbg_round = 1
        while delta < final_step:
            # print("Sorting array with a span of {}".format(delta))
            new_data = [None]*size
            right_stop = 0
            dst = 0
            while right_stop < size:
                left = right_stop
                left_stop = left + delta
                right = left_stop
                right_stop = right + delta
                if left_stop >= size:
                    left_stop = size
                    right_stop = size
                elif right_stop > size:
                    right_stop = size
                # print("Sorting array from {} to {} against {} to {}".format(left, left_stop-1, right, right_stop-1))
                # loop until either all the left side or all the right side has been moved
                while left < left_stop and right < right_stop:
                    if comparator(data[left], data[right]) > 0:
                        new_data[dst] = data[right]
                        right += 1
                    else:
                        new_data[dst] = data[left]
                        left += 1
                    dst += 1
                # clear out any remaining left sides
                while left < left_stop:
                    new_data[dst] = data[left]
                    dst += 1
                    left += 1
                # clear out any remaining right sides
                while right < right_stop:
                    new_data[dst] = data[right]
                    dst += 1
                    right += 1
            for i in range(0, size):
                data[i] = new_data[i]
            del new_data
            dbg_round += 1
            delta = delta*2
