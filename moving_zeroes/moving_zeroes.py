'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    #set a count
    count = 0
    #for loop if not 0 set count to the index increase by 1
    for i in range(len(arr)):
        if(arr[i] !=0):
            arr[count] = arr[i]
            count += 1
# while count < len(arr) set to 0 and incresee by one
    while count < len(arr):
        arr[count] = 0
        count += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")