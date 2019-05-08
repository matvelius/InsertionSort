# Insertion sort iterates, consuming one input element each repetition,
# and growing a sorted output list. At each iteration, insertion sort
# removes one element from the input data, finds the location it belongs
# within the sorted list, and inserts it there. It repeats until no input
# elements remain.

# Sorting is typically done in-place, by iterating up the array, growing
# the sorted list behind it. At each array-position, it checks the value
# there against the largest value in the sorted list (which happens to be
# next to it, in the previous array-position checked). If larger, it leaves
# the element in place and moves to the next. If smaller, it finds the
# correct position within the sorted list, shifts all the larger values
# up to make a space, and inserts into that correct position.

array = [7, 1, 9, 4, 3, 5, 8, 6, 2]
########[1, 7, 9, 4, 3, 5, 8, 6, 2]


def insertionSort(array):

    # check if array is empty
    if len(array) == 0:
        return []

    # keep track of the array slice
    sliceStartIndex = 0
    sliceEndIndex = 0

    # keep track of largestValueSoFar
    largestValueSoFar = 0


    # while (we haven't reached the end of the array)
    # when (sliceEnd index = len(array) - 1)
    while sliceEndIndex < len(array) - 1:

    # grab element at sliceEnd (+ 1 ?)
    # if it's larger than largestValueSoFar, leave it in place.. otherwise
    # find the right spot for it
        # store in a temp variable
        currentValueToSort = array[sliceEndIndex]
        if currentValueToSort < largestValueSoFar:
            for indexOfValueToCheckAgainst in range(0, sliceEndIndex):
                valueToCheckAgainst = array[indexOfValueToCheckAgainst]
                # find the exact spot to place currentValueToSort
                if currentValueToSort < valueToCheckAgainst:
                    # move whatever's between indexOfValueTo.. and sliceEndIndex
                    # over to the right
                    # and place currentValueToSort at indexOfValueTo...
                    for valueToMove in reversed(array[indexOfValueToCheckAgainst:sliceEndIndex]:
                        array[sliceEndIndex]

        else:
            largestValueSoFar = currentValueToSort



    # compare with values below largestValueSoFar
    # find the correct position in the list
    #

    # shift all the larger values to the right:
    # iterate through array slice + 1
    # insert it there


    # iterate through the array backwards

    # increment sliceEnd
    sliceEndIndex += 1

    # return sorted array
    return array

