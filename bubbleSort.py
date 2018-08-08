class BubbleSort:
    """Implements a bubble sort"""
    @staticmethod
    def sort(data: list, comparator):
        """Progressively sink values from the top of the list to the bottom"""

        # Trap all the cases that could cause a crash
        if data is None:
            # invalid data
            return data
        if type(data) is not list:
            print("Error - BubbleSort.sort(data, cmp): data not a list")
            return data
        if not data or len(data) == 1:
            # an empty list or a list with 1 element is already sorted
            return data

        dbg_round_cnt = 1
        for stop_place in range(len(data)-1, 0, -1):
            had_exchange = False
            for j in range(0, stop_place):
                if comparator(data[j], data[j+1]) > 0:
                    tmp = data[j]
                    data[j] = data[j+1]
                    data[j+1] = tmp
                    had_exchange = True
            # print("BubbleSort after round #", dbg_round_cnt, ": ", data)
            dbg_round_cnt += 1
            if not had_exchange:
                break
        return data
