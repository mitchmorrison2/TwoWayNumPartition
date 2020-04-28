import itertools

# read in our number set
with open('Data.txt', 'r') as f:
    data = f.read().split()
    # elements = map(int, elements)

"""
# trivial implementation of finding the best way to partition the set
# @param list of numbers representing set of processes
# @return two partitioned sets close in sum
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

    # print(best_set, "sum = ", sum(map(int, best_set)))
    # print(other_set, "other set sum = ", sum(map(int, other_set)))

    # return both sets as a list of ints
    return list(map(int, other_set)), list(map(int, best_set))


"""
# robust heuristic implementation to find efficient and best way to partition the set
# @param list of numbers representing set of processes
# @return two partitioned sets close in sum
"""


def robust_implementation(elements):
    # performing two way set partition using karmarkar-karp algorithm
    x = sorted(map(int, elements), reverse= True)
    set1 = []
    set2 = []
    # set_diff represents the difference in scores of sum(set1) - sum(set2)
    # when it is positive, set1 has a larger sum and vice versa
    set_diff = 0

    # print(x)
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

    # print("set 1 = ", set1)
    # print("set 2 = ", set2)
    # print("set differences = ", set_diff)
    # print("calc set diff = ", sum(set1) - sum(set2))

    # return both sets
    return set1, set2


if __name__ == '__main__':
    # call trivial implementation
    triv_set1, triv_set2 = trivial_implementation(data)
    # call robust implementation
    rob_set1, rob_set2 = robust_implementation(data)

    print(sorted(triv_set1, reverse=True), sorted(triv_set2, reverse=True))
    print("Trivial remainder:", abs(sum(triv_set1) - sum(triv_set2)))
    print(rob_set1, rob_set2)
    print("Robust remainder:", abs(sum(rob_set1) - sum(rob_set2)))

