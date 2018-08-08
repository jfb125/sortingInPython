import random


class HeapPermutationGenerator:

    @staticmethod
    def generatePermutations(src: list):
        """Generates all the permutations of a list using heap's algorithm"""
        permutation_list = list()
        # make a copy of the source
        src_list = list(src)
        HeapPermutationGenerator.heapPermutation(permutation_list, src_list, len(src), len(src))
        return permutation_list

    @staticmethod
    def heapPermutation(dst: list, a: list, size: int, n: int):
        """Recursively calls itself with smaller & smaller arrays"""
        if size != 1:
            for i in range(0, size):
                HeapPermutationGenerator.heapPermutation(dst, a, size-1, n)

                if size % 2 == 1:
                    # if size is odd, swap first & last
                    tmp = a[0]
                    a[0] = a[size-1]
                    a[size-1] = tmp
                else:
                    tmp = a[i]
                    a[i] = a[size-1]
                    a[size-1] = tmp
        else:
            # print("Permutations generated: ", a)
            dst += [list(a)]    # make a deep copy of the new permutation


def generate_all_n_digit_lists_of_values_m(n: int, m: int):
    """Generates a list that contains all possible lists of length n that can be built with
        the values 0-(m-1): (2, 3)
        generates [[0,0], [1,0], [2,0],
                   [0,1], [1,1], [2,1],
                   [0,2], [1,2], [2,2]]"""

    return_value = list()
    one_vector = [0] * n
    stop_vector = [m - 1] * n
    while one_vector != stop_vector:
        return_value += [one_vector[:]]
        had_a_carry = True
        digit = 0
        while had_a_carry and digit != n:
            if one_vector[digit] == m - 1:
                had_a_carry = True
                one_vector[digit] = 0
                digit += 1
            else:
                had_a_carry = False
                one_vector[digit] += 1
    return_value += [stop_vector[:]]
    return return_value


def build_random_list(number):
    ex_data = list()
    random.seed()
    for i in range(0, number):
        ex_data += [random.randrange(0, number)]
    return ex_data


