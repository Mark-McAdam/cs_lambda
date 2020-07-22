'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(array):
    # Your code here
    # set end equal to one less than length of array
    end = len(array)-1
    # start at index 0 and work towards the end 
    current = 0
    
    # end when the current is the
    # same as the end

    # or run until current equals end
    while current < end:
        # if the current value is equal to zero
        # fancy swap it to the end
        if array[current] == 0:
            # fancy swap
            array[current], array[end] = array[end], array[current]
            #decrement end 
            end -= 1
        #increment current     
        current =+ 1
    return array

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")