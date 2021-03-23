def smallestDifference(arrayOne, arrayTwo):

    arrayOne.sort()
    arrayTwo.sort()
    data = []
    i, j = 0, 0
    smallest_val = float("inf")

    while (i < len(arrayOne) and j < len(arrayTwo)):
        arr1 = arrayOne[i]
        arr2 = arrayTwo[j]
        diff = abs(arr1-arr2)

        if diff < smallest_val:
            smallest_val = diff
            data = [arrayOne[i], arrayTwo[j]]

        if (arr1 > arr2):
            j += 1
        elif (arr1 < arr2):
            i += 1
        else:
            return [arr1, arr2]

    return data


arr1 = [-1, 3, 5, 10, 20, 28]
arr2 = [15, 17, 26, 134, 135]
print(smallestDifference(arr1, arr2))
