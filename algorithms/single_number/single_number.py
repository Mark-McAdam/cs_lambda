'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    arr.sort()
    # with duplicates side by side
    # loop through all pairs and check for duplicates
    for i in range(0, len(arr)-1, 2):
        if arr[i] != arr[i+1]:
            # If the values don't match 
            # return the value
            return arr[i]
    
    # odd size list of numbers 
    # loop will never reach the end value 
    # if end value was the single value 
    # and it was largest value 
    return arr[-1]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")