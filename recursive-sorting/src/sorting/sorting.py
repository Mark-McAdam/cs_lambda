# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # different approach than indicated in module
    # start with 0 to inc from initial results list
    a, b = 0, 0
    result = []

    while a < len(arrA) and b < len(arrB):
        # handle while a and b < len A/B   
        if arrA[a] < arrB[b]:
            result.append(arrA[a])
            a += 1
        # otherwise do 
        else:
            result.append(arrB[b])
            b += 1

    result += arrA[a:]
    result += arrB[b:]
    return result

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    
    #case 1 if length less than equal to 1 
    if len(arr) <= 1:
        return arr

    #cases for mid left right 
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

