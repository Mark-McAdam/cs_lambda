def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
            if arr[i] ==  target:
                return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # save pointers for an iterative approach
    min = 0
    max = len(arr)-1

    # Your code here
    while min <= max:
        # find mid-point
        mid = (max + min) // 2

        if arr[mid] > target:
            # shift down
            max = mid + 1
        elif arr[mid] < target:
            # shift up
            min = mid - 1
        else: # if arr[mid] == target
            # target found
            return mid

    return -1  # not found