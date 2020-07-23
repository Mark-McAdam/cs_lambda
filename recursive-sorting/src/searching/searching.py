# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # first solution 
    # case 1 start greater than end 
    if start > end:
        return -1
    # mid 
    mid = (start + end) // 2
    
    # if target and mid are same return the mid
    if target == arr[mid]:
        return mid

    # if target is less than mid 
    # recursion start at start end mid-1 
    if target < arr[mid]:
        return binary_search(arr, target, start, mid-1)
    # else     
    # recursion start at mid+1 end end 
    else:
        return binary_search(arr, target, mid+1, end)


    # our tl shared this solution with us 
#     if start > end:
#         return -1
#     else:
#         mid = (start + end) // 2
# ​
#         if arr[mid] == target:
#             return mid
# ​
#         elif arr[mid] > target:
#             return binary_search(arr, target, start, mid - 1)
# ​
#         else:
#             return binary_search(arr, target, mid + 1, end)



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
