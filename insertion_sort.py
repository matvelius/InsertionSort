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

array = [7, 1, 9, -4, 3, 5, 8, 6, 2]
########[1, 7, 9, 4, 3, 5, 8, 6, 2]


def insertionSort(array):

    # check if array is empty
    if len(array) == 0:
        return []

    print(f"starting with: {array}")

    # keep track of the array slice
    sliceStartIndex = 0
    sliceEndIndex = 0

    # keep track of largestValueSoFar
    largestValueSoFar = 0


    # while (we haven't reached the end of the array)
    # when (sliceEnd index = len(array) - 1)
    while sliceEndIndex < len(array):

    # grab element at sliceEnd (+ 1 ?)
    # if it's larger than largestValueSoFar, leave it in place.. otherwise
    # find the right spot for it
        # store in a temp variable
        currentValueToSort = array[sliceEndIndex]
        print(f"currentValueToSort: {currentValueToSort}")
        if currentValueToSort < largestValueSoFar:
            for indexOfValueToCheckAgainst in range(0, sliceEndIndex):
                valueToCheckAgainst = array[indexOfValueToCheckAgainst]
                print(f"valueToCheckAgainst: {valueToCheckAgainst}")
                # find the exact spot to place currentValueToSort
                if currentValueToSort < valueToCheckAgainst:
                    print("currentValueToSort is < valueToCheckAgainst")
                    # move whatever's between indexOfValueTo.. and sliceEndIndex
                    # over to the right...
                    for movingIndex in reversed(range(indexOfValueToCheckAgainst + 1, sliceEndIndex + 1)):
                        print(f"movingIndex: {movingIndex}")
                        print(f"array[movingIndex] was: {array[movingIndex]}")
                        array[movingIndex] = array[movingIndex - 1]
                        print(f"array[movingIndex] is now: {array[movingIndex]}")

                    # ...and place currentValueToSort at indexOfValueTo...
                    array[indexOfValueToCheckAgainst] = currentValueToSort
                    print(f"array is now: {array}")
                    break
        else:
            largestValueSoFar = currentValueToSort
            print(f"setting largestValueSoFar to: {largestValueSoFar}")

        # increment sliceEnd
        sliceEndIndex += 1

    # return sorted array
    print(f"final result: {array}")
    return array

insertionSort(array)