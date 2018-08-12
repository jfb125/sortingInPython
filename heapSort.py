class HeapSort:

    @staticmethod
    def heapify(a: list, comparator):
        if a and len(a) != 0:
            final_element_in_a = len(a)-1
            final_parent = HeapSort.parent(final_element_in_a)
            for i in range(final_parent, -1, -1):
                HeapSort.sink(a, i, comparator)

    @staticmethod
    def left_child(parent: int):
        """Returns the left child index of this parent index.
            This is based on 0 indexing: 0->1, 1->3, 3->7 or 2k+1"""
        return 2*parent+1

    @staticmethod
    def right_child(parent: int):
        """Returns the right child index of this parent index.
            This is based on 0 indexing: 0->2, 2->6 or 2k+2"""
        return 2*parent+2

    @staticmethod
    def parent(child: int):
        """Returns the parent index of this child, based on 0 indexing:
            1->0, 2->0,  3->1, 4->1, 5->2, 6->2 or (child-1)/2"""
        return (child-1)//2


    @staticmethod
    def sink(a: list, node_num: int, comparator):
        """Sinks node_num to the correct place in the array"""
        if not a or node_num < 0:
            return
        hsize = len(a)
        # determine where the final parent node is
        final_parent = HeapSort.parent(hsize-1)
        # while not at a leaf
        while node_num <= final_parent:
            # calculate the index of the left child of this node
            lchi = HeapSort.left_child(node_num)
            # if the left child is in the heap (this should always be True)
            if lchi < hsize:
                lch = a[lchi]
            # calculate the index of the right child of this node
            rchi = HeapSort.right_child(node_num)
            # if the right child is in the heap
            if rchi < hsize:
                rch = a[rchi]
            else:
                rch = None

            # there is no right child, so left must be compared or
            # there is a right child, so determine which child is greater
            if not rch or comparator(lch, rch) > 0:
                # the left child is the largest
                if comparator(lch, a[node_num]) > 0:
                    a[lchi] = a[node_num]
                    a[node_num] = lch
                    node_num = lchi
                else:
                    break   # no further sinking is necessary
            else:
                # the right child is the largest (or they are equal)
                if comparator(rch, a[node_num]) > 0:
                    a[rchi] = a[node_num]
                    a[node_num] = rch
                    node_num = rchi
                else:
                    break   # no further sinking is necessary

    @staticmethod
    def print_heap(a: list):
        node_width = 80
        the_end = len(a)
        i = 0
        elements_on_this_level = 1
        count = 0
        while i < the_end:
            print("{:^{}d}".format(a[i], node_width), end="")
            i = i+1
            count += 1
            if count == elements_on_this_level:
                elements_on_this_level *= 2
                count = 0
                node_width //= 2
                print()
        if count != 0:
            print()

    @staticmethod
    def sort(a: list, comparator):
        tmp = list()
#        print("HeapSort.sort() passed: ", a)
        HeapSort.heapify(a, comparator)
#        print("HeapSort.sort() after heapify")
#        HeapSort.print_heap(a)
        for i in range(len(a)-1, 0, -1):
            tmp.insert(0, a[0])             # store largest remaining item
            a[0] = a[i]                     # replace top with bottom of heap
            a.pop()                         # remove bottom from heap
            HeapSort.sink(a, 0, comparator) # sink the new top, which is small
        tmp.insert(0, a[0])
        a.clear()
        for i in range(0, len(tmp)):
            a.append(tmp[i])
#        print("Returning: ", a)

    @staticmethod
    def replace(a: list, v):
        ret = a[0]
        a[0] = v
        HeapSort.sink(a, 0)
        return ret