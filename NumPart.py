import itertools
import time

# read in our number set
with open('Data.txt', 'r') as f:
    data = f.read().split()

"""
# @desc: trivial implementation to find the best way to partition 
            the set into two sets of as close to equal sum as possible
# @param: elements: list of numbers (n < 30)
# @return: two partitioned sets
"""


def trivial_implementation(elements):
    # generate all combinations for set of elements
    min_diff = 1000000
    x = itertools.combinations(elements, 10)
    # find respective sums and store set with smallest difference from half sum all elements
    for a in x:
        sum_a = sum(map(int, a))
        set_diff = abs((sum(map(int, elements)))/2 - sum_a)
        if set_diff < min_diff:
            min_diff = set_diff
            best_set = a
            # print("Difference between the two sets = ", min_diff)

    other_set = []
    for e in elements:
        if e not in best_set:
            other_set.append(e)

    # return both sets as a list of ints
    return list(map(int, other_set)), list(map(int, best_set))


"""
# @desc: robust heuristic implementation to find efficient (and near best)
            way to partition the set into two sets of equal sum
# @param: list of integers for two-way partitioning
# @return: two partitioned sets
"""


def robust_implementation(elements):
    # performing two way set partition using karmarkar-karp algorithm
    x = sorted(map(int, elements), reverse= True)
    set1 = []
    set2 = []
    # set_diff represents the difference in scores of sum(set1) - sum(set2)
    # when it is positive, set1 has a larger sum and vice versa
    set_diff = 0

    var = True
    count = 0
    while count < len(x):
        # if difference is greater than 0, set1 has a larger score
        if set_diff > 0:
            # subtract from set_diff because you are giving the larger score to set2
            if x[count] > x[count+1]:
                # add larger element to set2
                set2.append(x[count])
                set1.append(x[count+1])
                set_diff = set_diff - (x[count] - x[count+1])
            else:
                set1.append(x[count])
                set2.append(x[count+1])
                set_diff = set_diff - (x[count+1] - x[count])
        # set 2 has a larger or equal score
        else:
            # subtract difference between elements from set_diff because larger element is going into set1
            if x[count] > x[count+1]:
                # add larger element to set1
                set1.append(x[count])
                set2.append(x[count+1])
                set_diff = set_diff + (x[count] - x[count+1])
            else:
                set2.append(x[count])
                set1.append(x[count+1])
                set_diff = set_diff + (x[count+1] - x[count])

        # increment counter by 2 because moving in pairs
        count = count + 2

        # edge case for odd amounts of elements in a set
        if count == len(x) - 1:
            print(x[count], " ")
            print(sum(set1), sum(set2))
            if set_diff > 0:
                set2.append(x[count])
                set_diff = set_diff - x[count]
            else:
                set1.append(x[count])
                set_diff = set_diff + x[count]
            break

    # return both sets
    return set1, set2


if __name__ == '__main__':

    # call trivial implementation
    start_trivial = time.perf_counter()
    triv_set1, triv_set2 = trivial_implementation(data)
    elapsed_triv = (time.perf_counter() - start_trivial)

    print(sorted(triv_set1, reverse=True), sorted(triv_set2, reverse=True))
    print("Trivial remainder:", abs(sum(triv_set1) - sum(triv_set2)))
    print("Time required for trivial implementation: ", elapsed_triv, " seconds\n\n")

    # call robust implementation
    start_robust = time.perf_counter()
    rob_set1, rob_set2 = robust_implementation(data)
    elapsed_robust = (time.perf_counter() - start_robust)

    print(rob_set1, rob_set2)
    print("Robust remainder:", abs(sum(rob_set1) - sum(rob_set2)))
    print("Time required for robust implementation: ", elapsed_robust, "seconds\n\n")

